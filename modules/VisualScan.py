import pytesseract
from PIL import Image
import mss

from modules.tesseract import setup_tesseract


def capture_screen(region=(0, 0, 1920, 1080)):
    with mss.mss() as sct:
        screenshot = sct.grab(region) if region else sct.grab(sct.monitors[1])
        img = Image.frombytes('RGB', screenshot.size, screenshot.rgb)
        return img


def extract_text_from_image(image, lang='rus'):
    return pytesseract.image_to_string(image, lang=lang)


def scan_and_extract_text(region=(0, 0, 1920, 1080)):
    img = capture_screen(region)
    text = extract_text_from_image(img, lang=rus)
    return text


rus = 'rus'
eng = 'eng'
setup_tesseract()

region = (0, 0, 1920, 1080)  # Задайте регион экрана
extracted_text = scan_and_extract_text(region)
print("Extracted Text:\n", extracted_text)


def VisualScanTracker():
    pass
