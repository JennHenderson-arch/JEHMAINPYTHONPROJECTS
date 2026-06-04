# Created 20251014 - WIP
# Jennifer E. Henderson
# This is a the selenium work around for popping created messages into the DataBot App and creating the messages that way.
# Required since some infrastructure changes rendered the Pymqi method inop.

# Planned upgrade(s) - unk
# Might want to make a Databot Methods page and put all the Databod methods there and call them when needed!!  >> This is that very thing!!


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

import Vess
import Date
import Port

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  ## Must comment out to run headless (lines 15-19).
driver.implicitly_wait(30)  #This adds an implict wait for items to be found or contingent commands to be executed.
driver.maximize_window()



'''mode = "Databot"
#mode = "PayGov"

#pymntNo = "3"
#pymntNo = "1"
pymntNo = "5"
arvldte = "2025-09-25"  ##Must be manually updated to actual segment ar dte FORMAT diff from Arr dte on Segment.  If same day as segment creation, then that arr date (DEBUG 2 - Date.arrDateJax) variable can be used.
voyNo = "M1202509250256"     ##Must be manually updated to actual segment'''


def openDBCustm():  ## Could do alt for specifics like Ace pay - but it is implemented in that page already.
    driver.get("https://vessel-databot-service.dev.mesh.cbp.dhs.gov/ta/conveyance/vessel/databot/custom")
    time.sleep(5)

def selMsgTyp(msgTyp):
    driver.find_element("name", "messageType").send_keys(Keys.ENTER) 
    time.sleep(1)
    dropdown = Select(driver.find_element("id","messageType"))
        #dropdown.select_by_index(1)  ## This messes up - I saw it pick DEV!
        # Select by visible text
    dropdown.select_by_visible_text(msgTyp)
    time.sleep(1)

def selEnv():
    driver.find_element("name", "env").send_keys(Keys.ENTER) 
    time.sleep(1)
    dropdown = Select(driver.find_element("id","env"))
        # Select by visible text
    dropdown.select_by_visible_text("SAT")
    time.sleep(1)

def selTempl(templTyp):
    driver.find_element("name", "template").send_keys(Keys.ENTER) 
    time.sleep(1)
    dropdown = Select(driver.find_element("id","template"))
        #dropdown.select_by_index(1)  ## This messes up - I saw it pick DEV!
        # Select by visible text
    dropdown.select_by_visible_text(templTyp)
    time.sleep(1)





## I need to put this somewhere so it is callable in ANY program!!
## It is the BOMB!!
## Note>> not used for custom box.  value "messageTxt"  see long message below.
def sledgehammer(ID,value):
    driver.find_element("id",ID).clear()
    time.sleep (2)
    driver.find_element("id",ID).send_keys (value) 

'''  THIS WORKS!!!! 
long_string= message
input_box = driver.find_element("id","messageTxt")
driver.execute_script('arguments[0].value=arguments[1]', input_box, long_string)    
'''
def texthammer(ID,message):
    long_string= message
    input_box = driver.find_element("id",ID)
    driver.execute_script('arguments[0].value=arguments[1]', input_box, long_string)   