import csv
import re

input_query = 'airpods'

csv_file_path = f'{input_query}.csv'
result_file_path = f'{input_query}(sorted).csv'

regex_pattern = re.compile(r'm19') # Find Airpods m19

with open(csv_file_path, newline='', encoding='utf-8') as csvfile, open(result_file_path, 'w', newline='', encoding='utf-8') as resultfile:
    csv_reader = csv.reader(csvfile)
    csv_writer = csv.writer(resultfile)

    header = next(csv_reader)
    csv_writer.writerow(header)

    filtered_rows = [row for row in csv_reader if regex_pattern.search(row[0])]

    sorted_rows = sorted(filtered_rows, key=lambda x: int(x[1]))

    csv_writer.writerows(sorted_rows)

print(f" result saved in : {result_file_path}")
