import names
import argparse
import random
import datetime
import csv
from datetime import date

parser = argparse.ArgumentParser(description='Generate synthetic data for EatenByBear ML Problem')
parser.add_argument('--rows', type=int, required=True,
                    help='The number of data rows returned by the program')
parser.add_argument('--outfile', help='File for the results')
args = parser.parse_args()

colorOptions = ['black', 'white', 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'magenta', 'purple']
headerRow = ['name', 'age', 'birthDate', 'distanceFromZoo', 'meatObjectsWorn', 'honeyRatio', 'height', 'weight', 'combatTraining', 'hasBearSpray', 'numberofPicnicBaskets', 'runningSpeed', 'colorsWorn', 'eatenByBear']

def getRows(rows):
    payload = []
    payloadRow = []
    for _ in range(rows):
        payloadRow.append(names.get_full_name())
        payloadRow.append(random.randint(1, 99))
        payloadRow.append(date.isoformat(datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 99)*365)))
        payloadRow.append(random.randint(0, 999))
        payloadRow.append(random.randint(0, 9))
        payloadRow.append(round(random.random(), 2))
        payloadRow.append(random.randint(21, 107))
        payloadRow.append(random.randint(7, 1400))
        payloadRow.append(random.choice(['TRUE', 'FALSE']))
        payloadRow.append(random.choice(['TRUE', 'FALSE']))
        payloadRow.append(random.randint(0, 2))
        payloadRow.append(random.uniform(0.1, 8.0))
        payloadRow.append(', '.join(random.sample(colorOptions, k=3)))
        payloadRow.append(random.choice(['TRUE', 'FALSE']))
        payload.append(payloadRow)
        payloadRow = []
    return payload

if args.outfile:
    with open(args.outfile, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headerRow)
        rowPayload = getRows(args.rows)
        for row in rowPayload:
            writer.writerow(row)
else: 
    print(', '.join(headerRow))
    rowPayload = getRows(args.rows)
    for row in rowPayload:
        print(', '.join(str(s) for s in row))