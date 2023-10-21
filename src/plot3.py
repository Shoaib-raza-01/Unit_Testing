"""Importing the required module"""
import csv
import matplotlib.pyplot as plt

def plot(data):
    """Plot the graph"""
    plt.figure(figsize=(12,10))
    plt.bar(data.keys(),data.values())
    plt.xlabel("Teams")
    plt.ylabel("Extra Runs")
    plt.title("Team wise extra runs 2016")
    plt.xticks(rotation = 90)
    plt.tight_layout()
    plt.savefig('../images/plot3.png')

def execute():
    """make the datastructure as required"""
    # extra_runs_2016 ={}
    match_id_2016 =[]
    with open("../Dataset/mock_matches.csv", 'r', encoding="utf-8") as file:
        matches = csv.DictReader(file)
        for _match in matches:
            match_id = _match.get('id')
            season = _match.get('season')
            if season == '2016' and match_id not in match_id_2016:
                match_id_2016.append(match_id)
    team_and_extra_run_2016 ={}
    with open('../Dataset/mock_deliveries.csv', 'r', encoding='utf-8') as file:
        deliveries = csv.DictReader(file)
        for delivery in deliveries:
            match_id = delivery.get('match_id')
            batting_team = delivery.get('batting_team')
            extras = delivery.get('extra_runs')
            if match_id in match_id_2016:
                if batting_team not in team_and_extra_run_2016:
                    team_and_extra_run_2016[batting_team] = int(extras)
                else:
                    team_and_extra_run_2016[batting_team] += int(extras)
    plot(team_and_extra_run_2016)
    return team_and_extra_run_2016
execute()
