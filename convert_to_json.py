# 450 Data Vizualization

import csv
import json
import os

def main():
    # Create a file for a person.

    filePath = r"C:\Users\Steven\Documents\School\Fall 2019\Data Viz\Project 2\jsonData"

    participantList = []

    fileEndings = [".graphEVD", ".graphFXD", ".graphGZD", 
                   ".treeEVD", ".treeFXD", ".treeGZD", "GZD"]

    # (p0, ... , p36)
    i = 26
    while(i < 37):
        if i == 8: i = 10
        if i == 22: i+=1
        if i == 26: i+=1
        if i == 29: i+=1
        participantList.append("p" + str(i))
        i += 1

    print(participantList)

    for participant in participantList:
        directory = filePath + '\\' + participant
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        for ending in fileEndings:
            csvFile = participant + ending
            createJSON(participant, csvFile)
  

def createJSON(folder, fileName):
    # Open the CSV  
    with open(r"C:\Users\Steven\Documents\School\Fall 2019\Data Viz\Project 2\Archive\\" + folder + "\\" + fileName + ".txt", 'r' ) as f: 
        reader = csv.reader(f, delimiter = '\t')  

        data = list(reader)

        
    out = json.dumps(data)   
    print("JSON parsed!")  
    # Save the JSON  
    f = open(r"C:\Users\Steven\Documents\School\Fall 2019\Data Viz\Project 2\jsonData\\" + folder + "\\"+ fileName + ".json", 'w')   
    f.write(out)  
    print("JSON saved!")  

main()