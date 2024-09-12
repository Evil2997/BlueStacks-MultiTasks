from applications import *
from applications.ElonMusk import *
from modules.VisualScan import visual_scan_tracker
from modules.get_image_colors import color_spectrum_scanner
from modules.moves import Close_AnyWay
from modules.screens import click_on_big_range_of_colors, click_in_center_on_region_by_color


def Run_ElonMusk(dailik, event, win_main):
    find_ElonMusk = find_ElonMusk_2 if win_main else find_ElonMusk_1

    PreRun(find_ElonMusk, win_main)

    pg.click(Musk_take)
    delay()

    pg.press('num4')
    delay(12, 15)
    pg.press('num4')
    delay(0.2, 0.4)

    for coordinate in Elon_daily:
        pg.click(coordinate)
        delay(2, 3)
    make_upgrades()
    pg.doubleClick(mining)
    delay(0.6, 1)

    pg.press('num4')
    delay(12, 15)
    pg.press('num4')
    delay(0.2, 0.4)

    pg.click(Elon_daily[0])
    delay()
    for _ in range(4):
        find_it_and_click_it(get_reward)
        drag_to_bottom(duration=0.25)
        delay(0.2, 0.5)
    Close_AnyWay()


def make_upgrades():
    """
    Функция проходит по всем вкладкам и прокликивает улучшения (монетки с желтым текстом).
    """
    dominant_colors = color_spectrum_scanner(template_image=yellow_text, num_colors=40)

    for _ in range(5):
        pg.click(open_upgrades)
        delay(0.2, 0.5)
        pg.click(close_upgrade)
        delay(0.2, 0.5)
        pg.click(open_upgrades)

        for navigation_target in navigation_tabs:
            drags_numeric = 6 if navigation_target == "Майнинг" else 10

            if target_coordinates := visual_scan_tracker(target_phrase=navigation_target):
                pg.click(target_coordinates)

                for _ in range(drags_numeric):
                    click_on_big_range_of_colors(
                        target_colors=dominant_colors,
                        region=(1040, 320, 1370, 930),
                        pixel_threshold=300,
                        tolerance=10,
                        min_samples=160,
                        eps=10
                    )
                    click_in_center_on_region_by_color(color_lvl_up)
                    drag_to_bottom()
                    delay(0.2, 0.5)
    delay()
