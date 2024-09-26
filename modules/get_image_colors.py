from typing import Tuple

import cv2
import numpy as np
from rembg import remove
from sklearn.cluster import KMeans


def remove_background(image_path: str) -> np.ndarray:
    """
    Удаляет фон с изображения с помощью библиотеки rembg и выполняет переворот цветов (BGR -> RGB).

    :param image_path: Путь к изображению.
    :return: NumPy массив изображения без фона в формате RGB.
    """
    # Считываем изображение с помощью OpenCV
    image_bgr = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    # Преобразуем BGR в RGB (если нужно)
    if image_bgr.shape[2] == 4:  # Если есть альфа-канал (RGBA)
        image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGRA2RGBA)
    else:  # Если нет альфа-канала (BGR)
        image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

    # Преобразуем изображение в байты
    _, encoded_img = cv2.imencode('.png', image_rgb)
    input_image = encoded_img.tobytes()

    # Удаление фона
    output_image = remove(input_image)

    # Конвертируем результат в NumPy массив
    nparr = np.frombuffer(output_image, np.uint8)
    image_no_bg = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)

    return image_no_bg


def filter_visible_pixels(image_with_alpha: np.ndarray) -> np.ndarray:
    """
    Фильтрует пиксели, оставляя только те, где альфа-канал полностью непрозрачный (255).

    :param image_with_alpha: NumPy массив изображения в формате RGBA.
    :return: NumPy массив только видимых пикселей (RGB).
    """
    if image_with_alpha.shape[2] == 4:  # Проверяем, есть ли альфа-канал
        # Маска для полностью непрозрачных пикселей (где альфа-канал == 255)
        opaque_mask = image_with_alpha[:, :, 3] == 255

        # Оставляем только непрозрачные пиксели и убираем альфа-канал
        visible_pixels = image_with_alpha[opaque_mask]
        visible_pixels_rgb = visible_pixels[:, :3]  # Берем только RGB каналы

        return visible_pixels_rgb
    else:
        # Если альфа-канала нет, возвращаем изображение как есть
        return image_with_alpha


def get_dominant_colors(image_array: np.ndarray, num_colors: int = 5) -> np.ndarray | None:
    """
    Определяет наиболее часто встречающиеся цвета в изображении с помощью кластеризации.

    :param image_array: NumPy массив видимых пикселей (RGB).
    :param num_colors: Количество кластеров (цветов), которые нужно выделить.
    :return: NumPy массив доминирующих цветов (целые числа).
    """
    # Преобразуем изображение в двумерный массив пикселей
    pixels = image_array.reshape(-1, 3)
    if pixels.shape[0] == 0:
        print("Нет видимых пикселей для обработки. Проверьте исходное изображение или фильтрацию.")
        return None

    # Используем KMeans для кластеризации пикселей
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)

    # Получаем центры кластеров (наиболее часто встречающиеся цвета)
    dominant_colors = kmeans.cluster_centers_

    # Преобразуем цвета в целые значения (0-255)
    dominant_colors = dominant_colors.astype(int)

    return dominant_colors


def color_spectrum_scanner(template_image: str, num_colors: int) -> np.ndarray:
    """
    Обрабатывает изображение, удаляет фон, фильтрует только видимые пиксели и находит доминирующие цвета.

    :param template_image: Путь к изображению для обработки.
    :param num_colors: Количество доминирующих цветов, которые нужно выделить.
    :return: NumPy массив доминирующих цветов в формате RGB.
    """
    image_path = f"Images/{template_image}.png"
    # Удаление фона с изображения
    image_no_bg = remove_background(image_path)

    # Фильтрация только видимых (непрозрачных) пикселей
    image_array = filter_visible_pixels(image_no_bg)

    # Нахождение доминирующих цветов
    return get_dominant_colors(image_array, num_colors=num_colors)


def get_rgb_bounds(colors: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Получает нижнюю и верхнюю границы цвета в RGB на основе списка цветов.

    :param colors: NumPy массив цветов в формате RGB (shape: Nx3).
    :return: Нижняя и верхняя границы цвета в RGB в формате np.ndarray.
    """
    # Преобразуем список RGB цветов в формат NumPy массива, если это еще не массив
    if not isinstance(colors, np.ndarray):
        colors = np.array(colors)

    # Определим нижние и верхние границы по каждому каналу (R, G, B)
    lower_bound = np.min(colors, axis=0)  # Минимальные значения для каждого канала
    upper_bound = np.max(colors, axis=0)  # Максимальные значения для каждого канала

    return lower_bound, upper_bound
