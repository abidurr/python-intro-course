import os
os.chdir("C:\\Users\\abidu\\Downloads")

def load_data(file):
    fHandle = open(file, "r")
    fContent = fHandle.readlines()
    for i in range(len(fContent)):
        fContent[i] = fContent[i].strip().split(',')
    return(fContent)

def get_gpa_averages(file):
    lst = list(file)
    admitNo = 0
    nonAdmitNo = 0
    totalAdmit = 0
    totalNonAdmit = 0
    for i in range(1, len(lst)):
        if lst[i][0] == "1":
            admitNo += 1
            totalAdmit += float(lst[i][2])
        if lst[i][0] == "0":
            nonAdmitNo += 1
            totalNonAdmit += float(lst[i][2])
    gpaAdmitAvg = totalAdmit/admitNo
    gpaNonAdmitAvg = totalNonAdmit/nonAdmitNo
    return gpaAdmitAvg, gpaNonAdmitAvg




    

    
