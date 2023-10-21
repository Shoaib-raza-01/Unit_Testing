"""CSV to read file MATPLOTLIB to plot graph"""
import csv
import matplotlib.pyplot as plt
import math


def plot(data):
    names = list(data.keys())
    plt.figure(figsize=(12,6))
    economy = [data[bowler]['economy'] for bowler in names]
    plt.bar(names, economy)
    plt.xlabel("Bowlers")
    plt.ylabel("Economy Rate")
   
    plt.xticks(rotation=90)
    plt.title("Top 10 Economic Bowlers of the Season 2015-16")
    plt.tight_layout()
    plt.savefig("../images/plot4.png")



def execute():
    match_id_for_2015 = []

    with open('../Dataset/mock_matches.csv', 'r', encoding="utf-8") as file:
        matches = csv.DictReader(file)
        for _match in matches:
            match_id = _match.get('id')
            season = _match.get('season')        
            if season == '2015' and match_id not in match_id_for_2015:
                match_id_for_2015.append(match_id)

    total_run_deliveries = {}

    with open('../Dataset/mock_deliveries.csv', 'r') as file:
        deliveries = csv.DictReader(file)

        for delivery in deliveries:
            match_id = delivery.get('match_id')
            bowler = delivery.get('bowler')
            total_run = delivery.get('total_runs')
            
            if match_id in match_id_for_2015:
                if bowler not in total_run_deliveries:
                    total_run_deliveries[bowler] = {'total': 0, 'over': 0}
                total_run_deliveries[bowler]['total'] += int(total_run)
                total_run_deliveries[bowler]['over'] += 1

    # Calculate the economy for each bowler
    for bowler in total_run_deliveries:
        try:
            runs = total_run_deliveries[bowler]['total']
            overs = total_run_deliveries[bowler]['over']
            economy = runs / overs
            total_run_deliveries[bowler]['economy'] = round(economy, 2)
        except ZeroDivisionError:
            total_run_deliveries[bowler]['economy'] = 0.0


    # print(total_run_deliveries)
    plot(total_run_deliveries)
    return total_run_deliveries

    

# print(match_id_for_2015)



execute()