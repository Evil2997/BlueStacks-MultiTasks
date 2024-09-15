click_at_moon = ["click_at_moon"]
find_BUMP_1 = ["BUMP"]
find_BUMP_2 = ["BUMP_2"]
X = ["green_X", "gray_X"]

open_bust = (940, 800)
bust_activate = [(940, 720), (940, 950)]
cords_to_drag__for_BUMP = (940, 300)
colors_daily = [(36, 143, 72)]
# colors_get_daily = [(53, 170, 93), (29, 119, 60), (50, 200, 99)]

daily_reward__1 = [(200, 800), (400, 800), (580, 800), (750, 800), (950, 800), (1100, 800)]
daily_reward__2_3 = [(970, 500),
                     (200, 800), (400, 800), (580, 800), (750, 800), (950, 800), (1100, 800)]
daily_reward__4 = [(970, 400),
                  (200, 650), (400, 650), (580, 650), (750, 650), (950, 650), (1100, 650),
                  (900, 840)]

from typing import Optional, List, Tuple
import pyautogui as pg
import cv2
import numpy as np
from PIL import ImageGrab
import time


def multi_image_hunter(image_names: List[str], region: Tuple[int, int, int, int] = (0, 0, 1920, 1080),
                       threshold: float = 0.92, template_path: Optional[str] = "Images/") -> None:
    """
    Поиск всех шаблонов в указанной области экрана и клики по ним, с удалением уже найденных изображений из списка.

    :param image_names: Список изображений-шаблонов для поиска.
    :param region: Регион экрана в формате (x1, y1, x2, y2).
    :param threshold: Порог совпадения для поиска шаблонов (от 0 до 1).
    :param template_path: Путь к директории с изображениями.
    """
    remaining_images = image_names.copy()  # Копируем список для обработки
    while remaining_images:  # Пока есть изображения для поиска
        found_any = False  # Флаг, если хоть одно изображение найдено
        for image_name in remaining_images[:]:  # Проходим по оставшимся изображениям
            matches = find_all_templates_in_region(image_name, region, threshold, template_path)
            if matches:
                found_any = True  # Помечаем, что хотя бы одно изображение было найдено
                for (x, y, width, height) in matches:
                    time.sleep(0.2)  # Добавляем задержку между кликами
                    pg.click(x + width / 2, y + height / 2)
                remaining_images.remove(image_name)  # Удаляем изображение из списка после успешного клика
        if not found_any:
            break  # Если не найдено ни одного изображения, выходим из цикла


def find_all_templates_in_region(template_name: str, region: Tuple[int, int, int, int] = (0, 0, 1920, 1080),
                                 threshold: float = 0.92, template_path: Optional[str] = "Images/") -> Optional[
    List[Tuple[int, int, int, int]]]:
    """
    Поиск всех совпадений шаблона в указанной области экрана.

    :param template_name: Название изображения-шаблона.
    :param region: Регион экрана (x1, y1, x2, y2).
    :param threshold: Порог совпадения для поиска шаблона (от 0 до 1).
    :param template_path: Путь к изображению-шаблону.
    :return: Список координат верхнего левого угла и размеров найденных совпадений.
    """
    template_full_path = f"{template_path}{template_name}.png"

    (x1, y1, x2, y2) = region
    screenshot = np.array(ImageGrab.grab(bbox=(x1, y1, x2, y2)))  # Захват региона экрана
    template = cv2.imread(template_full_path, cv2.IMREAD_GRAYSCALE)

    if template is None:
        raise FileNotFoundError(f"Template image not found: {template_full_path}")

    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)  # Преобразуем скриншот в grayscale

    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)

    if len(loc[0]) == 0:
        return None

    matches = []
    template_height, template_width = template.shape
    for pt in zip(*loc[::-1]):
        top_left = (pt[0] + x1, pt[1] + y1)
        matches.append((top_left[0], top_left[1], template_width, template_height))

    return matches
