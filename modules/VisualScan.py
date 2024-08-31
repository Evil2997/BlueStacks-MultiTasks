import pytesseract
from PIL import Image
import mss
import pyautogui as pg

from modules.tesseract import setup_tesseract

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
            coordinates[text] = (x_center, y_center)
    return coordinates

def scan_and_find_coordinates(region=(0, 0, 1920, 1080), lang='rus'):
    img = capture_screen(region)
    data = extract_text_and_cords(img, lang)
    target_phrases = ["ИИ", "Офис", "Команда", "Персональные", "Майнинг"]
    return find_text_coordinates(data, target_phrases)

rus = 'rus'
eng = 'eng'
setup_tesseract()

region = (0, 0, 1920, 1080)
coordinates = scan_and_find_coordinates(region, lang=rus)

print("Coordinates of target phrases:\n", coordinates)

def VisualScanTracker():
    for phrase, (x, y) in coordinates.items():
        print(f"Moving to {phrase} at coordinates: ({x}, {y})")
        pg.moveTo(x, y)

VisualScanTracker()
