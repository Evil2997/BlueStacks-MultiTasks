import numpy as np
from PIL import ImageGrab as scr
from pytesseract import pytesseract

from modules import config_numbers_0to9__add_slash_point
from modules.screens import get_image_size, find_template_in_region


def found_text_on_image(region=(0, 0, 1920, 1080), lang='eng'):
    screenshot = np.array(scr.grab(bbox=region))
    text = pytesseract.image_to_string(screenshot, config=config_numbers_0to9__add_slash_point, lang=lang)
    return text


def fff(name, region=(0, 0, 1920, 1080), threshold=0.92, lang='eng'):
    top_left = find_template_in_region(template_name=name, region=region, threshold=threshold)
    width, height = get_image_size(name)
    if top_left:
        region_image_founded = (top_left[0], top_left[1], top_left[0] + width, top_left[1] + height)
        text = found_text_on_image(region_image_founded, lang=lang)
        print(text)
