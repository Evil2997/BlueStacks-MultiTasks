import time

from applications import *
from applications.ElonMusk import *
from modules.VisualScan import visual_scan_tracker, find_coin_and_check_text, capture_full_screen_or_region, \
    extract_text_and_coordinates
from modules.get_image_colors import color_spectrum_scanner, get_rgb_bounds
from modules.moves import Close_AnyWay


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
    dominant_colors = color_spectrum_scanner(template_image=yellow_text, num_colors=10)
    lower_yellow, upper_yellow = get_rgb_bounds(dominant_colors)

    pg.click(open_upgrades)
    delay()
    for navigation_target in navigation_tabs:
        if target_coordinates := visual_scan_tracker(target_phrase=navigation_target):
            pg.click(target_coordinates)
            for _ in range(10):
                coins_centers = find_coin_and_check_text(
                    template_name=yellow_coin,
                    lower_yellow=lower_yellow,
                    upper_yellow=upper_yellow
                )
                for coin_center in coins_centers:
                    pg.click(coin_center)
                    delay()
                drag_to_bottom()
                delay(0.2, 0.4)
