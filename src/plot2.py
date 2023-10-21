import csv
import matplotlib.pyplot as plt

def plot(data):
    teams = set()
    years = list(data.keys())

    for year_data in data.values():
        teams.update(year_data.keys())
    team_championships = {team: [data[year].get(team, 0) for year in years] for team in teams}

    teams = sorted(teams)

    # Prepare data for the chart
    team_championships = {team: [data[year].get(team, 0) for year in years] for team in teams}

    # Create the stacked bar chart
    plt.figure(figsize=(10, 6))

    bottom = [0] * len(years)

    for team in teams:
        values = team_championships[team]
        plt.bar(years, values, label=team, bottom=bottom)
        bottom = [b + v for b, v in zip(bottom, values)]

    plt.xlabel('Year')
    plt.ylabel('number of wins')
    plt.title('IPL win count by Team')
    plt.legend(title='Teams', loc='upper left', bbox_to_anchor=(1, 1))
    plt.tight_layout()
    plt.savefig('../images/plot2.png')

def execute():
    won_per_team_year = {}
    with open('../Dataset/mock_matches.csv', 'r') as file:
        reader = csv.DictReader(file)
        # next(reader, None)  # skip the headers
        
        for row in reader:
            year = int(row.get('season'))
            winner = row.get('winner')
            if year not in won_per_team_year:
                won_per_team_year[year] = {}

            if winner not in won_per_team_year[year]:
                won_per_team_year[year][winner] = 1
            else:
                won_per_team_year[year][winner] += 1
    # print(won_per_team_year)
    plot(won_per_team_year)
    return won_per_team_year

execute()