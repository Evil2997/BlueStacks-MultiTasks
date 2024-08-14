from applications import *
from applications.DejenDog import *
from modules.moves import Close_AnyWay


def Run_DejenDog(dailik):
    PreRun(find_DejenDog, chat=True, chat_type="image", chat_image_name=ChatDog)
    drag_to_bottom(duration=0.4)
    for _ in range(3):
        pg.press("num3")  # ON
        delay(16, 24)
        pg.press("num3")  # OFF
        delay(4, 6)
    for coordinates in dog_lvlup_menu:
        pg.click(coordinates)
        delay(8, 9)
    Close_AnyWay()
