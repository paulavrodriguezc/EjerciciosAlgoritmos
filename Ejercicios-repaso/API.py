import requests
import json
import random
from Teams import Teams
def greet_and_menu():
    print("Welcome to the World Cup 2022 DB!")
    option=input("What would you like to do? \n1. Look for a group or team and its information \n2. See a match and its results \n3. See statistics \n4. Exit \n---> ")
    while not option.isnumeric() or not option in ["1","2","3","4"]:
        option=input("Invalid input. What would you like to do? \n1. Look for a group or team and its information \n2. See a match and its results \n3. See statistics \n4. Exit \n---> ")  
    return int(option)
def search_function(teams: list, groups: set, countries: list):
    option=input("Would you like to search for a group or a team? \n1. Group \n2. Team \n---> ")
    while not option.isnumeric() or not option in ["1","2"]:
        option=input("Invalid input. Would you like to search for a group or a team? \n1. Group \n2. Team \n---> ")
    if int(option)==1:
        group=input("Please enter the group you would like to look for: ")
        while not group.isalpha() or not group.capitalize() in groups: 
           group=input("Invalid input. Please enter the group you would like to look for: ")
        print(f"Group {group.capitalize()}: ")
        for team in teams:
            if team.group==group.capitalize():
                print(f"\tTeam: {team.name} \n\tFifa Code: {team.fifa_code} \n\tID: {team.id} \n\tMatches played: {team.matches_played} \n\tAccumulated points: {team.points}\n")
    else:
        team_searched=input("Please enter the name of the team you would like to look for: ")
        while not team_searched.title() in countries: 
           team_searched=input("Invalid input. Please enter the name of the team you would like to look for: ")
        for team in teams:
            if team.name==team_searched.title():
                print(f"\nTeam: {team.name} \nFifa Code: {team.fifa_code} \nGroup: {team.group} \nID: {team.id} \nMatches played: {team.matches_played} \nAccumulated points: {team.points}\n")
def match_display(teams: list, countries: list, matches: int, ties: int):
    matches+=1
    possibilities=["Tie"]
    team_1=input("Please enter the name of the first team: ")
    team_2=input("Please enter the name of the second team: ")
    while not team_1.title() in countries or not team_2.title() in countries:
        if not team_1.title() in countries:
            team_1=input("Invalid input. Please enter the name of the first team: ")
        else:
            team_2=input("Invalid input. Please enter the name of the second team: ")
    possibilities.append(team_1.title())
    possibilities.append(team_2.title())
    for team in teams:
            if team.name==team_1.title():
                team.matches_played+=1
            elif team.name==team_2.title():
                team.matches_played+=1
    result=random.choice(possibilities)
    if result!="Tie":
        print(f"{result} has won the match!")
        for team in teams:
            if team.name==result:
                team.points+=3
    else:
        ties+=1
        for team in teams:
            if team.name==team_1.title():
                team.points+=1
            elif team.name==team_2.title():
                team.points+=1
        print("The match ended up in a tie.")
    return matches, ties
def winner_per_group(teams: list, group: str):
    max_group=0
    winner_group=""
    for team in teams:
        if team.group==group:
            if team.points>max_group:
                max_group=team.points
                winner_group=team.name
    return winner_group, max_group
def main():
    continuing=True
    teams=[]
    groups=[]
    countries=[]
    matches=0
    ties=0
    response=requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json")
    data_base=response.json()
    for country in data_base:
            team=Teams(country["name"],country["fifa_code"],country["group"],country["id"])
            teams.append(team)
            groups.append(team.group)
            countries.append(team.name)
    groups=set(groups)
    while continuing:
        option=greet_and_menu()
        if option==1:
            search_function(teams, groups, countries)
        elif option==2:
            matches,ties=match_display(teams, countries, matches, ties)
        elif option==3:
            archive=open("Statistics WC","a")
            archive.write("\n***END OF THE DAY***\n")
            archive.close()
            max_points=0
            winner=""
            max_games=0
            most_played=""
            for group in groups:
                winner_group,max_group=winner_per_group(teams, group)
                if max_group!=0:
                    print(f"In group {group}, the team with most points is {winner_group} with {max_group} points.")
                    archive=open("Statistics WC","a")
                    archive.write(f"In group {group}, the team with most points is {winner_group} with {max_group} points.\n")
                    archive.close()
            for team in teams:
                if team.points>max_points:
                    max_points=team.points
                    winner=team.name
                if team.matches_played>max_games:
                    max_games=team.matches_played
                    most_played=team.name
            print(f"The team with most points overall is {winner} with {max_points} points.")
            if matches!=0:
                print(f"The average of ties is {ties/matches}.")
            print(f"The team with most games played is {most_played} with {max_games} matches.")
            archive=open("Statistics WC","a")
            archive.write(f"The team with most points is {winner} with {max_points}. \nThe average of ties is {ties/matches}. \nThe team that has played the most is {most_played} with {max_games} played.")
            archive.close()
        else:
            print("Thank you for preferring us, have a nice day!")
            continuing=False
main()