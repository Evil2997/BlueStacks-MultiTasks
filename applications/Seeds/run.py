from applications import *
from applications.Seeds import *
from modules.moves import Close_AnyWay


def Run_Seeds(dailik):
    PreRun(find_Seeds)
    if dailik:
        pg.click(open_daily_Seeds)
        delay(3, 4)
        drag_to_bottom(duration=0.4, cords_to_drag=(940, 300))
        for coordinates in daily_Seeds:
            pg.click(coordinates)
            delay(0.2, 0.6)
        delay()
        pg.press("Esc")
        delay()
        pg.click(open_daily_Seeds)
        delay()
        pg.click(claim_ticket_Seeds)
        delay(3, 4)
        pg.press("Esc")
        delay()
        for coordinates in get_ticket_Seeds:
            pg.click(coordinates)
            delay(6, 8)
        pg.press("Esc")
        delay()
    for coordinates in seeds_claim:
        pg.click(coordinates)
        delay(0.4, 1)
    for _ in range(2):
        pg.click(caterpillar_claim_on_tree)
    Close_AnyWay()
