import json
import csv

def json_to_csv(json_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    csv_file_path = json_file_path[:-5] + '.csv'
    
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)

        header = []
        for key in data[0].keys():
            header.append(key)
        writer.writerow(header)

        for item in data:
            row = []
            for key in header:
                row.append(item[key])
            writer.writerow(row)

    print(f'JSON file converted to CSV: {csv_file_path}')
