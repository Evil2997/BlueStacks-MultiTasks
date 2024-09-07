import time

import cv2
import numpy as np
from rembg import remove
from sklearn.cluster import KMeans


def remove_background(image_path: str) -> np.ndarray:
    """
    Удаляет фон с изображения с помощью библиотеки rembg.

    :param image_path: Путь к изображению.
    :return: NumPy массив изображения без фона.
    """
    with open(image_path, "rb") as file:
        input_image = file.read()

    # Удаление фона
    output_image = remove(input_image)

    # Конвертируем результат в NumPy массив
    nparr = np.frombuffer(output_image, np.uint8)
    image_no_bg = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)

    return image_no_bg


def image_to_array(image_no_bg: np.ndarray) -> np.ndarray:
    """
    Преобразует изображение с удаленным фоном в RGB NumPy массив.

    :param image_no_bg: NumPy массив изображения с удаленным фоном.
    :return: NumPy массив изображения в формате RGB.
    """
    if image_no_bg.shape[2] == 4:  # Если есть альфа-канал (прозрачность)
        image_rgb = cv2.cvtColor(image_no_bg, cv2.COLOR_BGRA2RGB)
    else:
        image_rgb = cv2.cvtColor(image_no_bg, cv2.COLOR_BGR2RGB)

    return image_rgb


def get_dominant_colors(image_array: np.ndarray, num_colors: int = 5) -> np.ndarray:
    """
    Определяет наиболее часто встречающиеся цвета в изображении с помощью кластеризации.

    :param image_array: NumPy массив изображения.
    :param num_colors: Количество кластеров (цветов), которые нужно выделить.
    :return: NumPy массив доминирующих цветов (целые числа).
    """
    # Преобразуем изображение в двумерный массив пикселей
    pixels = image_array.reshape(-1, 3)

    # Используем KMeans для кластеризации пикселей
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)

    # Получаем центры кластеров (наиболее часто встречающиеся цвета)
    dominant_colors = kmeans.cluster_centers_

    # Преобразуем цвета в целые значения (0-255)
    dominant_colors = dominant_colors.astype(int)

    return dominant_colors


# Пример использования
image_path = r'C:\Users\Dmitriy\Pictures\Screenshots\yellow_text.png'

# Начинаем замер времени
start_time = time.time()

# Удаление фона
start_remove_bg = time.time()
image_no_bg = remove_background(image_path)
end_remove_bg = time.time()
print(f"Время удаления фона: {end_remove_bg - start_remove_bg:.2f} секунд\n")

# Преобразуем изображение без фона в RGB NumPy массив
start_rgb_conversion = time.time()
image_array = image_to_array(image_no_bg)
end_rgb_conversion = time.time()
print(f"Время преобразования изображения: {end_rgb_conversion - start_rgb_conversion:.2f} секунд\n")

# Находим 10 наиболее часто встречающихся цветов
start_color_analysis = time.time()
dominant_colors = get_dominant_colors(image_array, num_colors=10)
end_color_analysis = time.time()
print(f"Время анализа доминирующих цветов: {end_color_analysis - start_color_analysis:.2f} секунд\n")

# Выводим доминирующие цвета
print(f"Доминирующие цвета (без фона):\n{dominant_colors}")

# Сохраняем результат изображения без фона
start_save_image = time.time()
cv2.imwrite(r'C:\Users\Dmitriy\Pictures\Screenshots\111.png', cv2.cvtColor(image_no_bg, cv2.COLOR_RGBA2BGRA))
end_save_image = time.time()
print(f"Время сохранения изображения: {end_save_image - start_save_image:.2f} секунд\n")

# Полное время выполнения
end_time = time.time()
print(f"Полное время работы скрипта: {end_time - start_time:.2f} секунд")
