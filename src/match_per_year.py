import csv
import matplotlib.pyplot as plt

def plot(generated_data):
    plt.bar(generated_data.keys(), generated_data.values())
    plt.xlabel('Year')
    plt.ylabel('Number of Matches')
    plt.title('Matches by Year')
    plt.tight_layout()
    # plt.xticks(generated_data.keys(), rotation= 0)

    plt.savefig('../images/plot1.png')

def execute():
    match_year_count = {}
    with open('../Dataset/mock_matches.csv', 'r') as matches:
        reader = csv.DictReader(matches)
        
        # next(reader)
        for row in reader:
            season = int(row.get('season'))
            if season not in match_year_count:
                match_year_count[season] = 1
            else:
                match_year_count[season] += 1
    # print(match_year_count)
    # plot(match_year_count)
    return match_year_count
    
    

execute()