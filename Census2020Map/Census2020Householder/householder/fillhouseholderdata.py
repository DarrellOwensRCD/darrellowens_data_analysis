#Fills geojson file with racial homeowner data 2020
import json
import csv
import statistics
import os.path
from os import path

geofile = '/Users/darrell/Desktop/Census2020/Census2020Householder/householder/CA2020CensusNetChange.geojson'
datafile = '/Users/darrell/Desktop/Census2020/Census2020Householder/PHC2020/DECENNIALDHC2020.H10-Data.csv'
ldatafile = '/Users/darrell/Desktop/Census2020/Census2020Householder/PHCLatino2020/DECENNIALDHC2020.H11-Data.csv'
# Open Geofile
z = open(datafile)
line_data = csv.reader(z, delimiter=',')
rows = list(line_data)
z.close()
# Open latino Geofile
z = open(ldatafile)
H_line_data = csv.reader(z, delimiter=',')
his_rows = list(H_line_data)
z.close()
# Open Datafile
z = open(geofile)
tracts = json.load(z)
z.close()
for tract in tracts['features']:
    for row in rows:
        if tract['properties']['GEOID'] == row[0][9:]:  
            tract["properties"]["Households"] = int(row[2])
            tract["properties"]["Homeowners"] = int(row[4])#Total Homeowners
            tract["properties"]["Renters"] = int(row[20])#Total Homeowners
            tract["properties"]["WhiteHomeowners"] = int(row[6]) #WhiteHomeowners 
            tract["properties"]["BlackHomeowners"] =int(row[8]) #BlackHomeowners 
            tract["properties"]["Native AmericanHomeowners"] =int(row[10]) #Natives
            tract["properties"]["AsianHomeowners"] =int(row[12]) #AsianHomeownerss
            tract["properties"]["Pacific IslanderHomeowners"] =int(row[14]) #Pacific IslanderHomeownerss
            tract["properties"]["OtherHomeowners"] =int(row[16]) #OtherHomeownerss
            tract["properties"]["Multi-RaceHomeowners"] = int(row[18]) #MultiRace
            if(tract["properties"]["WhiteHomeowners"] > 0):
                tract["properties"]["WhiteHomeownersPer"]= round(tract["properties"]["WhiteHomeowners"] / tract["properties"]["Homeowners"] * 100,1)#WhiteHomeownerss
            else:
                tract["properties"]["WhiteHomeownersPer"] = 0
            
            if(tract["properties"]["BlackHomeowners"] > 0):
                tract["properties"]["BlackHomeownersPer"]= round(tract["properties"]["BlackHomeowners"] / tract["properties"]["Homeowners"] * 100,1)#BlackHomeowners
            else:
                tract["properties"]["BlackHomeownersPer"] = 0        
            if(tract["properties"]["Native AmericanHomeowners"] > 0):
                tract["properties"]["Native AmericanHomeownersPer"]= round(tract["properties"]["Native AmericanHomeowners"] / tract["properties"]["Homeowners"] * 100,1)#Natives
            else:
                tract["properties"]["Native AmericanHomeownersPer"] = 0
            if(tract["properties"]["AsianHomeowners"] > 0):
                tract["properties"]["AsianHomeownersPer"] = round(tract["properties"]["AsianHomeowners"] / tract["properties"]["Homeowners"] * 100,1)#AsianHomeowners
            else:
                tract["properties"]["AsianHomeownersPer"] = 0
            if(tract["properties"]["Pacific IslanderHomeowners"] > 0):
                tract["properties"]["Pacific IslanderHomeownersPer"] = round(tract["properties"]["Pacific IslanderHomeowners"] / tract["properties"]["Homeowners"] * 100,1)#OtherHomeowners
            else:
                tract["properties"]["Pacific IslanderHomeownersPer"] = 0 

            if(tract["properties"]["OtherHomeowners"] > 0):
                tract["properties"]["OtherHomeownersPer"] = round(tract["properties"]["OtherHomeowners"] / tract["properties"]["Homeowners"] * 100,1)#OtherHomeowners
            else:
                tract["properties"]["OtherHomeownersPer"] = 0
            if(tract["properties"]["Multi-RaceHomeowners"] > 0):
                tract["properties"]["Multi-RaceHomeownersPer"] = round(tract["properties"]["Multi-RaceHomeowners"] / tract["properties"]["Homeowners"] * 100,1)#Other
            else:
                tract["properties"]["Multi-RaceHomeownersPer"] = 0
            # Renters
            tract["properties"]["WhiteRenters"] = int(row[22]) #WhiteRenters 
            tract["properties"]["BlackRenters"] =int(row[24]) #BlackRenters 
            tract["properties"]["Native AmericanRenters"] =int(row[26]) #Natives
            tract["properties"]["AsianRenters"] =int(row[28]) #AsianRenterss
            tract["properties"]["Pacific IslanderRenters"] = int(row[30]) #Pacific IslanderRenterss
            tract["properties"]["OtherRenters"] =int(row[32]) #OtherRenterss
            tract["properties"]["Multi-RaceRenters"] = int(row[34])#MultiRace
            tract["properties"]["LatinoRenters"] = 0 #LatinoRenterss
            if(tract["properties"]["LatinoRenters"] > 0):
                tract["properties"]["LatinoPer"] = round(tract["properties"]["LatinoRenters"] / tract["properties"]["Renters"] * 100,1)#Latinos
            else:
                tract["properties"]["LatinoPer"] = 0
            if(tract["properties"]["WhiteRenters"] > 0):
                tract["properties"]["WhitePer"]= round(tract["properties"]["WhiteRenters"] / tract["properties"]["Renters"] * 100,1)#Whites
            else:
                tract["properties"]["WhitePer"] = 0

            if(tract["properties"]["BlackRenters"] > 0):
                tract["properties"]["BlackPer"]= round(tract["properties"]["BlackRenters"] / tract["properties"]["Renters"] * 100,1)#Black
            else:
                tract["properties"]["BlackPer"] = 0        
            if(tract["properties"]["Native AmericanRenters"] > 0):
                tract["properties"]["Native AmericanPer"]= round(tract["properties"]["Native AmericanRenters"] / tract["properties"]["Renters"] * 100,1)#Natives
            else:
                tract["properties"]["Native AmericanPer"] = 0
            if(tract["properties"]["AsianRenters"] > 0):
                tract["properties"]["AsianPer"] = round(tract["properties"]["AsianRenters"] / tract["properties"]["Renters"] * 100,1)#Asian
            else:
                tract["properties"]["AsianPer"] = 0
                
            if(tract["properties"]["OtherRenters"] > 0):
                tract["properties"]["OtherRentersPer"] = round(tract["properties"]["OtherRenters"] / tract["properties"]["Renters"] * 100,1)#Other
            else:
                tract["properties"]["OtherRentersPer"] = 0
                
            if(tract["properties"]["Pacific IslanderRenters"] > 0):
                tract["properties"]["Pacific IslanderRentersPer"] = round(tract["properties"]["Pacific IslanderRenters"] / tract["properties"]["Renters"] * 100,1)
            else:
                tract["properties"]["Pacific IslanderRentersPer"] = 0
            if(tract["properties"]["Multi-RaceRenters"] > 0):
                tract["properties"]["Multi-RaceRentersPer"] = round(tract["properties"]["Multi-RaceRenters"] / tract["properties"]["Renters"] * 100,1)#Other
            else:
                tract["properties"]["Multi-RaceRentersPer"] = 0
    # Hispanics
    for his_row in his_rows:
        if tract['properties']['GEOID'] == his_row[0][9:]: 
            tract["properties"]["LatinoHomeowners"] = int(his_row[8]) #LatinoHomeownerss
            if(tract["properties"]["LatinoHomeowners"] > 0):
                tract["properties"]["LatinoHomeownersPer"] = round(tract["properties"]["LatinoHomeowners"] / tract["properties"]["Homeowners"] * 100,1)#LatinoHomeownerss
            else:
                tract["properties"]["LatinoHomeownersPer"] = 0
            tract["properties"]["LatinoRenters"] = int(his_row[14]) #LatinoRenterss
            if(tract["properties"]["LatinoRenters"] > 0):
                tract["properties"]["LatinoPer"] = round(tract["properties"]["LatinoRenters"] / tract["properties"]["Renters"] * 100,1)#Latinos
            else:
                tract["properties"]["LatinoPer"] = 0
with open(geofile, 'w') as c:
    json.dump(tracts, c)
    c.close()
