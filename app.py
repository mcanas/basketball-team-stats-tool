import constants
from utils import data
from utils import menu


def start():
    print('BASKETBALL TEAM STATS TOOL')

    players_by_team = data.balance_teams(
        data.clean_data(constants.PLAYERS), constants.TEAMS)

    menu.add_menu(
        id='MAIN',
        header='Main Menu',
        options=[('Display Team Stats', 'TEAMS')],
        include_back=False,
    )

    menu.add_menu(
        id='TEAMS',
        header='Select a Team',
        options=[(team, 'STATS') for team in constants.TEAMS],
        previous_menu='MAIN'
    )

    menu.add_menu(
        id='STATS',
        header='Team Menu',
        previous_menu='TEAMS'
    )

    goto = 'MAIN'
    while True:
        choice, goto = menu.show_menu(goto)
        if goto == None:
            print('Goodbye!')
            break
        if goto == 'STATS':
            data.render_stats(choice, data.get_team_stats(
                players_by_team[choice]))
            goto = 'MAIN'


if __name__ == '__main__':
    start()
