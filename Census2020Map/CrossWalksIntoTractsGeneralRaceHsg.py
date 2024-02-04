# Crosswalk File: General Census data version
import json
import csv
import statistics
import os.path
from os import path


def zerodiv(a, b):
    if b > 0:
        return round((a / b) * 100, 1)
    return 0


filegeo = '/Users/darrell/Desktop/Census2020/Census2020Householder/householder/CA2020CensusNetChange.geojson'
file2010 = '/Users/darrell/Desktop/Census2020/Census2010Blockgroup/nhgis0055_ds172_2010_blck_grp.csv'
filecw = '/Users/darrell/Desktop/Census2020/Census2010Blockgroup/nhgis_bg2010_tr2020_06.csv'
with open(filecw) as a, open(file2010) as b:
    cw = list(csv.reader(a, delimiter=','))
    d10 = list(csv.reader(b, delimiter=','))
    a.close()
    b.close()
c = open(filegeo)
tracts = json.load(c)
c.close()
# STEP 1 : iterate through crosswalk file blockgroups, find and multiply
# weight x data
for cross_row in cw:
    for row in d10:
        if cross_row[0] == row[0]:
            weight = float(cross_row[4])
            weightH = float(cross_row[8])
            cross_row[10] = float(row[39]) * weight  # Total Pop
            cross_row[11] = float(row[41]) * weight  # White
            cross_row[12] = float(row[42]) * weight  # Black
            cross_row[13] = float(row[43]) * weight  # Native
            cross_row[14] = float(row[44]) * weight  # Asian
            cross_row[15] = float(row[45]) * weight  # PI
            cross_row[16] = float(row[46]) * weight  # Other
            cross_row[17] = float(row[47]) * weight  # Multi
            cross_row[18] = float(row[48]) * weight  # Latino
            cross_row[19] = float(row[56]) * weightH  # Units
            cross_row[20] = float(row[58]) * weightH  # Vacant
for tract in tracts['features']:  # for each tract iterate thru rows
    first = True
    for cross_row in cw:
        if tract['properties']['GISJOIN'] == cross_row[2]:
            if first:
                first = False
                pop = float(cross_row[10])
                white = float(cross_row[11])
                black = float(cross_row[12])
                native = float(cross_row[13])
                asian = float(cross_row[14])
                pac = float(cross_row[15])
                other = float(cross_row[16])
                multi = float(cross_row[17])
                latino = float(cross_row[18])
                units = float(cross_row[19])
                vac = float(cross_row[20])
            else:
                pop += float(cross_row[10])
                white += float(cross_row[11])
                black += float(cross_row[12])
                native += float(cross_row[13])
                asian += float(cross_row[14])
                pac += float(cross_row[15])
                other += float(cross_row[16])
                multi += float(cross_row[17])
                latino += float(cross_row[18])
                units += float(cross_row[19])
                vac += float(cross_row[20])
        # when you're finished, set each value to Net Househlds = 2020 data - Net Households
        # check if first flag was triggered, if so, this was a valid iteration
        # of a tract
    if not first:
        tract['properties']['PopulationNet'] = round(
            tract['properties']['Population'] - pop)
        tract['properties']['WhiteNet'] = round(
            tract['properties']['White'] - white)
        tract['properties']['BlackNet'] = round(
            tract['properties']['Black'] - black)
        tract['properties']['Native AmericanNet'] = round(
            tract['properties']['Native American'] - native)
        tract['properties']['AsianNet'] = round(
            tract['properties']['Asian'] - asian)
        tract['properties']['Pacific IslanderNet'] = round(
            tract['properties']['Pacific Islander'] - pac)
        tract['properties']['OtherNet'] = round(
            tract['properties']['Other'] - other)
        tract['properties']['Multi-RaceNet'] = round(
            tract['properties']['Multi-Race'] - multi)
        tract['properties']['LatinoNet'] = round(
            tract['properties']['Latino'] - latino)
        tract['properties']['HomesNet'] = round(
            tract['properties']['Homes'] - units)
        tract['properties']['VacantNet'] = round(
            tract['properties']['Vacant'] - vac)
        # Calculate Percentage
        tract['properties']['PopulationNetPer'] = zerodiv(
            tract['properties']['PopulationNet'], pop)
        tract['properties']['WhiteNetPer'] = zerodiv(
            tract['properties']['WhiteNet'], white)
        tract['properties']['BlackNetPer'] = zerodiv(
            tract['properties']['BlackNet'], black)
        tract['properties']['Native AmericanNetPer'] = zerodiv(
            tract['properties']['Native AmericanNet'], native)
        tract['properties']['AsianNetPer'] = zerodiv(
            tract['properties']['AsianNet'], asian)
        tract['properties']['Pacific IslanderNetPer'] = zerodiv(
            tract['properties']['Pacific IslanderNet'], pac)
        tract['properties']['OtherNetPer'] = zerodiv(
            tract['properties']['OtherNet'], other)
        tract['properties']['Multi-RaceNetPer'] = zerodiv(
            tract['properties']['Multi-RaceNet'], multi)
        tract['properties']['LatinoNetPer'] = zerodiv(
            tract['properties']['LatinoNet'], latino)
        tract['properties']['HomesNetPer'] = zerodiv(
            tract['properties']['HomesNet'], units)
        tract['properties']['VacantNetPer'] = zerodiv(
            tract['properties']['VacantNet'], vac)
# STEP 2: Iterate through Each 2020 Tract in the GEOJSON Map
# STEP 3: Find each instance of 2020 Tract and sum up values
# STEP 4: with summations finished, round and subtract from 2020 data
# STEP 5: Insert calculations into map
# FINAL: ADD LATINOS
with open(filegeo, 'w') as c:
    json.dump(tracts, c)
    c.close()
