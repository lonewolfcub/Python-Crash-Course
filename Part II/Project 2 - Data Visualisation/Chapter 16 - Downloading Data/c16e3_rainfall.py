import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get dates, high and low temperatures from file.
filename = 'san_francisco_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, rainfall_level = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            rainfall = float(row[19])
        except ValueError:
            print(current_date, 'Missing Data')
        else:
            dates.append(current_date)
            rainfall_level.append(rainfall)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, rainfall_level, c='blue', alpha=0.5)


# Format plot.
title = "Daily rainfall - 2014\nSan Francisco, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rainfall (Inch)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()