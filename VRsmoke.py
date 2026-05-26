# Created 20250603 - 
# Jennifer E. Henderson
# Program logs into VRL program and then performs advanced smoke test.
# May be used as part of integrated smoke test.
# Upgrades done:
#   Convert to a function and pass User IR as a variable.
# Planned upgrade(s) - possibly incorporate python html report module, assertion libraries

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

## testing headless - VERIFIED to work 20250723 - but comment out line w ChromeDriverManager() - line 21 to make it work.
'''from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless=new") 
driver = webdriver.Chrome(options=chrome_options)'''

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  ## Must comment out to run headless (lines 15-19).
driver.implicitly_wait(30)  #This adds an implict wait for items to be found or contingent commands to be executed.
driver.maximize_window()

## Note: VESSEL MUST HAVE SP + eNOAD, but NOT a MP hit!!
user = 'HHHVR01'  # May 2021+ VRL AIS/VRL Standard User  	            ## Script works fine - make default user to keep DB login active.
#user = 'HHHVR02'  # May 2021+ VRL/AIS Superv  						    ## Script works fine - Run Monthly
#user = 'HHHVR05'  # May 2021+ VRL Foreign User						    ## Script works fine - Run Monthly - Honestly - I thought it would fail!
#user = 'HHHVR04'  # DEC 2021+ VRL/AIS/VMS Admin			            ## This user gets a LOT of use - no need to run monthly.
#user = 'HHHVR07'  # Sep 2024+ Vessel Risk / VRL/AIS DHS-USCG User  	## Script will fail at Landing Status - Still Run Monthly!
#user = 'HHHVR08'  # Sep 2024+ Vessel Risk / VRL/AIS DHS-HQ User		## Script will fail at select Crew - Still Run Monthly!

vessel = "PORTO KAGIO"
segment = "28652"

#env = "dev"
env = "sat"

# def loginVR(user) here.
def loginVR(user):
    print("\nLogging into Vessel Risk List for smoke test validation!")
    time.sleep(2)
    print("  >Authenticating by passing SSO URL with test ID: "+user+"")
    driver.get("https://apps-"+env+".sat.cbp.dhs.gov/ta/sso/test-login/login/user/"+user+"")
    time.sleep(5)
    print("  >Now logging into the actual Vessel Risk Start page.")
       #driver.get("https://apps-"+env+".sat.cbp.dhs.gov/ta/conveyance/vessel") ## prior to 20250716 (OIDC)
    driver.get("https://apps-"+env+".sat.cbp.dhs.gov/ta/vessel/risk/dashboard.html")  ## 20250716
    time.sleep(5)

    # Functions as page load assertion:
    datatime = driver.find_element("css selector","#page-content-wrapper > div > div > div.section-header-first.padding-top-2 > span > span:nth-child(2)").text # by css selector - works
    #datatime = driver.find_element("xpath","//*[@id='page-content-wrapper']/div/div/div[1]/span/span[2] ").text #by xpath - works
    print ("  >>>> Vessel Risk data " +datatime)
    time.sleep(2)
    #time.sleep(500) ## Use if this is a login helper for testing.
#end

def clearVRfilters():
    print ("\nClearing any open filters...")
    #driver.find_element("xpath", "//*[@id='menu-toggle']").send_keys(Keys.ENTER) ## This works!!
    driver.find_element("css selector","#menu-toggle").send_keys(Keys.ENTER) ## This works!!
         
    time.sleep(2)
    driver.find_element("link text","Clear filters").send_keys(Keys.ENTER) 
   
    time.sleep(3)
    driver.find_element("css selector","#sidebar-wrapper > div > div > div.filters-tab > div > ul > li.pull-right.menu-toggle > a").send_keys(Keys.ENTER) 
    print ("  >>>> FIlters cleared.")
    time.sleep(5)
#end

def toggleHistSch(vessel, segment):
    print ("\nSearching for "+vessel+ " segment " +segment+ ".")
    print ("  >Toggling search to Historical search.")
    driver.find_element("css selector", "#vsl-dash-sgmt-srch > div > div > span:nth-child(1) > button").send_keys(Keys.ENTER) 
    time.sleep(1)
    driver.find_element("css selector", "#vsl-dash-sgmt-srch > div > div > span:nth-child(1) > button").send_keys(Keys.DOWN) 
    time.sleep(2)
    driver.find_element("xpath", "//*[@id='vsl-dash-sgmt-srch']/div/div/span[1]/ul/li[1]/a").send_keys(Keys.ENTER) 
    time.sleep(2)

    driver.find_element("id","main-search").send_keys (segment) 
    time.sleep(2)
    print ("  >Searching...")
    driver.find_element("css selector", "#vsl-dash-sgmt-srch > div > div > span:nth-child(3) > button").send_keys(Keys.ENTER) 
    time.sleep(10)
    ## needs validator.  #row_28626 > div:nth-child(2) > ul > li:nth-child(4) > span > span > span    SBR250506  
    #findme = driver.find_element("css selector", "#row_28626 > div:nth-child(2) > ul > li:nth-child(4) > span > span > span").text
    #findme = driver.find_element("css selector", "#row_28626 > div:nth-child(2) > ul > li:nth-child(4) > span > span > span")
    findme = driver.find_element("css selector", "#row_"+segment+" > div:nth-child(2) > ul > li:nth-child(4) > span > span > span")
    #assert findme.text == "SBR250506" ## this is relatively worthless, because it just passes, but does not give any indication unless it fails. Also - if you change the segment it will fail!
    # #row_28626 > div:nth-child(2) > ul > li:nth-child(1) > span > a > span
    print ("  >>>>Validated return of data for "+vessel+ " Voyage: " +findme.text)
    time.sleep(10)

def goToSegDet(segment):
    print ("\nGoing to the Segment Details Page for segment " +segment+ ".")
    time.sleep(2)
    driver.find_element("css selector", "#row_"+segment+" > div:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > a" ).send_keys(Keys.ENTER) 
    time.sleep(5)
    ## not sure it is on right page... making sure here: (It needed this !!)
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    print("  >Switched to Vessel Detail page")

    vsegdetPg = driver.find_element("css selector", "#bs-example-navbar-collapse-1 > div:nth-child(1) > ul > li.active > a" ).text
    vsegdetNm = driver.find_element("css selector","#vslNm > a ").text
    vsegdetNo = driver.find_element("css selector","#voyageRowSegmentId > span > mark").text
    print ("  >>>>Validated return of data on " +vsegdetPg+ " Page for "+vsegdetNm+ " Segment: " +vsegdetNo+ ".")
    time.sleep(5)

def selectCrw():
    print("\nSelecting a crewmember from "+vessel+" "+segment+ ".")  ## might have to make this a global
    checkbox01 = driver.find_element("css selector", "#vessel-detail-crew-table-body > tr:nth-child(1) > td:nth-child(1) > input[type=checkbox]")
    if not checkbox01.is_selected():
        checkbox01.click() # works!!
    ## xpath - //*[@id="vessel-detail-crew-table-body"]/tr[1]/td[1]/input
    if checkbox01.is_selected():
        print("  >>>>Checkbox is verefied as checked.")
 
def selCrewLineActionBtn(): ## Use for C>P, Crew Edit etc.
    print("\nSelecting the crew line level Actions button.")
    driver.find_element("css selector", "#vessel-detail-crew-table-body > tr.warning > td:nth-child(20) > div > button").click()
    

def selCrewAreaActionsBtn():  ## Use for DOB, I-418, Add Crew, etc,
    print("\nSelecting the crew AREA Actions button.")
    driver.find_element("css selector", "#btn-actions").click()  ##This is the Crew AREA actions button.
    time.sleep(5)

def selCrewGrantLandingStatus():
    print("\nSelecting the Crew Grant Landing Status link.")
    driver.find_element("css selector", "#btn-landing-status-modal").click()
    time.sleep(3) ## Needs time for modal to open before searching.
    if driver.find_element("css selector", "#landingStatusModalLabel").is_displayed():
        print( "  >>The Grant Landing Status modal appeared as required.")
    else:
        print( "  !!!! ERROR - The Grant Landing Status modal did NOT appear as required.")

def closeCrewGrantLandingStatus():
    time.sleep(10)
    print( "  >>>>Closing Grant Landing Status modal.")
    driver.find_element("css selector", "#landingStatusForm > div > div.modal-header > button").send_keys(Keys.ENTER) 
    ## #landingStatusForm > div > div.modal-header > button > span:nth-child(1)
   
## Close current tab

## Go back to Start page

## Verify Vessel Detail Page

## Verify Stow Plan Page

## Verify Conveyance Exam Findings Link and Page.

## Shut down
def shutDown():
    print( "  >>>>Thank you for your service; shutting down now.")
    time.sleep(5)
    driver.close() 
    driver.quit()

loginVR(user)
clearVRfilters()
toggleHistSch(vessel, segment)
goToSegDet(segment)
selectCrw()
selCrewAreaActionsBtn()
selCrewGrantLandingStatus()
closeCrewGrantLandingStatus()
time.sleep(500)
shutDown()