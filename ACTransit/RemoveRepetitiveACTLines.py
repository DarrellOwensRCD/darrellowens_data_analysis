import json
import csv
import statistics
def main():
    filename2 = '/Users/darrell/Desktop/ACTProject/Fall19/Stop_Summary_Daily_Totals_Fall_2019.csv'
    fp = open(filename2, encoding = "ISO-8859-1")
    fileLines = csv.reader(fp, delimiter=',')
    Lines = list(fileLines)
    #START
    with open("ACTLinesFa19.csv", "w", encoding = "ISO-8859-1", newline = '') as f:
        writer = csv.writer(f)
        for line in Lines:
            if(line[0] != "ROUTE_NAME"):
                if(line[0] != save):
                    row = [line[0],]
                    writer.writerow(row)
            save = line[0]
