def experience_to_bool(experience_str):
    return experience_str.lower() == 'yes'


def height_to_int(height_str):
    return int(height_str.split(' ')[0])


def guardians_to_list(guardians_str):
    return guardians_str.split(' and ')


def clean_player_info(name, experience, height, guardians):
    return {
        'name': name,
        'experience': experience_to_bool(experience),
        'height': height_to_int(height),
        'guardians': guardians_to_list(guardians)
    }


def clean_data(data):
    return [clean_player_info(**obj) for obj in data]


def sort_by_experience(obj):
    return obj['experience']


def balance_teams(players, teams):
    players.sort(key=sort_by_experience)
    balanced_teams = {}
    while len(players):
        for team in teams:
            player = players.pop(0)
            if team not in balanced_teams:
                balanced_teams[team] = [player]
            else:
                balanced_teams[team].append(player)

    return balanced_teams


def get_team_stats(players):
    player_names = []
    guardian_names = []
    total_players = len(players)
    total_experienced = 0
    total_height = 0

    for player in players:
        player_names.append(player['name'])
        guardian_names.append(', '.join(player['guardians']))

        if player['experience']:
            total_experienced += 1

        total_height += player['height']

    return {
        'player_names': player_names,
        'guardian_names': guardian_names,
        'total_players': total_players,
        'total_experienced': total_experienced,
        'average_height': total_height / total_players
    }
