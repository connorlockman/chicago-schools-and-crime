**FINAL PROJECT**

-By Connor Lockman


This is a visualization project.  It will allow you to access information about Chicago Public Schools and crime within the city. 

This project makes use of two data souces. Ultimatley, the program plots where each elementary / middle school is located within the city and plots all reported homicides that have occurred across the city over the year 2018.  The goal of this project is to help visualize the proximity of Chicago's youth to crime that occurs across the city.  The plot.ly map also contains information about the schools "ranking" assigned by the Chicago Public Schools District.  

**Data Sources**
1) A large XLS file that is in the repo title "Accountability_SQRPratings_2018-2019_SchoolLevel.xls".  It contains information about every Chicago Public School within the city.
2) The program will access an api and request information about every crime within the city for 2018 (Over 200,000 instances) and will cache this information in "2018crime.csv". (https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2/data)

**Running This Program**
In order to effectively run this program, you will need to fork and clone this repo. You can run the program via the command line / terminal by running the project.py file.  You can do the same for the test.py file.  Before you can run the project you will need to input your credentials (see getting started section below) in the secrets.py file.

*command examples*
cd to the directory you have the repo saved and type in / run:
python project.py 

python tests.py

*Note: This program may take a few minutes to run the first time, as it needs to access / cache a large amount of data. Patience is a troublesome virtue*


This image shows what the program will look like broadly when you run it.  It should automatically open in your default browser after you run the project.py file.
![What is this](outputsample.png)

This image shows a zoomed in example of what the map will display.  The locations of homicides are plotted in light red and the locations of schools in dark blue.  If you hover your mouse over the school plots, it will show you the name of the school along with its CPS ranking.  The ranking criteria is as follow:

4.0 + = Level 1 + School, The highest ranking a school can get


3.5 - 3.9 = Level 1 School


3.0 - 3.4 = Level 2 + School, School needs to improve


2.0 - 2.9 = Level 2 School, School needs to improve quickly


< 2.0 = Level 3 School, Lowest ranking a school can have, at risk of being closed

![What is this](outputsample2.png)

**Getting Started**
You will need to set up a google places api (info about this can be found here: https://developers.google.com/places/web-service/intro) and a plot.ly account (info found here: https://plot.ly/python/getting-started/).  

You will take your unique credentials and input them in the secrets.py folder of the repo.

I've included my own credentials for the rest api that requests the crime information from the city of chicago.  Here is the api documentation if you'd like to look at it. https://dev.socrata.com/foundry/data.cityofchicago.org/6zsd-86xi

Info about socrata can be found here https://dev.socrata.com



**Dependencies**
You will need to install the following libraries to make this program work.
(Nothing too crazy)
1) sodapy
2) plotly 
3) Requests
4) urllib
5) pandas
6) numpy
7) matplotlib 
8) xlrd
9) csv

Info about sodapy can be found here: https://pypi.org/project/sodapy/




*You should install these libraries following your own Operating Systems instructions. For me, I used pip install on macOS.  Useful information is available in the documentation for each library about how to install these libraries for your own specific technology*


**Requirements I've Fullfilled**

*Level 1 Requirements*

Two Data sources: One is an xls file downloaded from internet (I believe it is more than sufficiently complicated), the other is a rest api.

Caching is used for the google places lon and lat (schoolcache.json) leveraging the alternate advanced caching file given to us in class. 
The rest api will make the call to download the info and save it in a file (2018crime.csv) and then will check if that file exists anytime the program is run after that.

The key pieces of info used from the schoolcache are school name and school rating. I also have school reading score and math score saved in lists, I want to include those at a later dat.

The key pieces of info from 2018crime.csv are the type of crime and where it occurred.  I only use homicides from this past year, while all crime from 2018 is in the file.  I would like to plot other types of crime in the future. 

I use many modules aside json,random, and requests as evident in the dependencies.

I do have a test suite with more than 2 test classes developed for this project in tests.py

This project produces a data visualization after running.

This project does make use of two classes (which ultimately will be more beneficial in the future).  

Class School_Information allows me to easily identify schools with their ranking in my plot.ly maps.  Hopefully I will plot high schools and include more information in the future which should all flow through this class.

Class Crime_Info does the same but for the crime data.  It is the way I parsed through the data for homicide locations and then use to link with plot.ly.  I look to plot other types of crime and other years of crimes through this class in the future.

My readme shows examples of the output and they are also available as pngs in the repo (outputsample.png and outputsample2.png)

I do believe errors are handled as well as they can be, you just run the project.py file so there isn't much user centered command.

*Level 2 Requirements*

I use a REST API socrata to acquire the data about crimes in chicago.  I've left my credentials in the api.py file so that you won't need to sign up for an account.

I use Pandas in this project, which is something we never really covered in class.  I use it to interact with the csv file containing all the crime info and to parse it for what I need (homicide incidents).

I wanted to put all this data into a postgres database but ultimately didn't have time to do so.  


*Level 3 Requirements*

This project produces a plot.ly data visualization through running the project.py file.

**Acknowledgments**

The alternate_advanced_caching.py file in this directory was provided to me in class and is not authored by me.

Other aspects of this code rely on the concepts / projects / examples that were covered over the course of si 508.


**Files Contained in this Repo Explained**

project.py  How the program runs

api.py  How the program requests info about crimes

2018crime.csv  Empty csv that is filled with crime info and serves as cache

alternate_advanced_caching  used to cache the google api requests

school_cache.json  File that holds the school locations returned from google api

secrets.py  The file you need to bput google apikey and plotly credentials in to run program

tests.py   A set of tests that determine if key parts of the program are working




