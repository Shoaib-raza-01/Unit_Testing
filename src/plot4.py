"""CSV to read file MATPLOTLIB to plot graph"""
import csv
import matplotlib.pyplot as plt
import math


def plot(data):
    pass


def execute():
    match_id_for_2015 = []

    with open('../Dataset/mock_matches.csv', 'r', encoding="utf-8") as file:
        matches = csv.DictReader(file)
        for _match in matches:
            match_id = _match.get('id')
            season = _match.get('season')        
            if season == '2015' and match_id not in match_id_for_2015:
                match_id_for_2015.append(match_id)

    # print(match_id_for_2015)
    total_run_deliveries = {}
    with open('../Dataset/mock_deliveries.csv' , 'r') as file:
        deliveries = csv.DictReader(file)
        

        for delivery in deliveries:
            match_id = delivery.get('match_id')
            bowler = delivery.get('bowler')
            total_run = delivery.get('total_runs')
            
            if match_id in match_id_for_2015:
                if bowler not in total_run_deliveries:
                    total_run_deliveries[bowler] = {'total' : 0, 'over' :  0}
                else:
                    total_run_deliveries[bowler]['total'] += int(total_run)
                    total_run_deliveries[bowler]['over'] += (1/6)
        
        for bowler in total_run_deliveries:
            total_run_deliveries[bowler]['over'] = round(total_run_deliveries[bowler]['over'])
            runs = total_run_deliveries[bowler]['total']
            # overs = math.ceil(total_run_deliveries[bowler]['over'])
            # economy = runs / overs
            # total_run_deliveries[bowler]['economy'] = round(economy, 2)

        # sorted_list = sorted(total_run_deliveries.items(), key= lambda x : x[1]['economy'])

        # top_10_economical_bowler = sorted_list[:10]
        # print(top_10_economical_bowler)

        # name = []
        # economy = []
        # for i in range(len(top_10_economical_bowler)):
        #     name.append(top_10_economical_bowler[i][0])
        #     economy.append(top_10_economical_bowler[i][1]['economy'])
        # print(name, economy)



































# print(match_id_for_2015)


    # plt.bar(name, economy)
    # plt.xlabel("Bowlers")
    # plt.ylabel("Economy Rate")
    # plt.xticks(rotation=90)
    # plt.title("Top 10 Economic Bowlers of the Season 2015-16")
    # plt.savefig("../images/top_10_economical_bowler.png")

execute()