
# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

###################################
### IMPORT STATEMENTS 
import csv
from secrets import *

import pandas as pd
from sodapy import Socrata
###################################


###################################
### CHICAGO REST API REQUEST CREDENTIALS
client = Socrata("data.cityofchicago.org",
                 "7eHdl1TLWcWcYuR9yDa3hHSNK",
                 username="lockman@umich.edu",
                 password="Password!")


#####################################



#####################################
### ORIGINAL CALL TO API RETURNS ALL CRIME (6 + million)
#result_list = client.get("6zsd-86xi",limit=250000)
#results_df = pd.DataFrame.from_records(result_list)
#print(results_df)


#print(result_list)
#lon = result_list(longitude)

#results_df.to_csv('2018crime.csv')

#results_df.to_csv('2001crime.csv')
######################################


#####################################
### USING CRIME LON LAT (SET OF 250000 crimes since 2001)

#with open('2001crime.csv','r') as f:
#	crime_lon_lat = csv.DictReader(f)
#	line_count = 0
	#crime_lon_lat = crime_lon_lat[13]
	#print(crime_lon_lat)
	#for i in crime_lon_lat:
	#	print([i[0]])

#print(dict(crime_lon_lat))
######################################



######################################
### IMPLEMENTING CACHE FOR 2018 CRIME CSV

def crime_look_up(year):
    
    #print(list_crimedata)
    
    with open('2018crime.csv','r') as f:
        crime_lon_lat = csv.DictReader(f)
        line_count = 0
        #crime_lon_lat = crime_lon_lat[13]
        list_crimedata = list(crime_lon_lat)
        #print(list_crimedata)
        #print(len(list_crimedata))

        if len(list_crimedata) is 0:
            #print("needs to cache")
            results_list = client.get("6zsd-86xi","?year=2018",limit=500000)
            results_df = pd.DataFrame.from_records(results_list)
            results_df.to_csv('2018crime.csv')

            with open('2018crime.csv','r') as f:
                crime_lon_lat = csv.DictReader(f)
                line_count = 0
                #crime_lon_lat = crime_lon_lat[13]
                list_crimedata = list(crime_lon_lat)



        else: 
            #print('doesnt')
            list_crimedata = list_crimedata



    #print(list_crimedata)
    return list_crimedata


list_crimedata = crime_look_up("2018")


######################################



######################################
### ORIGINAL OPEN OF CSV
#with open('2018crime.csv','r') as f:
#	crime_lon_lat = csv.DictReader(f)
#	line_count = 0
	#crime_lon_lat = crime_lon_lat[13]
#	list_crimedata = list(crime_lon_lat)

#new_crime_data = list_crimedata
######################################

new_crime_data = list_crimedata

######################################
### 2018 Homicides
#homicide_data = []
#for i in new_crime_data:
#	if i['primary_type'] == 'HOMICIDE':
#		homicide_data += [i]


#homicide_location = []
#for i in homicide_data:
#	lon = i["longitude"]
#	lat = i["latitude"]
#	homicide_location += [(lon,lat)]

#######################################


########################################
### CLASS THAT RETURNS 2018 HOMICIDE INFO
class crime_info():
    
    def __init__(self,list_crimedata):
        self.list_crimedata = list_crimedata



    def get_location(self):
        homicide_data = []
        for i in self.list_crimedata:
            if i['primary_type'] == 'HOMICIDE':
                homicide_data += [i]

        homicide_location = []

        homicide_location = []
        for i in homicide_data:
            lon = i["longitude"]
            lat = i["latitude"]
            homicide_location += [(lon,lat)]


        return homicide_location

##########################################


##########################################
### Requesting Info

sample_crime = crime_info(list_crimedata)
crime_info_lst = sample_crime.get_location()
#print(crime_info_lst)
homicide_crime_locations = crime_info_lst


###########################################
