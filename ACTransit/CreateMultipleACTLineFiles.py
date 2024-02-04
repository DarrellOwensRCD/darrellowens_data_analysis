'''
Takes a list of AC Transit lines and shapes and makes individual files for them all.
'''
import json
import csv
def main():
    check = 0
    #CSV
    filename2 = '/Users/darrell/Desktop/ACTProject/Fall19/ACTLinesFa19.csv'
    fp = open(filename2, encoding = "ISO-8859-1")
    fileLines = csv.reader(fp, delimiter=',')
    Lines = list(fileLines)
    for line in Lines:
        #Get the data from the main geojson line data
        with open("/Users/darrell/Desktop/ACTProject/Fall19/ACTBoardingsFa19.geojson", 'r') as org:
            main_data = json.load(org)
            org.close()
            #open a blank geojson
            with open("/Users/darrell/Downloads/map(2).geojson", 'r') as d:
                    starter = json.load(d)
            for feat in main_data['features']:
                name = line[0].split(" ", 1)[0]
                if(feat['properties']["route_name"] == name and feat['properties']["day"] == 'Saturday'):
                    #Append the proper line sections of it into the blank instance
                    check = 1
                    starter['features'].append(feat)
            if(check):
                #Create a line file
                line_file = "/Users/darrell/Desktop/ACTProject/Fall19/Saturday/" + name + "-fa19.geojson"
                #Dump appended line data into line file and close, start OVER
                with open(line_file, 'w') as f:
                    json.dump(starter, f)
                    f.close()
            check = 0
            d.close()
    print("DONE")
