import pyautogui as pg

from modules.screens import find_it_and_click_it
from modules.time import delay

cords_to_drag = (1650, 230)
cords_to_start_drag = (1650, 830)
cords_close = (116, 132)

close_anyway = "close_anyway"




def drag_to_up():
    delay(0.06, 0.12)
    pg.moveTo(cords_to_drag, duration=0.1)
    pg.drag(0, 500, 0.6)


def drag_to_bottom():
    delay(0.04, 0.08)
    pg.moveTo(cords_to_start_drag, duration=0.06)
    pg.dragTo(cords_to_drag, duration=0.12)


def Close_AnyWay():
    delay()
    pg.click(cords_close)
    delay(0.4, 0.6)
    find_it_and_click_it(close_anyway)
    delay(0.4, 0.6)
