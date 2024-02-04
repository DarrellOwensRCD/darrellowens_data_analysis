'''
In order to upload shapes of the AC Transit routes, this program makes "recipes" which are
attributes and visualization files for Mapbox's Tiling Service.
'''
import json
import csv
def main():
    check = 0
    #JSON
    #CSV
    filename2 = '/Users/darrell/Desktop/ACTProject/Fall19/ACTLinesFa19.csv'
    fp = open(filename2, encoding = "ISO-8859-1")
    fileLines = csv.reader(fp, delimiter=',')
    Lines = list(fileLines)
    count = 0
    file_count = 1
    x = { "version" : 1, "layers" : {}}
    for line in Lines:
        name = line[0].split(" ", 1)[0]
        y = {name + "-line": {
          "source": "mapbox://tileset-source/idothethinking/" + name + '-week-19',
          "minzoom": 0,
          "maxzoom": 12.6
        }}
        if(count == 0):
            with open("/Users/darrell/Desktop/ACTProject/Fall19/Weekday/recipe/recipe" + str(file_count) + ".json", "w") as new:
                new.seek(0)
                json.dump(x, new, indent=4)
                
        with open("/Users/darrell/Desktop/ACTProject/Fall19/Weekday/recipe/recipe" + str(file_count) + ".json", 'r+') as file:
            f_data = json.load(file)
            f_data["layers"].update(y)
            file.seek(0)
            json.dump(f_data, file, indent=4)
        count = count +1
        if(count == 20):
            file_count = file_count + 1
            count = 0
        
