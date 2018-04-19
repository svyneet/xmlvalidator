import pandas as pd
import math
import sys

args = sys.argv
file = sys.argv[1]   
print(file)

#file ='raw_data//G003_Flight_0001_side.tra'

def validateDataFormat(file):
    try:
        pd.read_table(file)
    except Exception as ex:
        print("The data format is not valid\n")
        print(ex)
        sys.exit(0)
        
#validateDataFormat(file)

def validateMissingData(file):
    data = pd.read_table(file,sep='\s+',header=None) 
    for index, row in data.iterrows():
        for x in range(0, len(row)):
            if(row[x] in (None, "") or math.isnan(row[x])):
                print("Missing value is in the following row: \n" + str(row))

#validateMissingData(file)

def validateDataType(file):
    data = pd.read_table(file,sep='\s+',header=None) 
    for index,row in data.iterrows():
        for x in range(0, len(row)):
            try:
                float(row[x])
            except ValueError:
                print ("Not a numeric data:\n"+ str(row))
           
            
#validateDataType(file)


#verification with target result (exact value)
def validateDuplicateData(file):
    data = pd.read_table(file,sep='\s+',header=None) 
    duplicate =data.duplicated(subset=[1,2,3,4,5], keep=False)
    for index,row in duplicate.iteritems():
        if(row == True):
            print(index,row)
    
validateDuplicateData(file)

def validateDataInRange(file):
    data = pd.read_table(file,sep='\s+',header=None) 
    col_one_min,   col_one_max     = 0, 2048
    col_two_min,   col_two_max     = 0, 2048
    col_three_min, col_three_max   = -1.59, 1.59
    col_four_min,  col_four_max    = 0, 1786
    col_five_min,  col_five_max    = 0.00, 1.00

    col1 = []
    col2 = []
    col3 = []
    col4 = []
    col5 = []
    count = 0

    for index, row in data.iterrows():
        col1.append(row[1])
        col2.append(row[2])
        col3.append(row[3])
        col4.append(row[4])
        col5.append(row[5])
        count = index
       
    for i in range(0, count) :
        #Boundary value check
        if( not ( col1[i]>= float(col_one_min) and (col1[i] <= float(col_one_max)))):
            print("The computed result: "+str(col1[i])+" at: "+ str(i)+" do not match with the expected range of values: ("+str(col_one_min)+", "+str(col_one_max)+")")
        if( not ( col2[i]>= float(col_two_min) and (col2[i] <= float(col_two_max)))):
            print("The computed result: "+str(col2[i])+" at: "+ str(i)+" do not match with the expected range of values: ("+str(col_two_min)+", "+str(col_two_max)+")")
        if( not ( col3[i]>= float(col_three_min) and (col3[i] <= float(col_three_max)))):
            print("The computed result: "+str(col3[i])+" at: "+ str(i)+" do not match with the expected range of values: ("+str(col_three_min)+", "+str(col_three_max)+")")
        if( not ( col4[i]>= float(col_four_min) and (col4[i] <= float(col_four_max)))):
            print("The computed result: "+str(col4[i])+" at: "+ str(i)+" do not match with the expected range of values: ("+str(col_four_min)+", "+str(col_four_max)+")")
        if( not ( col5[i]>= float(col_five_min) and (col5[i] <= float(col_five_max)))):
            print("The computed result: "+str(col5[i])+" at: "+ str(i)+" do not match with the expected range of values: ("+str(col_five_min)+", "+str(col_five_max)+")")
        i = i + 1

#validateDataInRange(file)
