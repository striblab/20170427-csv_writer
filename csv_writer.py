import csv

# open source data
with open('thefile.csv', 'rb') as f:
  data = list(csv.reader(f))

# breakdown source file into rows
import collections
counter = collections.defaultdict(int)
for row in data:
    counter[row[0]] += 1

# write rows to new csv
writer = csv.writer(open("/path/to/my/csv/file", 'w'))
for row in data:
    if counter[row[0]] >= 4:
        writer.writerow(row)