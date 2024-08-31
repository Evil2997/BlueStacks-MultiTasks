import mss
import pyautogui as pg
import pytesseract
from PIL import Image


def capture_screen(region=(0, 0, 1920, 1080)):
    with mss.mss() as sct:
        screenshot = sct.grab(region) if region else sct.grab(sct.monitors[1])
        img = Image.frombytes('RGB', screenshot.size, screenshot.rgb)
        return img


def extract_text_and_cords(image, lang='rus'):
    custom_config = r'--oem 3 --psm 6'
    data = pytesseract.image_to_data(image, lang=lang, config=custom_config, output_type=pytesseract.Output.DICT)
    return data


def find_text_coordinates(data, target_phrases):
    coordinates = {}
    for i in range(len(data['text'])):
        text = data['text'][i].strip()
        if text in target_phrases:
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            x_center, y_center = x + w // 2, y + h // 2
            if text not in coordinates:
                coordinates[text] = []
            coordinates[text].append((x_center, y_center))
    return coordinates


def scan_and_find_coordinates(region=(0, 0, 1920, 1080), lang='rus', target_phrases=None):
    img = capture_screen(region)
    data = extract_text_and_cords(img, lang)
    return find_text_coordinates(data, target_phrases)


def VisualScanTracker(region=(0, 0, 1920, 1080), lang='rus', target_phrases=None):
    coordinates = scan_and_find_coordinates(region=region, lang=lang, target_phrases=target_phrases)
    for phrase, cords in coordinates.items():
        for idx, (x, y) in enumerate(cords):
            print(f"Moving to {phrase} [{idx}] at coordinates: ({x}, {y})")
            pg.moveTo(x, y)
