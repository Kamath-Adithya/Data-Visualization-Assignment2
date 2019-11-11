# 450 Data Vizualization

import csv
import pandas as pd
import os

class fxdpt:
    def __init__(self, duration, screenx, screeny):
        self.duration = duration
        self.screenx = screenx
        self.screeny = screeny

def main():
    # Create a file for a person.


    participantList1 = []
    participantList2 = []
    gg = []
    eg = []
    gt = []
    et = []
    gg.append(["num","percentage"])
    eg.append(["num","percentage"])
    gt.append(["num","percentage"])
    et.append(["num","percentage"])
    i = 1
    while(i < 37):
        if i == 9: i = 11
        if i == 29: i=31
        participantList1.append("p" + str(i))
        i += 2
        
    i = 2
    while(i<38):
        if i == 8: i = 10
        if i == 22: i = 24
        if i == 26: i = 28
        participantList2.append("p"+str(i))
        i+=2
    
    #genreal tree
    num=0
    vis = 0
    total = 0
    percent = 0
    for participant in participantList1:
        num+=1
        vis = 0
        total = 0
        data = pd.read_csv(participant+"/"+participant+".treeFXD.csv",na_values = ['no_info','.'])
        for i in range (len(data)):
            if data['screen_y'][i]>400:
                vis+=data['duration'][i]
            total +=data['duration'][i]
        if(vis==0 or total==0):
            percent=0
        else:
            percent = vis/total
        gt.append([num,percent])
        

    
    #expert graph
    num=0
    vis = 0
    total = 0
    percent = 0
    for participant in participantList1:
        num+=1
        data = pd.read_csv(participant+"/"+participant+".graphFXD.csv",na_values = ['no_info','.'])
        for i in range (len(data)):
            if data['screen_y'][i]>400:
                vis+=data['duration'][i]
            total +=data['duration'][i]
        percent = vis/total
        eg.append([num,percent])
        vis = 0
        total = 0
        
    
    #expert tree
    num=0
    vis = 0
    total = 0
    percent = 0
    for participant in participantList2:
        num+=1

        data = pd.read_csv(participant+"/"+participant+".treeFXD.csv",na_values = ['no_info','.'])
        for i in range (len(data)):
            if data['screen_y'][i]>400:
                vis+=data['duration'][i]
            total +=data['duration'][i]
        percent = vis/total
        et.append([num,percent])
        vis = 0
        total = 0
        percent = 0
        
    
    #general graph
    num=0
    vis = 0
    total = 0
    percent = 0
    for participant in participantList2:
        num+=1
        data = pd.read_csv(participant+"/"+participant+".graphFXD.csv",na_values = ['no_info','.'])
        for i in range (len(data)):
            if data['screen_y'][i]>400:
                vis+=data['duration'][i]
            total +=data['duration'][i]
        percent = vis/total
        gg.append([num,percent])
        vis = 0
        total = 0
        percent = 0
    
    writecsv(gg,"gg")
    writecsv(eg,"eg")
    writecsv(et,"et")
    writecsv(gt,"gt")
    
            
def writecsv(dataList,name):
    with open(r"C:\Users\Xinyi\Desktop\450\assignment2\csvData\\"+name+".csv", 'w') as f:
        writer=csv.writer(f)
        for item in dataList:
            writer.writerow(item)
    print("done")
            
main()