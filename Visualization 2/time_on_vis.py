# 450 Data Vizualization

# vis: 1 = tree, 2= graph  Ont 1=general 2=expert

# Open aditional information file
# Put the stuff into a list
# we already have 4 different lists for the files
# if the fi

import csv

def main():
    # Create a file for a person.
    participantList1 = []
    participantList2 = []
    gg = []
    eg = []
    gt = []
    et = []

    # Append the column names
    gg.append(["participant","percentage_fixation", "score"])
    eg.append(["participant","percentage_fixation", "score"])
    gt.append(["participant","percentage_fixation", "score"])
    et.append(["participant","percentage_fixation", "score"])

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

    print(participantList1) # did general tree and expert graph
    print(participantList2) # did general graph and expert tree

    # in gt append 1, 1
    # in gg append 2, 1
    # in et append 1, 2
    # in eg append 2, 2

    calc_percent(participantList1, ".treeFXD.csv", gt)
    calc_percent(participantList1, ".graphFXD.csv", eg)
    calc_percent(participantList2, ".treeFXD.csv", et)
    calc_percent(participantList2, ".graphFXD.csv", gg)
    
    writecsv(gg,"gg")
    writecsv(eg,"eg")
    writecsv(et,"et")
    writecsv(gt,"gt")

# in FXD data [number, time, duration, x, y]
def calc_percent(participant_list, file_ending, output_file):
    file_path = r'C:\Users\Steven\Documents\School\Fall 2019\Data Viz\Project 2\clean_FXD_Data\\'
    for participant in participant_list:
        vis = 0
        total = 0
        percent = 0
        with open(file_path + participant + "\\" + participant + file_ending, mode='r', newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter = ',')
            next(reader)
            for row in reader:
                if int(row[4])>400:
                    vis+=int(row[2])
                total +=int(row[2])
        percent = vis/total
        output_file.append([participant,percent])


def writecsv(dataList,name):
    with open(r"C:\Users\Steven\Documents\School\Fall 2019\Data Viz\Project 2\Percent_Time\\"+name+".csv", mode='w', newline='') as f:
        writer=csv.writer(f)
        for item in dataList:
            writer.writerow(item)
    print("done")
            
main()