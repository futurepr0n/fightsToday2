from lxml import html, etree
from StringIO import StringIO
from django.utils.encoding import smart_str, smart_unicode
from pyquery import PyQuery as pq
import requests
import MySQLdb


##### The JQuery for "The Ultimate Fighter" Posters is:

#mw-content-text > table:nth-child(52) > tbody > tr:nth-child(2) > td

def loadPosterData (event_url, x):
    #set up the lxml, load url to scrape
    page = requests.get('http://www.bellator.com/events')
    tree = html.fromstring(page.content)

    #set up PyQuery section, load the url to scrape
    d = pq("<html></html>")
    d = pq(etree.fromstring("<html></html>"))
    d = pq(url='http://www.bellator.com/events')
    print event_url
    
    poster_url_array = tree.xpath('//*[@id="t4_lc_promo1"]/div/ul/li[%s]/div[1]/a/div/img'%(x))
    print '//*[@id="t4_lc_promo1"]/div/ul/li[%s]/div[1]/a/div/img'%(x) 
    newstr = ''.join(poster_url_array)
    asccii_string = smart_str(newstr)
    print newstr, asccii_string


    poster_url_array2 = tree.xpath('//*[@id="t3_lc"]/div/div/ul/li[4]/a/div/img/@src')
    print poster_url_array2

    # //*[@id="t3_lc"]/div/div/ul/li[4]/a/div/img
    #poster_url_array = tree.xpath('//*[@id="t4_lc_promo1"]/div/ul/li[1]/div[1]/a/div/img/@src')

    # If the poster is not found, we might want to try this xpath: //*[@id="mw-content-text"]/table[5]/tr[2]/td/a/img


    #ev_fc_poster_wbst = str(poster_url_array).strip('[\'\']')
    #ev_fc_poster_wbst = str(asccii_string).strip('[\'\']')
    #newstr2 = ev_fc_poster_wbst
    #ev_fp_wbst = "http:%s"%(newstr2)
    ev_fp_wbst = "http:%s"%(newstr)

    return ev_fp_wbst;

def insertRows (poster_url, event_id, event_fight_card_url, event_date, event_name):
    print '+++++++++++++++++++++++++++++'
    db_e_poster_url = ''.join(poster_url)
    print 'Adding poster URL to the Database: ',  db_e_poster_url
    print '+++++++++++++++++++++++++++++'
    print '+++++++++++++++++++++++++++++'
    query = "INSERT INTO mma_events_wiki_poster (event_fight_poster_url, event_id, event_fight_card_url, event_date, event_name) VALUES (\"%s\",%i, \"%s\", \"%s\", \"%s\")"%(db_e_poster_url, event_id, event_fight_card_url, event_date, event_name)
    print query
    # commenting out the query since we are loaded in the db right now
    # cur.execute(query)

    return;

# Database Connection
db = MySQLdb.connect(host="markpereira.com", # your host, usually localhost
                     user="mark5463_ft_test", # your username
                      passwd="fttesting", # your password
                      db="mark5463_ft_testdb") # name of the data base

# Cursor object. It will let you execute the queries
cur = db.cursor()

# This section will delete the information on the table, for a clean run.
#cur.execute("TRUNCATE mma_events_wiki_poster ")

# This section will query the database and return all data in the table
cur.execute("SELECT event_name, event_id, event_fight_card_url, event_org, event_date FROM mma_events_wiki where event_org = \"Bellator\" ORDER BY event_id ASC")

# initialize the arrays
event_name = []
event_id = []
event_fight_card_url = []
event_org = []
event_date = []

#fight poster specific arrays
#fight_card_poster = []
fight_card_poster_url = []

# load our arrays with all of our event data.
for row in cur.fetchall() :
    event_name.append(row[0])
    event_id.append(row[1])
    event_fight_card_url.append(row[2])
    event_org.append(row[3])
    event_date.append(row[4])


x_range = len(event_name)

# This loops for every entry of event in the database to build our fight card information
for x in range(0, x_range):  # prev 0, 533
  #bring in the url information
  #wiki_url = event_fight_card_url[x]
  wiki_url = "http://www.bellator.com/events"
  this_event_poster = loadPosterData(wiki_url, x)
  #fight_card_event_name.append(this_event_name)
  fight_card_poster_url.append(this_event_poster)
  insertRows(this_event_poster, x + 1, event_fight_card_url[x], event_date[x], event_name[x])

  #time.sleep(5)

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
