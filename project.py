###########################
###IMPORT STATEMENTS / SETUP
import plotly.graph_objs as go
import urllib
import plotly
import plotly.plotly as py
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import requests
from alternate_advanced_caching import *
from secrets import *
from api import *
###########################


#########################
###SCHOOL INFORMATION

file = 'Accountability_SQRPratings_2018-2019_SchoolLevel.xls'
data = pd.ExcelFile(file)
#print(data.sheet_names)

###########################


#########################
# FIRST SETS OF SCHOOL DATA ~ NAME / RANKING
df1 = data.parse('Elem Schools (grds PreK-8 only)')

#print(df1.iloc[4:],[2])

df1_dict = pd.read_excel('Accountability_SQRPratings_2018-2019_SchoolLevel.xls',header=[0,1],sheet_name='Elem Schools (grds PreK-8 only)')

sub_df1_dict = df1_dict["SQRP SY2019 Individual Indicator Scores (Based on 2017-2018 Data)"]

school_name_lst = list(sub_df1_dict['School Name'])
school_ranking_lst = list(sub_df1_dict['SQRP Total Points Earned'])
#print(school_name_lst)

###########################
#print(school_name_lst)

###########################
# SECOND SET OF SCHOOL DATA ~ SCORES
df2 = data.parse('Elem Schools (grds PreK-8 only)')
df2_dict = pd.read_excel('Accountability_SQRPratings_2018-2019_SchoolLevel.xls',header=[0,1],sheet_name='Elem Schools (grds PreK-8 only)')
sub_df2_dict = df2_dict['NWEA MAP Growth Indicators - All Students']
reading_score = list(sub_df2_dict['National School Growth Percentile - Reading'])
#print(reading_score)

math_score = list(sub_df2_dict['National School Growth Percentile - Math'])
#print(math_score)

###########################



###########################
# SCHOOL CLASS THAT DOES WHAT ITS SUPPOSED TO

class school_information():
    
    def __init__(self,school_name_lst,school_ranking_lst,reading_score,math_score):
        self.school_name_lst = school_name_lst
        self.school_ranking_lst = school_ranking_lst
        self.reading_score = reading_score
        self.math_score = math_score

    def school_dictionary1(self):
        school_dict = zip(self.school_name_lst,self.school_ranking_lst)
        #keys = [self.school_name_lst]
        #values = [self.school_ranking_lst]
        return list(school_dict)


sample_school2 = school_information(school_name_lst,school_ranking_lst,reading_score,math_score)
school_info_lst = sample_school2.school_dictionary1()





###########################
### USING CRIME LON LAT
#with open('2001crime.csv','r') as f:
#	crime_lon_lat = f.read()
#	crime_lon_lat = crime_lon_lat[13]
	#print(crime_lon_lat)



####################################
### TEST FOR GETTING SCHOOL LON AND LAT

#test_data_request = school_name_lst[3] + " CHICAGO PUBLIC SCHOOL"
#print(test_data_request)
#test_param = {"key":google_api_key,"input":test_data_request,"inputtype":"textquery","fields":"geometry"}
#test_location = requests.get("https://maps.googleapis.com/maps/api/place/findplacefromtext/json?",test_param).text

#json_formatted= json.loads(test_location)

#lat = json_formatted["candidates"][0]["geometry"]["location"]["lat"]
#lon = json_formatted["candidates"][0]["geometry"]["location"]["lng"]
#print(lat)
#print(lon)


#struggling to get this function to cache school lon and lat up and running
####################################
school_cache = Cache("school_cache.json")

def params_unique_combination(baseurl, params_d, private_keys=["api_key"]):
    alphabetized_keys = sorted(params_d.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_keys:
            res.append("{}-{}".format(k, params_d[k]))
    return baseurl + "_".join(res)


def school_location(school_name):
    params_dict = {"key":google_api_key,"input": school_name + " CHICAGO PUBLIC SCHOOL","inputtype":"textquery","fields":"geometry"}
    #print(params_dict)
    id = params_unique_combination("https://maps.googleapis.com/maps/api/place/findplacefromtext/json?",params_dict,google_api_key)
    cached_place = school_cache.get(id)
    
    if cached_place is not None:
        get_place = cached_place
    
    else:
        get_place = requests.get("https://maps.googleapis.com/maps/api/place/findplacefromtext/json?",params=params_dict).text
        school_cache.set(id,get_place,5)

    location= json.loads(get_place)

    if location["status"] == "OK":
        lat = location["candidates"][0]["geometry"]["location"]["lat"]
        lng = location["candidates"][0]["geometry"]["location"]["lng"]
        return [lat,lng]
    return ['','']

short_school_name_lst = school_name_lst[1:11]
#print(short_school_name_lst)
#print(school_location("STAGG"))

#############################



#############################
### TEST CASES (SHORT SCHOOL LIST)
#location1 = []
#for i in short_school_name_lst:
#    lat_lon = school_location(i)
#    location1 += [lat_lon]
#location1 = [school_location("GLOBAL CITIZENSHIP"),school_location("LOCKE A")]
#print(location1)
#############################



############################
#BUILDING SCHOOL LOCATION LIST

location1 = []

for i in school_name_lst[1:]:
    lat_lon = school_location(i)
    location1 += [lat_lon]


#############################



#############################
### PLOTLY MAP 

def plot_map_locations(state_abbr):
    

    ###################
    ### TEST CASE
    #for i in short_school_name_lst:
    #    name += [i]
    ###################
    ### HOMICIDES 
    h_lat_list = []
    h_lon_list = []

    #print(homicide_location[0:9])

    #for i in homicide_location:
    #    h_lat_list += [str(i[1])]
    #    h_lon_list += [str(i[0])]

    for i in homicide_crime_locations:
        h_lat_list += [str(i[1])]
        h_lon_list += [str(i[0])]

    ###################
 


    ###################
    ### SCHOOL LOCATIONS

    name = []
    lat_list = []
    lon_list = []

    for i in school_info_lst[1:]:
        name += [i]

   # for i in school_ranking_lst[1:101]:
   #     pair = [i]
   #     ranking += [i]

    for i in location1:
        lat_list += [str(i[0])]
        lon_list += [str(i[1])]  
        #lat_list += i[0]
        #lon_list += i[1]

    #print(lat_list)
    #print(lon_list)
    ####################


    ####################
    data = [
        go.Scattermapbox(
        lat = lat_list, 
        lon = lon_list,
            mode='markers',
            marker=dict(
                size=10
            ),
            text= name,
            ),

        go.Scattermapbox(
        lat = h_lat_list, 
        lon = h_lon_list,
            mode='markers',
            marker=dict(
                size=10,
                color='rgb(242,177,172)'
            ),
            text= 'homicide',
            )
        ]


    layout = go.Layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=token,
            bearing=0,
            center=dict(
                lat =41.8,
                lon= -87.5
                ),
            pitch=0,
            zoom=10
            ),
        )
    fig = dict(data=data,layout=layout)
    py.iplot(fig,filename='plot_chicago_sites',auto_open=True)

##############################

##############################
### STARTS IT ALL

plot_map_locations("il")









