"""Importing the modules required"""
import csv
import matplotlib.pyplot as plt

def plot(generated_data):
    """Ploting the graph"""
    plt.bar(generated_data.keys(), generated_data.values())
    plt.xlabel('Year')
    plt.ylabel('Number of Matches')
    plt.title('Matches by Year')
    plt.tight_layout()
    plt.savefig('../images/plot1.png')

def execute():
    """Executing the function to generate data to plot it"""
    match_year_count = {}
    with open('../Dataset/mock_matches.csv', 'r', encoding='utf-8') as matches:
        reader = csv.DictReader(matches)
        for row in reader:
            season = int(row.get('season'))
            if season not in match_year_count:
                match_year_count[season] = 1
            else:
                match_year_count[season] += 1
    plot(match_year_count)
    return match_year_count
execute()
