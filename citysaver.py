import csv
from sys import argv

# CitySaVer !

# 14 Jun 2025

NUMBER_OF_TRIPS = 40
CITYSAVER_FARE = 460.0

excluded_station_ids = [
    43, 54, 55, # TCL & DRL
    67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 78, #EAL
    96, 97, 98, 99, 100, 101, 102, 103, #MOL
    115, 116, 117, 118, 119, 120, #WRL
    90 #HIK
]
usage = """Usage:
        citysaver.py <station_id> (trips starting from the station id)
        citysaver.py 0 (all trips showing where the source has lower station id)
        """
print("CitySaVer! Listing the trips where using the MTR City Saver actually saves.")

if len(argv) != 2:
    print("Argument count incorrect.")
    print(usage)
    quit()

if not argv[1].isdigit():
    print("Needs to be digits")
    print(usage)
    quit()

if int(argv[1]) in excluded_station_ids:
    print("This station is excluded...")
    quit()

mtr_lines_fares = "../Downloads/mtr_lines_fares.csv" # substitute with the location of the file
with open(mtr_lines_fares, newline='') as csvfile:
    farereader = csv.DictReader(csvfile)
    for row in farereader:
        if int(row["SRC_STATION_ID"]) in excluded_station_ids:
            continue

        if int(row["DEST_STATION_ID"]) in excluded_station_ids:
            continue

        if int(argv[1]) > 0 and int(row["SRC_STATION_ID"]) != int(argv[1]):
            continue

        if int(argv[1]) == 0 and int(row["SRC_STATION_ID"]) >= int(row["DEST_STATION_ID"]):
            continue

        saved_by_citysaver = float(row["OCT_ADT_FARE"]) - CITYSAVER_FARE / NUMBER_OF_TRIPS
        
        if saved_by_citysaver >= 0:
            print(f"From {row['SRC_STATION_NAME']} to {row['DEST_STATION_NAME']} saved {saved_by_citysaver}")