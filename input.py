import csv
from statistics import median

def read_csv(file_path):
    records = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            records.append(row)
    return records

def fill_missing_data(records):
    grouped_records = {}

    for record in records:
        country = record['country']
        daily_vaccinations = record['daily_vaccinations']

        if country not in grouped_records:
            grouped_records[country] = {'daily_vaccinations': []}
        if daily_vaccinations != '':
            daily_vaccinations = float(daily_vaccinations)
            grouped_records[country]['daily_vaccinations'].append(daily_vaccinations)

    # Fill in missing data with the median daily vaccination number of relevant countries
    for country, data in grouped_records.items():
        if data['daily_vaccinations']:
            median_daily_vaccinations = median(data['daily_vaccinations'])
        else:
            median_daily_vaccinations = float('inf')
        grouped_records[country]['median_daily_vaccinations'] = median_daily_vaccinations

    return grouped_records

if __name__ == '__main__':
    input_file = 'input.csv'
    records = read_csv(input_file)
    grouped_records = fill_missing_data(records)

    # Sort countries based on their median daily vaccination numbers
    sorted_countries = sorted(grouped_records.items(), key=lambda x: x[1]['median_daily_vaccinations'], reverse=True)

    # Print the top-3 countries with highest median daily vaccination numbers
    print("Top-3 Countries with Highest Median Daily Vaccination Numbers:")
    count = 0
    for country, data in sorted_countries:
        if count == 3:
            break
        if data['median_daily_vaccinations'] != float('inf'):
            print(f"{count+1}. {country}: {data['median_daily_vaccinations']}")
            count += 1


