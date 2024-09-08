from applications import *
from applications.ElonMusk import *
from modules.VisualScan import visual_scan_tracker
from modules.get_image_colors import color_spectrum_scanner
from modules.moves import Close_AnyWay
from modules.screens import click_on_big_range_of_colors


def Run_ElonMusk(dailik, event, win_main):
    find_ElonMusk = find_ElonMusk_2 if win_main else find_ElonMusk_1

    PreRun(find_ElonMusk, win_main)

    pg.click(Musk_take)
    delay(4, 5)
    for coordinate in Elon_daily:
        pg.click(coordinate)
        delay(4, 5)
    # make_upgrades()
    Close_AnyWay()


def make_upgrades():
    """
    Функция проходит по всем вкладкам и прокликивает улучшения (монетки с желтым текстом).
    """
    dominant_colors = color_spectrum_scanner(template_image=yellow_text, num_colors=40)

    pg.click(open_upgrades)
    delay()
    for navigation_target in navigation_tabs:
        if target_coordinates := visual_scan_tracker(target_phrase=navigation_target):
            pg.click(target_coordinates)
            for _ in range(10):
                click_on_big_range_of_colors(
                    target_colors=dominant_colors,
                    region=(1040, 320, 1370, 930),
                    pixel_threshold=300,
                    tolerance=10,
                    min_samples=100,
                    eps=10
                )
                drag_to_bottom()
                delay()
