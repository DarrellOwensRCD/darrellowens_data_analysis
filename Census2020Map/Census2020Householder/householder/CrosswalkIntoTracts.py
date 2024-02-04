import json
import csv
import statistics
import os.path
from os import path


def zerodiv(a, b):
    if b > 0:
        return round(a / b, 1)
    return 0


filegeo = '/Users/darrell/Desktop/Census2020/Census2020Householder/householder/CA2020CensusNetChange.geojson'
file2010 = '/Users/darrell/Desktop/Census2020/Census2010Householder/DECENNIALSF12010.H14_2023-06-29T024537/DECENNIALSF12010.H14-Data.csv'
file2010L = '/Users/darrell/Desktop/Census2020/Census2010Householder/DECENNIALSF12010.H15_2023-06-29T024646/DECENNIALSF12010.H15-Data.csv'
filecw = '/Users/darrell/Desktop/Census2020/Census2020Householder/householder/nhgis_bg2010_tr2020_06.csv'
with open(filecw) as a, open(file2010) as b, open(file2010L) as l:
    cw = list(csv.reader(a, delimiter=','))
    d10 = list(csv.reader(b, delimiter=','))
    d10L = list(csv.reader(l, delimiter=','))
    a.close()
    b.close()
    l.close()
c = open(filegeo)
tracts = json.load(c)
c.close()
# STEP 1 : iterate through crosswalk file blockgroups, find and multiply
# weight x data
for cross_row in cw:
    for row in d10:
        if cross_row[0] == row[0][10:]:
            weight = float(cross_row[6])
            cross_row[10] = float(row[2]) * weight  # Total Households
            cross_row[11] = float(row[4]) * weight  # Total Homeowners
            cross_row[12] = float(row[5]) * weight  # WhiteHomeowners
            cross_row[13] = float(row[6]) * weight  # BlackHomeowners
            cross_row[14] = float(row[7]) * weight  # Natives
            cross_row[15] = float(row[8]) * weight  # AsianHomeownerss
            cross_row[16] = float(row[9]) * weight  # Pacific Islander
            cross_row[17] = float(row[10]) * weight  # OtherHomeownerss
            cross_row[18] = float(row[11]) * weight  # MultiRace
            cross_row[19] = float(row[12]) * weight  # Total Renters
            cross_row[20] = float(row[13]) * weight  # WhiteHomeowners
            cross_row[21] = float(row[14]) * weight  # BlackHomeowners
            cross_row[22] = float(row[15]) * weight  # Natives
            cross_row[23] = float(row[16]) * weight  # AsianHomeownerss
            cross_row[24] = float(row[17]) * weight  # Pacific Islander
            cross_row[25] = float(row[18]) * weight  # OtherHomeownerss
            cross_row[26] = float(row[19]) * weight  # MultiRace
    for row in d10L:
        if cross_row[1] == row[0][10:]:
            cross_row[27] = float(row[6]) * weight  # Latino Hmers
            cross_row[28] = float(row[9]) * weight  # Latino Renters
for tract in tracts['features']:  # for each tract iterate thru rows
    first = True
    for cross_row in cw:
        if tract['properties']['GISJOIN'] == cross_row[2]:
            if first:
                first = False
                tract['properties']['Net Households'] = float(cross_row[10])
                tract['properties']['Net Homeowners'] = float(cross_row[11])
                tract['properties']['Net Renters'] = float(cross_row[19])
                tract['properties']['Net White Homeowners'] = float(
                    cross_row[12])
                tract['properties']['Net Black Homeowners'] = float(
                    cross_row[13])
                tract['properties']['Net Native American Homeowners'] = float(
                    cross_row[14])
                tract['properties']['Net Asian Homeowners'] = float(
                    cross_row[15])
                tract['properties']['Net Pacific Islander Homeowners'] = float(
                    cross_row[16])
                tract['properties']['Net Other Homeowners'] = float(
                    cross_row[17])
                tract['properties']['Net Multi-Race Homeowners'] = float(
                    cross_row[18])
                tract['properties']['Net White Renters'] = float(cross_row[20])
                tract['properties']['Net Black Renters'] = float(cross_row[21])
                tract['properties']['Net Native American Renters'] = float(
                    cross_row[22])
                tract['properties']['Net Asian Renters'] = float(cross_row[23])
                tract['properties']['Net Pacific Islander Renters'] = float(
                    cross_row[24])
                tract['properties']['Net Other Renters'] = float(cross_row[25])
                tract['properties']['Net Multi-Race Renters'] = float(
                    cross_row[26])
                tract['properties']['Net Latino Homeowners'] = float(
                    cross_row[27])
                tract['properties']['Net Latino Renters'] = float(
                    cross_row[28])
            else:
                tract['properties']['Net Households'] += float(cross_row[10])
                tract['properties']['Net Homeowners'] += float(cross_row[11])
                tract['properties']['Net Renters'] += float(cross_row[19])
                tract['properties']['Net White Homeowners'] += float(
                    cross_row[12])
                tract['properties']['Net Black Homeowners'] += float(
                    cross_row[13])
                tract['properties']['Net Native American Homeowners'] += float(
                    cross_row[14])
                tract['properties']['Net Asian Homeowners'] += float(
                    cross_row[15])
                tract['properties']['Net Pacific Islander Homeowners'] += float(
                    cross_row[16])
                tract['properties']['Net Other Homeowners'] += float(
                    cross_row[17])
                tract['properties']['Net Multi-Race Homeowners'] += float(
                    cross_row[18])
                tract['properties']['Net White Renters'] += float(
                    cross_row[20])
                tract['properties']['Net Black Renters'] += float(
                    cross_row[21])
                tract['properties']['Net Native American Renters'] += float(
                    cross_row[22])
                tract['properties']['Net Asian Renters'] += float(
                    cross_row[23])
                tract['properties']['Net Pacific Islander Renters'] += float(
                    cross_row[24])
                tract['properties']['Net Other Renters'] += float(
                    cross_row[25])
                tract['properties']['Net Multi-Race Renters'] += float(
                    cross_row[26])
                tract['properties']['Net Latino Homeowners'] += float(
                    cross_row[27])
                tract['properties']['Net Latino Renters'] += float(
                    cross_row[28])
        # when you're finished, set each value to Net Househlds = 2020 data - Net Households
        # check if first flag was triggered, if so, this was a valid iteration
        # of a tract
    if not first:
        tract['properties']['Net Households'] = round(
            tract["properties"]["Households"] -
            tract['properties']['Net Households'])
        tract['properties']['Net Homeowners'] = round(
            tract["properties"]["Homeowners"] -
            tract['properties']['Net Homeowners'])
        tract['properties']['Net Renters'] = round(
            tract["properties"]["Renters"] -
            tract['properties']['Net Renters'])
        tract['properties']['Net White Homeowners'] = round(
            tract["properties"]["WhiteHomeowners"] -
            tract['properties']['Net White Homeowners'])
        tract['properties']['Net Black Homeowners'] = round(
            tract["properties"]["BlackHomeowners"] -
            tract['properties']['Net Black Homeowners'])
        tract['properties']['Net Native American Homeowners'] = round(
            tract["properties"]["Native AmericanHomeowners"] -
            tract['properties']['Net Native American Homeowners'])
        tract['properties']['Net Asian Homeowners'] = round(
            tract["properties"]["AsianHomeowners"] -
            tract['properties']['Net Asian Homeowners'])
        tract['properties']['Net Pacific Islander Homeowners'] = round(
            tract["properties"]["Pacific IslanderHomeowners"] -
            tract['properties']['Net Pacific Islander Homeowners'])
        tract['properties']['Net Other Homeowners'] = round(
            tract["properties"]["OtherHomeowners"] -
            tract['properties']['Net Other Homeowners'])
        tract['properties']['Net Multi-Race Homeowners'] = round(
            tract["properties"]["Multi-RaceHomeowners"] -
            tract['properties']['Net Multi-Race Homeowners'])
        tract['properties']['Net White Renters'] = round(
            tract["properties"]["WhiteRenters"] -
            tract['properties']['Net White Renters'])
        tract['properties']['Net Black Renters'] = round(
            tract["properties"]["BlackRenters"] -
            tract['properties']['Net Black Renters'])
        tract['properties']['Net Native American Renters'] = round(
            tract["properties"]["Native AmericanRenters"] -
            tract['properties']['Net Native American Renters'])
        tract['properties']['Net Asian Renters'] = round(
            tract["properties"]["AsianRenters"] -
            tract['properties']['Net Asian Renters'])
        tract['properties']['Net Pacific Islander Renters'] = round(
            tract["properties"]["Pacific IslanderRenters"] -
            tract['properties']['Net Pacific Islander Renters'])
        tract['properties']['Net Other Renters'] = round(
            tract["properties"]["OtherRenters"] -
            tract['properties']['Net Other Renters'])
        tract['properties']['Net Multi-Race Renters'] = round(
            tract["properties"]["Multi-RaceRenters"] -
            tract['properties']['Net Multi-Race Renters'])
        tract['properties']['Net Latino Homeowners'] = round(
            tract["properties"]["LatinoHomeowners"] -
            tract['properties']['Net Latino Homeowners'])
        tract['properties']['Net Latino Renters'] = round(
            tract["properties"]["LatinoRenters"] -
            tract['properties']['Net Latino Renters'])
        # Calculate Percentage
        tract['properties']['Net Households Per'] = zerodiv(
            tract['properties']['Net Households'], tract["properties"]["Households"] - tract['properties']['Net Households'])
        tract['properties']['Net Homeowners Per'] = zerodiv(
            tract['properties']['Net Homeowners'], tract["properties"]["Homeowners"] - tract['properties']['Net Homeowners'])
        tract['properties']['Net Renters Per'] = zerodiv(
            tract['properties']['Net Renters'], tract["properties"]["Renters"] - tract['properties']['Net Renters'])
        tract['properties']['Net White Homeowners Per'] = zerodiv(
            tract['properties']['Net White Homeowners'], tract["properties"]["WhiteHomeowners"] - tract['properties']['Net White Homeowners'])
        tract['properties']['Net Black Homeowners Per'] = zerodiv(
            tract['properties']['Net Black Homeowners'], tract["properties"]["BlackHomeowners"] - tract['properties']['Net Black Homeowners'])
        tract['properties']['Net Native American Homeowners Per'] = zerodiv(
            tract['properties']['Net Native American Homeowners'], tract["properties"]["Native AmericanHomeowners"] - tract['properties']['Net Native American Homeowners'])
        tract['properties']['Net Asian Homeowners Per'] = zerodiv(
            tract['properties']['Net Asian Homeowners'], tract["properties"]["AsianHomeowners"] - tract['properties']['Net Asian Homeowners'])
        tract['properties']['Net Pacific Islander Homeowners Per'] = zerodiv(
            tract['properties']['Net Pacific Islander Homeowners'], tract["properties"]["Pacific IslanderHomeowners"] - tract['properties']['Net Pacific Islander Homeowners'])
        tract['properties']['Net Other Homeowners Per'] = zerodiv(
            tract['properties']['Net Other Homeowners'], tract["properties"]["OtherHomeowners"] - tract['properties']['Net Other Homeowners'])
        tract['properties']['Net Multi-Race Homeowners Per'] = zerodiv(
            tract['properties']['Net Multi-Race Homeowners'], tract["properties"]["Multi-RaceHomeowners"] - tract['properties']['Net Multi-Race Homeowners'])
        tract['properties']['Net White Renters Per'] = zerodiv(
            tract['properties']['Net White Renters'], tract["properties"]["WhiteRenters"] - tract['properties']['Net White Renters'])
        tract['properties']['Net Black Renters Per'] = zerodiv(
            tract['properties']['Net Black Renters'], tract["properties"]["BlackRenters"] - tract['properties']['Net Black Renters'])
        tract['properties']['Net Native American Renters Per'] = zerodiv(
            tract['properties']['Net Native American Renters'], tract["properties"]["Native AmericanRenters"] - tract['properties']['Net Native American Renters'])
        tract['properties']['Net Asian Renters Per'] = zerodiv(
            tract['properties']['Net Asian Renters'], tract["properties"]["AsianRenters"] - tract['properties']['Net Asian Renters'])
        tract['properties']['Net Pacific Islander Renters Per'] = zerodiv(
            tract['properties']['Net Pacific Islander Renters'], tract["properties"]["Pacific IslanderRenters"] - tract['properties']['Net Pacific Islander Renters'])
        tract['properties']['Net Other Renters Per'] = zerodiv(
            tract['properties']['Net Other Renters'], tract["properties"]["OtherRenters"] - tract['properties']['Net Other Renters'])
        tract['properties']['Net Multi-Race Renters Per'] = zerodiv(
            tract['properties']['Net Multi-Race Renters'], tract["properties"]["Multi-RaceRenters"] - tract['properties']['Net Multi-Race Renters'])
        tract['properties']['Net Latino Homeowners Per'] = zerodiv(
            tract['properties']['Net Latino Homeowners'], tract["properties"]["LatinoHomeowners"] - tract['properties']['Net Latino Homeowners'])
        tract['properties']['Net Latino Renters Per'] = zerodiv(
            tract['properties']['Net Latino Renters'], tract["properties"]["LatinoRenters"] - tract['properties']['Net Latino Renters'])
# STEP 2: Iterate through Each 2020 Tract in the GEOJSON Map
# STEP 3: Find each instance of 2020 Tract and sum up values
# STEP 4: with summations finished, round and subtract from 2020 data
# STEP 5: Insert calculations into map
# FINAL: ADD LATINOS
with open(filegeo, 'w') as c:
    json.dump(tracts, c)
    c.close()
