# Created 20250703 - updated 20260526 for EDI testing. 
# Jennifer E. Henderson
# This is the location for Dates information.
# Used as locations of port variables for other methods and functions.

# Planned upgrade(s) - use time library to auto compute

## It could be more expeditious just to hardcode rather than compute dates. 
#  Compute dates here, but also have a hardcoded mode.

import time

#set-ups for date computed, formatted:
from datetime import datetime, timedelta

mode = "hardcoded"
mode = "computed" ## Based on Today system Time - one day hopper - most ususal config.
#mode = "2Weeks"  ## Dep GE  2 weeks (14 days) ago; Arr Miami is tomorrow // According to AI, China - LA/LB is about the same time schedule!!

timenow = datetime.now()
print("DEBUG 1- Current Date and Time:", timenow)

""" yearNow = now.strftime ("%Y")
yearNowBap = now.strftime ("%y")  ##2 digit, ie., 19
monthnow = now.strftime ("%m")  #zero padded if required.
daynow = now.strftime ("%d") #zero padded if required.
hournow = now.strftime ("%H")
minnow = now.strftime ("%M") 
				
				
runTime = now.strftime ("%m-%d-%Y: %H%M")
currentTime = now.strftime ("%H%M") """
		##@timeMS = current_time.strftime "%H%M%5N"  ## used in BOLA base 100 - error
        ##timeMS01 = now.strftime ("%3N")  ## used in BOLA hardcoded "00" to hopefully make this work
        ##timeMS = currentTime + "00" + timeMS01   ## used in BOLA
        ##timeSSMS = now.strftime ("%H%M%S%2N")

MPauditTime = datetime.now().strftime ("%m-%d-%Y")

## This below is the kernal of getting this whole thing to work much better than it did in Ruby!!
arrDateJax = datetime.now().strftime ("%Y-%m-%d")
tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
print ("DEBUG 2- Current Day is: ", arrDateJax)
print ("DEBUG 3- One day from now is: ", tomorrow)   
print ("DEBUG 4- One day ago was: ", yesterday)   



match mode:  
    case "hardcoded":

    #EDI 837 message DTG format: 
        timeNowDate837 = "20260523"    #date of mesage Creation in format YYYYMMDD - this is used in the ISA and GS segments of the message.  This is not necessarily the same as the date of service, which is used in the DTM segments of the message.
        timeNowTime837 = "1741"        #time of message creation in format HHMM - this is used in the ISA and GS segments of the message.  This is not necessarily the same as the time of service, which is used in the DTM segments of the message.

    # UPAX FORMAT DATE - "departureDate":"2020-07-13T04:00:00.000","arrivalDate":"2020-07-14T17:00:00.000" 
        arrDateGer02 = "2025-05-02"   #(current_time - 4)	
        depDateGer02 = "2025-05-03"  #(current_time - 3)	

        arrDateGer03  = "2025-04-31" #(current_time - 6)	
        depDateGer03  = "2025-05-01" #(current_time - 5)	

        arrDateGer04  = "2025-04-29"  #(current_time - 8)	
        depDateGer04  = "2025-04-30" #(current_time - 7)	

        arrDateGer05  = "2025-04-27"  #(current_time - 10)	
        depDateGer05  = "2025-04-28"  #(current_time - 9)	

        arrDateGer  = "2025-05-04" #(current_time - 2)	
        depDateGer = "2025-05-05"     #Hardcode for test  #(current_time - 1)	
        arrDateJax = "2025-05-06"     #*** Hardcode for test  #(current_time - 0)***	***(ARRIVAL DAY)***
        depDateJax = "2025-05-07"     #Hardcode for test  #(current_time + 1)	

        #CW1
        #arrDateSav      #Hardcode for test  #(current_time + 1)	
        #depDateSav      #Hardcode for test  #(current_time + 1)	

        #CW2
        #arrDateChas     #Hardcode for test  #(current_time + 1)	
        #depDateChas     #Hardcode for test  #(current_time + 1)	

        #DEP01
        #timeArrGerL    #depDateJax  +3 if one hopper
        #timeArrGerL     #depDateChas +7 

    ##  BAPLIE Dates - These are a diferent format: 
        ## DTM+137 = message time
        ## DTM+137:202005041455:203'
         ## DTM+137:202505041455:203'   ## @yearNowBap.to_s+ @monthnow.to_s+ @daynow.to_s+ @hournow.to_s+ @minnow.to_s
        timeNowBap = "202505061455" 

        ## DTM+136 = Departure time - use depDateGerBap 
        ##  DTM+136:202008181615:203' #time was 2215 - but the time zones are messed up in SAT - so use 1915 - It could have issues matching if you don't!
        ##  1915 shows in VRL as 2315!! // changing to 1715
        depDateGerBap ="202505051715"

        ## DTM+132 = Estimated arrival time - use arrDateJaxBap
        #DTM+132:202008202250:203'
        arrDateJaxBap = "202505061455" 

        #tripLegSeed = #monthnow + daynow + minnow  ## e.g., "070922"
        tripLegSeed = "050622"
        #voySeed =  #yearNowBap + monthnow + daynow   ##  e.g., "250709"   
        voySeed = "250506" 

        derogRecordId = "25050622" #yearNowBap + monthnow + daynow + minnow ## e.g."25070822" 

        #BOLdateNow = @yearNow.to_s+ @monthnow.to_s+ @daynow.to_s
        BOLdateNow = "20250506"
        #SealSeed = @yearArrJax.to_s + @arrMonJax.to_s + @arrDayJax.to_s
        SealSeed = "20250506"
        processDate = "20250506"
        #BOLarrDateJax = @arrYearJax.to_s[2025 %Y]+@arrMonJax.to_s+@arrDayJax.to_s
        BOLARRDateJax = "20250506"
        #@BOLarrdate = @yearArrJax.to_s[25 %y]+ @arrMonJax.to_s+ @arrDayJax.to_s
        BOLarrdate = "250506"
        ## I think we can get away w hardcoding this (HHMMSSsss)(s=milliseconds in 3 digit)"time" on old databot:
        timeMS = "145513165"
        timeMS = "151513165"  ## Note - if you run a correction or 2nd BOLA - you may need to make this unique...bc this is used in process time >> computed will change the minutes to be OK.
        ## I think we can get away w hardcoding this (SSss)(s=milliseconds in 2 digit) // I am not sure this is really used:
        timeSSMS = "1316"

    case "computed":        ## BOLA NOT CODED UP 20250924
    #EDI 837 message DTG format:     
        timeNowDate837 = datetime.now().strftime ("%Y%m%d")    #date of mesage Creation in format YYYYMMDD - this is used in the ISA and GS segments of the message.  This is not necessarily the same as the date of service, which is used in the DTM segments of the message.
        timeNowTime837 = datetime.now().strftime ("%H%M")        #time of message creation in format HHMM - this is used in the ISA and GS segments of the message.  This is not necessarily the same as the time of service, which is used in the DTM segments of the message.

    # eNOAD, MP, UPAX FORMAT DATE - "departureDate":"2020-07-13T04:00:00.000","arrivalDate":"2020-07-14T17:00:00.000" 
        arrDateGer02 = (datetime.now() - timedelta(days=4)).strftime("%Y-%m-%d")    #(current_time - 4)	
        depDateGer02 = (datetime.now() - timedelta(days=3)).strftime("%Y-%m-%d")    #(current_time - 3)	

        arrDateGer03  = (datetime.now() - timedelta(days=6)).strftime("%Y-%m-%d")   #(current_time - 6)	
        depDateGer03  = (datetime.now() - timedelta(days=5)).strftime("%Y-%m-%d")   #(current_time - 5)	

        arrDateGer04  = (datetime.now() - timedelta(days=8)).strftime("%Y-%m-%d")   #(current_time - 8)	
        depDateGer04  = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")   #(current_time - 7)	

        arrDateGer05  = (datetime.now() - timedelta(days=10)).strftime("%Y-%m-%d")  #(current_time - 10)	
        depDateGer05  = (datetime.now() - timedelta(days=9)).strftime("%Y-%m-%d")   #(current_time - 9)	

        arrDateGer  = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d")     #(current_time - 2)	
        depDateGer = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")      #(current_time - 1)	

        arrDateJax = datetime.now().strftime ("%Y-%m-%d")                           #(current_time - 0)***	***(ARRIVING TODAY)*** 
        depDateJax = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")      #(current_time + 1)	

        #CW1
        #arrDateSav      #Hardcode for test  #(current_time + 2)	
        #depDateSav      #Hardcode for test  #(current_time + 1)	

        #CW2
        #arrDateChas     #Hardcode for test  #(current_time + 1)	## I think this should be +2
        #depDateChas     #Hardcode for test  #(current_time + 1)	## I think this should be +3

        #DEP01
        #timeArrGerL    #depDateJax  +3 if one hopper
        #timeArrGerL     #depDateChas +7 

        #DEP02          ## Following visit to CW2.
        #timeArrGerL    #depDateJax  +4
        #timeArrGerL     #depDateChas +8

    ## BAPLIE Dates - These are a diferent format: 
        ## DTM+137 = message time
        ## DTM+137:202505041455:203'   ## @yearNowBap.to_s+ @monthnow.to_s+ @daynow.to_s+ @hournow.to_s+ @minnow.to_s
        timeNowBap = datetime.now().strftime ("%Y%m%d%H%M")   

        ## DTM+136 = Departure time - use depDateGerBap >> one day ago
        ##  DTM+136:202508182215:203'
        depDateGerBap = (datetime.now() - timedelta(days=1)).strftime("%Y%m%d%H%M")    

        ## DTM+132 = Estimated arrival time - use arrDateJaxBap >> Today
        #DTM+132:202508202250:203'
        arrDateJaxBap = datetime.now().strftime ("%Y%m%d%H%M")  

        ## DATETIME FORMATS - datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") // 2 digit year date is %y

        tripLegSeed = datetime.now().strftime ("%m%d%M")  #monthnow + daynow + minnow   ## eg.,"070922"
        voySeed = datetime.now().strftime ("%y%m%d") #yearNowBap + monthnow + daynow   ##  e.g., "250709"   
        derogRecordId = datetime.now().strftime ("%y%m%d%M") #yearNowBap + monthnow + daynow + minnow ## e.g."25070822" 

        #BOLdateNow = @yearNow.to_s+ @monthnow.to_s+ @daynow.to_s
        BOLdateNow = datetime.now().strftime ("%y%m%d")
        #BOLarrDateJax = @arrYearJax.to_s[2025 %Y]+@arrMonJax.to_s+@arrDayJax.to_s
        BOLARRDateJax = datetime.now().strftime ("%Y%m%d")
        #@BOLarrdate = @yearArrJax.to_s[25 %y]+ @arrMonJax.to_s+ @arrDayJax.to_s
        BOLarrdate = datetime.now().strftime ("%y%m%d")
        #SealSeed = @yearArrJax.to_s + @arrMonJax.to_s + @arrDayJax.to_s
        SealSeed = datetime.now().strftime ("%y%m%d")
        processDate = datetime.now().strftime ("%y%m%d") #same as BOLdatenow
        #BOLarrDateJax = @arrYearJax.to_s[2025 %Y]+@arrMonJax.to_s+@arrDayJax.to_s

        # THESE NEED TO BE CODED UP LIKE THE OTHERS
        BOLARRDateJax = "20250506"
        #@BOLarrdate = @yearArrJax.to_s[25 %y]+ @arrMonJax.to_s+ @arrDayJax.to_s
        BOLarrdate = "250506"

        ## I think we can get away w partially hardcoding this (HHMMSSsss)(s=milliseconds in 3 digit)"time" on old databot:
        timeMS = "145513165"
        timeMS = "151513165"  ## Note - if you run a correction or 2nd BOLA - you may need to make this unique...bc this is used in process time >> computed will change the minutes to be OK.
        ## I think we can get away w hardcoding this (SSss)(s=milliseconds in 2 digit) // I am not sure this is really used:
        timeSSMS = "1316"       



    case "2Weeks":  ## the port rotation ports will probably be nonsensical - Carribean Ports.  See: messagePrevForPortListBahamas  on ENOAD_ARRme.py  ## BOLA NOT CODED UP 20250924

    # eNOAD, MP, UPAX FORMAT DATE - "departureDate":"2020-07-13T04:00:00.000","arrivalDate":"2020-07-14T17:00:00.000" 
    ## Note - the ports for the rotation are currently coded as Carribean ports :/ so for GE or CN/AU these would need to be coded differently??  JEH 20251021
   
        arrDateGer05  = (datetime.now() - timedelta(days=23)).strftime("%Y-%m-%d")  #(current_time - 10) -23	
        depDateGer05  = (datetime.now() - timedelta(days=22)).strftime("%Y-%m-%d")   #(current_time - 9)	-22

        arrDateGer04  = (datetime.now() - timedelta(days=21)).strftime("%Y-%m-%d")   #(current_time - 8)	-21
        depDateGer04  = (datetime.now() - timedelta(days=20)).strftime("%Y-%m-%d")   #(current_time - 7)	-20

        arrDateGer03  = (datetime.now() - timedelta(days=19)).strftime("%Y-%m-%d")   #(current_time - 6)	-19
        depDateGer03  = (datetime.now() - timedelta(days=18)).strftime("%Y-%m-%d")   #(current_time - 5)	-18

        arrDateGer02 = (datetime.now() - timedelta(days=17)).strftime("%Y-%m-%d")    #(current_time - 4)	-17
        depDateGer02 = (datetime.now() - timedelta(days=16)).strftime("%Y-%m-%d")    #(current_time - 3)	-16

        arrDateGer  = (datetime.now() - timedelta(days=15)).strftime("%Y-%m-%d")     #(current_time - 2)	-15
        depDateGer = (datetime.now() - timedelta(days=14)).strftime("%Y-%m-%d")      #(current_time - 1)	-14 //will be 15 day journey

        #arrDateJax = datetime.now().strftime ("%Y-%m-%d")                           #(current_time - 0) ***arriving today // +1* CHANGE TO (ARRIVING TOMORROW)*** 
        arrDateJax = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")      #(current_time + 1)	+1 
        depDateJax = (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d")      #(current_time + 1)	+2 dep JAX day after tomorrow

        #CW1
        #arrDateSav      #Hardcode for test  #(current_time + 2)	## next coast wise arr would prob be tomorrow +2 = +3
        #depDateSav      #Hardcode for test  #(current_time + 3)	

        #CW2
        #arrDateChas     #Hardcode for test  #(current_time + 4)	## add +1 to this
        #depDateChas     #Hardcode for test  #(current_time + 5)	

        #DEP01
        #timeArrGerL    #depDateJax  +3 if one hopper   ## add +1 to this, so = +4
        #timeArrGerL     #depDateChas +7 

    ## BAPLIE Dates - These are a diferent format: 
        ## DTM+137 = message time
        ## DTM+137:202505041455:203'   ## @yearNowBap.to_s+ @monthnow.to_s+ @daynow.to_s+ @hournow.to_s+ @minnow.to_s ##Stays the same
        timeNowBap = datetime.now().strftime ("%Y%m%d%H%M")   

        ## DTM+136 = Departure time - use depDateGerBap >> one day ago >> -14
        ##  DTM+136:202508182215:203'
        depDateGerBap = (datetime.now() - timedelta(days=14)).strftime("%Y%m%d%H%M")    

        ## DTM+132 = Estimated arrival time - use arrDateJaxBap >> Today >> Tomorrow +1
        #DTM+132:202508202250:203'
        #arrDateJaxBap = datetime.now().strftime ("%Y%m%d%H%M")
        arrDateJaxBap = (datetime.now() + timedelta(days=1)).strftime("%Y%m%d%H%M")     

        ## DATETIME FORMATS - datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") // 2 digit year date is %y

        tripLegSeed = (datetime.now() + timedelta(days=1)).strftime ("%m%d%M")  #monthnow + daynow + minnow   ## eg.,"070922"                 ## these need +1 to be consistent
        voySeed = (datetime.now() + timedelta(days=1)).strftime ("%y%m%d") #yearNowBap + monthnow + daynow   ##  e.g., "250709"   
        derogRecordId = (datetime.now() + timedelta(days=1)).strftime ("%y%m%d%M") #yearNowBap + monthnow + daynow + minnow ## e.g."25070822" 

        #BOLdateNow = @yearNow.to_s+ @monthnow.to_s+ @daynow.to_s        ##Keep as is.               
        BOLdateNow = datetime.now().strftime ("%y%m%d")
        #BOLarrDateJax = @arrYearJax.to_s[2025 %Y]+@arrMonJax.to_s+@arrDayJax.to_s  ## These will need to be corrected to +1
        BOLARRDateJax = (datetime.now() + timedelta(days=1)).strftime ("%Y%m%d")
        #@BOLarrdate = @yearArrJax.to_s[25 %y]+ @arrMonJax.to_s+ @arrDayJax.to_s
        BOLarrdate = (datetime.now() + timedelta(days=1)).strftime ("%y%m%d")
        #SealSeed = @yearArrJax.to_s + @arrMonJax.to_s + @arrDayJax.to_s
        SealSeed = (datetime.now() + timedelta(days=1)).strftime ("%y%m%d")

        processDate = datetime.now().strftime ("%y%m%d") #same as BOLdatenow  ## No change needed
        #BOLarrDateJax = @arrYearJax.to_s[2025 %Y]+@arrMonJax.to_s+@arrDayJax.to_s

        # THESE NEED TO BE CODED UP LIKE THE OTHERS..Note format. %Y%m%d ## Needs +1
        BOLARRDateJax = "20250506"
        #@BOLarrdate = @yearArrJax.to_s[25>> %y]+ @arrMonJax.to_s+ @arrDayJax.to_s  %y%m%d ## Needs +1
        BOLarrdate = "250506"

        ## I think we can get away w partially hardcoding this (HHMMSSsss)(s=milliseconds in 3 digit)"time" on old databot:
        timeMS = "145513165"
        timeMS = "151513165"  ## Note - if you run a correction or 2nd BOLA - you may need to make this unique...bc this is used in process time >> computed will change the minutes to be OK.
        ## I think we can get away w hardcoding this (SSss)(s=milliseconds in 2 digit) // I am not sure this is really used:
        timeSSMS = "1316"       






        print ("DEBUG 5c- TripLeg seed: ", tripLegSeed)  
        print ("DEBUG 6c- Voyage seed: ", voySeed)
        print ("DEBUG 7c- Derog Record ID seed: ", derogRecordId)