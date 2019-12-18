from lxml import html, etree
from ics import Calendar, Event
from StringIO import StringIO
from django.utils.encoding import smart_str, smart_unicode
from pyquery import PyQuery as pq
import requests
import MySQLdb


##### The JQuery for "The Ultimate Fighter" Posters is:

#mw-content-text > table:nth-child(52) > tbody > tr:nth-child(2) > td
def month_converter(month):
    return{
        'Jan' : '01',
        'Feb' : '02',
        'Mar' : '03',
        'Apr' : '04',
        'May' : '05',
        'Jun' : '06',
        'Jul' : '07',
        'Aug' : '08',
        'Sep' : '09', 
        'Oct' : '10',
        'Nov' : '11',
        'Dec' : '12'
}[month]

def day_converter(day):

        if day == 1 : newday = '01'
        elif day == 2 : newday = '02'
        elif day == 3 : newday = '03'
        elif day == 4 : newday =  '04'
        elif day == 5 : newday =  '05'
        elif day == 6 : newday =  '06'
        elif day == 7 : newday = '07'
        elif day == 8 : newday = '08'
        elif day == 9 : newday =  '09'
        else : newday = day

        return newday;


def createEvents (event_day, event_fight_card_url, event_location, event_month, event_name, event_org, event_year):
    print '+++++++++++++++++++++++++++++'
    e = Event()
    e.name = event_name

    newMonth = month_converter(event_month)
    newDay = day_converter(event_day)
    
    print newMonth , '  <---- this is my month value'
    print newDay , '  <---- this is my day value'
    
    
    e.begin = "%s-%s-%s 19:00"%(event_year , newMonth , newDay)
    e.end = "%s-%s-%s 23:59"%(event_year , newMonth , newDay)
    e.url = event_fight_card_url
    e.location = event_location


    MMACalendar.events.add(e)
    print MMACalendar.events
    return;

# Database Connection
db = MySQLdb.connect(host="markpereira.com", # your host, usually localhost
                     user="mark5463_ft_test", # your username
                      passwd="fttesting", # your password
                      db="mark5463_ft_testdb") # name of the data base

# Cursor object. It will let you execute the queries
cur = db.cursor()

# This section will delete the information on the table, for a clean run.


# This section will query the database and return all data in the table
cur.execute("SELECT event_day, event_fight_card_url, event_id, event_location, event_month, event_name, event_org, event_year FROM mma_events")

# initialize the arrays
event_day = []
event_fight_card_url = []
event_id = []
event_location = []
event_month = []
event_name = []
event_org = []
event_year = []


MMACalendar = Calendar()



#fight poster specific arrays
#fight_card_poster = []
fight_card_poster_url = []

# load our arrays with all of our event data.
for row in cur.fetchall() :
    event_day.append(row[0])
    event_fight_card_url.append(row[1])
    event_id.append(row[2])
    event_location.append(row[3])
    event_month.append(row[4])
    event_name.append(row[5])
    event_org.append(row[6])
    event_year.append(row[7])


x_range = len(event_name)

# This loops for every entry of event in the database to build our fight card information
for x in range(0, x_range):  # prev 0, 533
  #bring in the url information

  createEvents(event_day[x], event_fight_card_url[x], event_location[x], event_month[x], event_name[x], event_org[x], event_year[x])

  #time.sleep(5)

with open('all_events.ics', 'w') as f:
    f.writelines(MMACalendar)

'''
# Scrape UFC Information
# initialize our arrays. our Arrays.

# event_month = []
# event_day = []
# event_year = []
# event_location = []

# event_location= []
prev_row_ptr = 0
array_pos = 0

print "*********************************************"
print "List of UFC Events Wikipedia Page URL Scrape..."
print "*********************************************"
# set the event organization to UFC
event_org = 'UFC'
# set the event url to sherdog ufc section
event_url = 'https://en.wikipedia.org/wiki/UFC_1'
#reset the event id
event_id = 0

poster_url = loadPosterData(event_url, event_org)
print " ---- Inserts ----"
print "------------------"
insertRows(poster_url)


'''
