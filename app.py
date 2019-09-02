from constants import TEAMS, PLAYERS


def generate_list_no_experience(old_list_players):
    return [player for player in old_list_players if player["experience"] == "NO"]


def generate_list_experience(old_list_players):
    return [player for player in old_list_players if player["experience"] == "YES"]


def return_dictionary_from_lst(old_list):
    return {team: list() for team in old_list}


def print_menu(**kwargs):
    for menu, lines in kwargs.items():
        if menu == 'menu_title':
            print("")
            print(lines)
            print(len(lines) * '-')
        elif menu == 'menu_options':
            for index, option in enumerate(lines, 1):
                print("{}- {}".format(index, option))


def print_players_per_team(team, players_per_team):
    for player in players_per_team[team]:
        print(player)


def check_user_input(input, good_options):
    if input is str and input in good_options:
        return True
    else:
        raise ValueError


def print_players(team, team_players):
    inexperienced_players = [player for player in team_players if player['experience'] == 'YES']
    experienced_players = [player for player in team_players if player['experience'] == 'NO']
    lst_team_height = [int(player['height'].split(' ')[0]) for player in team_players ]
    average_team_height = round(sum(lst_team_height) / len(lst_team_height), 2)
    lst_player_name = [player['name'] for player in team_players]

    lst_player_guardians = []
    for player in team_players:
        for guardian in player['guardians']:
            lst_player_guardians.append(guardian)

    title = "Team: {} Stats".format(team)
    print("")
    print(title)
    print(len(title) * "-")
    print("Total players: {}".format(len(team_players)))
    print("Total players with NO experience: {}".format(len(inexperienced_players)))
    print("Total players with experience: {}".format(len(experienced_players)))
    print("Team height average: {}".format(average_team_height))
    print("Team guardians: {}".format(', '.join(set(lst_player_guardians))))
    print("Players on the team: {}".format((', '.join(lst_player_name))))
    print("")


def assign_players_to_teams(main_collection, players):
    while players:
        for team in main_collection.keys():
            main_collection[team].append(players.pop())
    return main_collection


def split_guardians(main_collection):
    for players in main_collection.values():
        for player in players:
            lst_guardians = player["guardians"].split(" and ")
            player["guardians"] = lst_guardians
    return main_collection


def app_start():
    # New list with experienced players from constant files
    lst_players_exp = generate_list_experience(PLAYERS)
    # New list with non experienced players from constant files
    lst_players_no_exp = generate_list_no_experience(PLAYERS)
    # Generate main collection - I'll use a dictionary with Teams as keys and a list of players as value
    dct_teams = return_dictionary_from_lst(TEAMS)
    # Assign experienced players to teams in a round-robin fashion
    dct_teams = assign_players_to_teams(dct_teams, lst_players_exp)
    # Assign non experienced players to teams in a round robin fashion
    dct_teams = assign_players_to_teams(dct_teams, lst_players_no_exp)
    # Split guardians into list
    dct_teams = split_guardians(dct_teams)
    # Begin of user menu
    while True:
        print_menu(menu_title="BASKETBALL TEAM STATS TOOL MENU", menu_options=["Display Team Stats", "Quit"])
        print("")
        user_input = input("Your choice: ")
        if user_input == "1":

            while True:
                print_menu(menu_title="STATS MENU", menu_options=dct_teams.keys())
                print("Press 'x' if you want to exit menu.\n")
                user_input_team = input("Your choice: ")
                if user_input_team == '1':
                    print_players('Panthers', dct_teams["Panthers"])
                    input("Press any key to continue.")
                elif user_input_team == '2':
                    print_players('Bandits', dct_teams["Bandits"])
                    input("Press any key to continue.")
                elif user_input_team == '3':
                    print_players('Warriors', dct_teams["Warriors"])
                    input("Press any key to continue.")
                elif user_input_team == 'x':
                    break
                else:
                    print('Invalid option. Please try again.')
                    input("Press any key to continue.")
                    continue

        elif user_input == "2":
            quit()
        else:
            print('Invalid option. Please try again.')
            input("Press any key to continue.")
            continue


if __name__ == "__main__":
    app_start()
