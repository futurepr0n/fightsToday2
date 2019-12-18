from lxml import html, etree
from StringIO import StringIO
from django.utils.encoding import smart_str, smart_unicode
from pyquery import PyQuery as pq
import re
import requests


import MySQLdb

def loadData (event_url, event_org):
    #set up the lxml, load url to scrape
    page = requests.get('%s'%(event_url))
    tree = html.fromstring(page.content)

    #set up PyQuery section, load the url to scrape
    d = pq("<html></html>")
    d = pq(etree.fromstring("<html></html>"))
    d = pq(url='%s'%(event_url))

    #get the row length by querying the event table on table rows
    #p = d(".event tr")
    p = d("#upcoming_tab tr")
    #set the row length
    row_len = len(p)

    #run through every row in the table
    for x in range (2, row_len+1):
      # scrape ufc event name
      event_name_array = tree.xpath('//*[@id="upcoming_tab"]/table/tr[%i]/td[2]/a/span/text()'%(x))
      # event_parse = re.sub('[-.]', '', event_name_array)
      event_name.append(event_name_array)
      # scrape event month
      event_month_array = tree.xpath('//*[@id="upcoming_tab"]/table/tr[%i]/td[1]/span/span[1]/text()'%(x))
      event_month.append(event_month_array)
      # scrape event day
      event_day_array = tree.xpath('//*[@id="upcoming_tab"]/table/tr[%i]/td[1]/span/span[2]/text()'%(x))
      event_day.append(event_day_array)
      # scrape event year
      event_year_array = tree.xpath('//*[@id="upcoming_tab"]/table/tr[%i]/td[1]/span/span[3]/text()'%(x))
      event_year.append(event_year_array)
      # scrape event fight card URL
      event_fight_card_url_array = tree.xpath('//*[@id="upcoming_tab"]/table/tr[%i]/td[2]/a/@href'%(x))
      ev_fc_wbst = 'http://www.sherdog.com', ''.join(event_fight_card_url_array)
      event_fight_card_url.append(ev_fc_wbst)
      event_location_array = tree.xpath('//*[@id="upcoming_tab"]/table/tr[%i]/td[3]/text()'%(x))
      newstr = ''.join(event_location_array)
      asccii_string = smart_str(newstr)
      event_location.append(asccii_string)
    return row_len;


def insertRows (row_len, total_event, prev_row_ptr, array_pos):
    # set the array position
    array_pos = array_pos + prev_row_ptr
    event_id = total_event - 1

    # loop through all the rows
    for loopid in range (0,row_len-1):
      # set the event id


      print '+++++++++++++++++++++++++++++'
      db_e_en = ''.join(event_name[array_pos])
      db_e_ev = ''.join(event_month[array_pos])
      db_e_ed = ''.join((event_day[array_pos]))
      db_e_ey = ''.join((event_year[array_pos]))
      db_e_fc = ''.join(event_fight_card_url[array_pos])
      db_e_lc = ''.join(event_location[array_pos])
      print 'Adding event: ', event_id ,' +++ ', db_e_en,' +++ ', db_e_ev,' +++ ', db_e_ed, ' +++ ', db_e_ey,' +++ ', db_e_fc, ' +++ ', db_e_lc
      print '+++++++++++++++++++++++++++++'
      print '+++++++++++++++++++++++++++++'
      query = "INSERT INTO mma_events (event_name, event_month, event_day, event_year, event_id, event_fight_card_url, event_org, event_location) VALUES (\"%s\",\'%s\',%s,%s,%i,\"%s\",\"%s\",\"%s\")"%(db_e_en, db_e_ev, db_e_ed, db_e_ey, event_id, db_e_fc, event_org, db_e_lc)
      print query
      # commenting out the query since we are loaded in the db right now
      cur.execute(query)

      # Calender stuff
      

      array_pos = (array_pos) + 1
      event_id = event_id - 1
    prev_row_ptr = prev_row_ptr + row_len

    return;

# Database Connection
db = MySQLdb.connect(host="markpereira.com",user="mark5463_ft_test",passwd="fttesting", db="mark5463_ft_testdb")

# Cursor object. It will let you execute the queries
cur = db.cursor()

# This section will delete the information on the table, for a clean run.
#print "clear the table"
#cur.execute("TRUNCATE mma_events")

# Scrape UFC Information
# initialize our arrays. our Arrays.
event_name = []
event_month = []
event_day = []
event_year = []
event_location = []
event_fight_card_url = []
event_location= []
prev_row_ptr = 0
array_pos = 0

ufc_total_events = 0
bellator_total_events = 0


####################################

print "*********************************************"
print "Bellator Upcoming Section Scrape Page 1..."
print "*********************************************"
# set the event organization to UFC
event_org = 'Bellator'
# set the event url to sherdog ufc section
# event_url = 'http://www.sherdog.com/organizations/Ultimate-Fighting-Championship-2'
event_url = 'https://www.sherdog.com/organizations/Bellator-1960/upcoming-events/1'
#reset the event id
# event_id = 0

ufc_row_len = loadData(event_url, event_org)
ufc_total_events = ufc_total_events + ufc_row_len
print " ---- Inserts ----"
# insertRows(ufc_row_len, prev_row_ptr, array_pos)
insertRows(ufc_row_len, ufc_total_events, prev_row_ptr, array_pos)

#set the prev_row_ptrgth pointer
prev_row_ptr = ufc_row_len + prev_row_ptr - 1

#####################################




