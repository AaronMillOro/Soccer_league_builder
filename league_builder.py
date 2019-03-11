"""
Python Web Development Techdegree
Project 2 - Build Soccer league
--------------------------------
"""
import csv
import os
import random

FILE = 'soccer_players.csv'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# main program
def league_builder():

# reads CSV file and and stores information in a list of dictionaries
    with open(FILE) as csvfile:
        players = csv.DictReader(csvfile, delimiter = ',')
        all_players = list(players)

    print('-' * 35 + '\n' + 'There are {} players on the list'.format(len(all_players)) + '\n' + '-' * 35)

# Creates a list of players with and without experience
    experienced_players = [player['Name'] for player in all_players if player['Soccer Experience'] == 'YES']
    normal_players = [player['Name'] for player in all_players if player['Soccer Experience'] != 'YES']


# Divides the number players into 3 teams: Sharks, Dragons and Raptors.
# Set as variable in case of eventual changes in list of players
    nb_exp_players = int(len(experienced_players) / 3 )
    nb_normal_players = int(len(all_players) / 3) - (nb_exp_players)

    teams = ['Sharks', 'Dragons', 'Raptors']
    roster = {} # final roster dictionary

    for team in range(len(teams)):
        team_name = str(teams[team]) # Set team's name for iterator
        group = []
# First selects experienced players randomly and extracts the names from list "experienced_players"
        for count in range(nb_exp_players):
            bin_experienced = random.sample(experienced_players,1)
            selected = bin_experienced.pop()
            group.append(selected)
            experienced_players = list(set(experienced_players) - set(group))

# Selects non-experienced players randomly and extracts the names from list "normal_players"
        for count in range(nb_normal_players):
            bin_normal = random.sample(normal_players,1)
            selected_norm = bin_normal.pop()
            group.append(selected_norm)
            normal_players = list(set(normal_players) - set(group))
        roster[team_name] = group

# Creates a text file of the rosters
    with open('teams.txt', 'w') as outputfile:
        writer = csv.writer(outputfile, delimiter = ',', lineterminator='\n')

# Read the roaster dictionary
        for key, players in roster.items():
            outputfile.write('-' * 10)  # write export plain text
            outputfile.write('\nThe team {} is composed by: \n\n'.format(key))

# For a given player in the roster it will look for data in the first list of dictionaries 'all_players'
            for player in players:
                for dictionary in all_players:
                    if player == dictionary.get('Name'):
                        
                        data = [player, dictionary.get('Soccer Experience'), dictionary.get('Guardian Name(s)')]
                        writer.writerow(data)
    print('The file -- teams.txt -- was generated !')
    return

if __name__ == '__main__':
    # Start the program 'league_builder'
    clear_screen()
    league_builder()
