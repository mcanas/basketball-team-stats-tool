import constants
from utils import data
from utils import menu


def start(players_by_team):
    print('BASKETBALL TEAM STATS TOOL')

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
            player_names, guardian_names, total_players, total_experienced, average_height = data.get_team_stats(
                players_by_team[choice]).values()
            print(f'\n---- Team {choice} Stats ----\n')
            print(f'Total players: {total_players}\n')
            print(f'Experienced players: {total_experienced}\n')
            print(f'Average height: {average_height}\n')
            print(f'Players on team:\n\t{", ".join(player_names)}\n')
            print(f'Guardians:\n\t{", ".join(guardian_names)}\n')


start(data.balance_teams(data.clean_data(constants.PLAYERS), constants.TEAMS))
