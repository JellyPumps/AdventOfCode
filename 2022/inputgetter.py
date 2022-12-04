###############################################
#from
from aocd import get_data
###############################################
#import
import datetime
###############################################
currentTime=datetime.datetime.now()
###############################################
#Get data from current days input
def getAoCInput():
    return get_data(day=currentTime.day, year=currentTime.year)
