
# Created 20250613 - Updated 20260526 for EDI testing - see Date.py for date formats and HC837me.py for message construction.
# Jennifer E. Henderson
# This is the location for person information - for UPAX, MP, USEC, etc. NOT for routine crewpax info!
# Used as locations of person variables for other methods and functions.  

# Planned upgrade(s) - case statement for selction of various vessels. DONE
# Possible pull out Derog codes to a central list, but then they have to be set each time, so nah ?
# >>>>>Might be good to put trip leg ID here, call imo from Vess.

#import Vess


#derogRecordId = yearNowBap + monthnow + daynow + minnow ##must be unique per record. >> on Date.py Consumed on UPAX/MP/USEC as required.

#Test Persons
#Crew
#person = "OREO" #Crew - UPAX or MP
#person = "ARIEJDH" #Crew - UPAX or MP
#person = "USEC" #Crew - UPAX or MP ## Jazmin ALi - must be member of crew, obvs.

#MP Adds
#person = "FINN-HENDERSON" #Crew MP Add ONLY
person = "ARCHIE-HENDERSON" #Crew MP Add ONLY
#person = "MUNDT" #Crew MP Add ONLY
#person = "POLO" #Crew MP Add ONLY

#Passengers - UPAX only
#person = "VAN" #Passenger - UPAX only
#person = "MICKEY" #Passenger - UPAX only


#other codes
#derogCode01 = "10C2"	## Child Abductor
#derogCode02 = "I2D2"	## Procurer of Prostitutes	

match person:  
    case "OREO":  
        fName = "DERRICK"						#BOTH
        lName = "OREO"							#BOTH
        gender	= "male"						#eNOAD use
        genderCd ="M"							#UPAX use
        DoB =	"1983-12-25"					##eNOAD use, MP use
        DoB_UPAX =	"19831225"					#UPAX use
        dobMan = "12251983"					    #Man Gen use
        PPnum =	"DOREO928"					    #BOTH						
        PPcntry =	"RU"						#BOTH
						##@ArvlPtCd =	UPAX use, must be code for name above and match it - added to vessel - DONE		
						#@DepPtCode = "23661" 					#UPAX "Nassau"(NASSAU INTL, BS) Hard-coded in eNOAD
        #travelerID = "04"+Vess.tripLegId	##Unique per traveler per trip - imo and day baked in // Python may need to convert trip leg ID to s string?? //may need to keep this on MQ page.
        						
        derogCode01 = "ATF"	    ##Alcohol Tobacco and Firearms 
						##	derogCode02 = "A%3AD"	## Armed and Dangerous  CTFA -  ##"A/D"
        derogCode02 = "CTFA"	## FIREARMS/MUNITIONS
						# ## temporary override 20201007
						# derogCode01 = "TIP"	## TIPOFF   Record
						# derogCode02 = "P3E1"	## QUASI-REFUSAL   NAZI PERSECUTORS

    case "ARIEJDH":  
        #Test Person
        fName = "JUDY"						#BOTH
        lName = "ARIEJDH"					#BOTH
        gender	= "female"					#eNOAD use
        genderCd ="F"						#UPAX use
        DoB =	"2000-07-19"				##eNOAD use, MP use
        DoB_UPAX =	"20000719"				#UPAX use
        dobMan = "12251983"					#Man Gen use
        PPnum =	"IRIRJDJ8RU"					#BOTH						
        PPcntry =	"RU"						#BOTH
						##@ArvlPtCd =	UPAX use, must be code for name above and match it - added to vessel - DONE		
						#@DepPtCode = "23661" 					#UPAX "Nassau"(NASSAU INTL, BS) Hard-coded in eNOAD
        #travelerID = "01" + Vess.tripLegId	##Unique per traveler per trip - imo and day baked in // Python may need to convert trip leg ID to s string?? //may need to keep this on MQ page.
        #derogRecordId = yearNowBap + monthnow + daynow + minnow ##must be unique per record.						
        derogCode01 = "VRFSL" 	## VISA Refusal
						##	derogCode02 = "A%3AD"	## Armed and Dangerous  CTFA -  ##"A/D"
        derogCode02 = "VRVK"	## VISA Revoked
						# ## temporary override 20201007
						# derogCode01 = "TIP"	## TIPOFF   Record
						# derogCode02 = "P3E1"	## QUASI-REFUSAL   NAZI PERSECUTORS

    case "VAN":	## Traveler B / Passenger - TC 02 PASSPORT NUMBER is two words so passenger type is PA with match.
        fName ="COCO"							#BOTH
        lName ="VAN"                            #BOTH
        gender	= "female"						#eNOAD use
        genderCd ="F"							#UPAX use
        DoB =	"1960-06-17"					#eNOAD use, MP use
        DoB_UPAX =	"19600617"					#UPAX use
        dobMan = "12251983"					#Man Gen use
        PPnum =	"56324444"					#BOTH
        PPcntry =	"US"						#BOTH
						##@ArvlPtCd =	UPAX use, must be code for name above and match it - added to vessel - DONE		
						#@DepPtCode = "23661" 					#UPAX "Nassau"(NASSAU INTL, BS) Hard-coded in eNOAD
        #travelerID = "02" + Vess.tripLegId	##Unique per traveler per trip - imo and day baked in
						#@travelerID = "20444444" 				##Unique per traveler per trip
						#@derogRecordId = "2327902"  			## on Date.py
        derogCode01 = "TIP"	## TIPOFF   Record
        derogCode02 = "P3E1"	## QUASI-REFUSAL   NAZI PERSECUTORS		
						# ## temporary override 20201007 TC19
						#derogCode01 = "ATF"	##Alcohol Tobacco and Firearms 
						#derogCode02 = "CTFA"	## FIREARMS/MUNITIONS                   

    case "FINN-HENDERSON":	## Traveler B / Passenger - TC 02 PASSPORT NUMBER is two words so passenger type is PA with match.
        fName ="FINEGAN"							#BOTH
        lName ="BOYD-HENDERSON"                            #BOTH
        gender	= "male"						#eNOAD use
        genderCd ="M"							#UPAX use
        DoB =	"2010-05-01"					#eNOAD use, MP use Died June 2022 :(
        DoB_UPAX =	"20100501"					#UPAX use
        dobMan = "12251983"					#Man Gen use
        PPnum =	"HENDOG08"					#BOTH
        PPcntry =	"UK"						#BOTH
						##@ArvlPtCd =	UPAX use, must be code for name above and match it - added to vessel - DONE		
						#@DepPtCode = "23661" 					#UPAX "Nassau"(NASSAU INTL, BS) Hard-coded in eNOAD
        #travelerID = "06" + Vess.tripLegId	##Unique per traveler per trip - imo and day baked in
						#@travelerID = "20444444" 				##Unique per traveler per trip
						#@derogRecordId = "2327902"  			## on Date.py
        derogCode01 = "I10B"	##Requires Guardian 
        derogCode02 = "I08"	    ## Professional Beggar, haha - true!	
						# ## temporary override 20201007 TC19
						#derogCode01 = "ATF"	##Alcohol Tobacco and Firearms 
						#derogCode02 = "CTFA"	## FIREARMS/MUNITIONS

    case "ARCHIE-HENDERSON":	## Traveler G / Crew - TC ??  Not on eNOAD - MP add
        fName ="ARCHIBALD"							#BOTH
        lName ="HENDERSON"                            #BOTH
        gender	= "male"						#eNOAD use
        genderCd ="M"							#UPAX use
        DoB =	"2019-12-18"					#eNOAD use, MP use
        DoB_UPAX =	"20191218"					#UPAX use
        dobMan = "12251983"					#Man Gen use
        PPnum =	"HENDOG09"					#BOTH
        PPcntry =	"UK"						#BOTH
						##@ArvlPtCd =	UPAX use, must be code for name above and match it - added to vessel - DONE		
						#@DepPtCode = "23661" 					#UPAX "Nassau"(NASSAU INTL, BS) Hard-coded in eNOAD
        #travelerID = "09" + Vess.tripLegId	##Unique per traveler per trip - imo and day baked in
						#@travelerID = "20444444" 				##Unique per traveler per trip
						#@derogRecordId = "2327902"  			## on Date.py
        derogCode01 = "I10B"	##Requires Guardian 
        derogCode02 = "I08"	    ## Professional Beggar, haha - true!	
						# ## temporary override 20201007 TC19
						#derogCode01 = "ATF"	##Alcohol Tobacco and Firearms 
						#derogCode02 = "CTFA"	## FIREARMS/MUNITIONS

    case "MUNDT":	## Traveler F / Crew - TC ??  Not on eNOAD - MP add
        fName ="KARL"							#BOTH
        lName ="MUNDT"                            #BOTH
        gender	= "male"						#eNOAD use
        genderCd ="M"							#UPAX use
        DoB =	"2015-06-02"					#eNOAD use, MP use
        DoB_UPAX =	"20150602"					#UPAX use
        dobMan = "06022015"					#Man Gen use
        PPnum =	"KMUNDT91"					#BOTH
        PPcntry =	"US"						#BOTH
						##@ArvlPtCd =	UPAX use, must be code for name above and match it - added to vessel - DONE		
						#@DepPtCode = "23661" 					#UPAX "Nassau"(NASSAU INTL, BS) Hard-coded in eNOAD
        #travelerID = "07" + Vess.tripLegId	##Unique per traveler per trip - imo and day baked in
						#@travelerID = "20444444" 				##Unique per traveler per trip
						#@derogRecordId = "2327902"  			## on Date.py
        derogCode01 = "IF01"	##NOTIFY NEAREST FBI   SPECIAL AGENT.  DO NOT DETAIN 
        derogCode02 = "STXA"	## STATUS   CODE - FUGITIVE, FBI	
						# ## temporary override 20201007 TC19
						#derogCode01 = "ATF"	##Alcohol Tobacco and Firearms 
						#derogCode02 = "CTFA"	## FIREARMS/MUNITIONS

    case "USEC":	## Use ONLY w USEC testing until this warning is amended :/ 20250712 - not sure this is an issue.
        fName ="JAZMIN"							#BOTH
        lName ="ALI"                            #BOTH
        gender	= "female"						#eNOAD use
        genderCd ="F"							#UPAX use
        DoB =	"1990-04-07"					#eNOAD use, MP use
        DoB_UPAX =	"19900407"					#UPAX use
        dobMan = "04071990"					#Man Gen use
        PPnum =	"A17112720"					#BOTH
        PPcntry =	"GB"						#BOTH
						##@ArvlPtCd =	UPAX use, must be code for name above and match it - added to vessel - DONE		
						#@DepPtCode = "23661" 					#UPAX "Nassau"(NASSAU INTL, BS) Hard-coded in eNOAD
        #travelerID = "08" + Vess.tripLegId	##Unique per traveler per trip - imo and day baked in
						#@travelerID = "20444444" 				##Unique per traveler per trip
						#@derogRecordId = "2327902"  			## on Date.py
        derogCode01 = "IF01"	##NOTIFY NEAREST FBI   SPECIAL AGENT.  DO NOT DETAIN 
        derogCode02 = "STXA"	## STATUS   CODE - FUGITIVE, FBI	
						# ## temporary override 20201007 TC19
						#derogCode01 = "ATF"	##Alcohol Tobacco and Firearms 
						#derogCode02 = "CTFA"	## FIREARMS/MUNITIONS

    case "POLO":	## Traveler E / Crew - TC ??  Not on eNOAD - MP add
        fName ="MARKO"							#BOTH
        lName ="POLO"                            #BOTH
        gender	= "male"						#eNOAD use
        genderCd ="M"							#UPAX use
        DoB =	"1955-12-25"					#eNOAD use, MP use
        DoB_UPAX =	"19551225"					#UPAX use
        dobMan = "12251983"					#Man Gen use
        PPnum =	"POLOO928"					#BOTH
        PPcntry =	"IT"						#BOTH
						##@ArvlPtCd =	UPAX use, must be code for name above and match it - added to vessel - DONE		
						#@DepPtCode = "23661" 					#UPAX "Nassau"(NASSAU INTL, BS) Hard-coded in eNOAD
        #travelerID = "05" + Vess.tripLegId	##Unique per traveler per trip - imo and day baked in
						#@travelerID = "20444444" 				##Unique per traveler per trip
						#@derogRecordId = "2327902"  			## on Date.py
        derogCode01 = "P10C1"	##Intl Child Abductor
        derogCode02 = "I3G"	## Recruitment oor Use of Child Soldiers	
						# ## temporary override 20201007 TC19
						#derogCode01 = "ATF"	##Alcohol Tobacco and Firearms 
						#derogCode02 = "CTFA"	## FIREARMS/MUNITIONS

    case "MICKEY":	## Traveler E / Crew - TC ??  Not on eNOAD - MP add
        fName ="MICKEY"							#BOTH
        lName ="MOUSEANDCOMPANY"                            #BOTH
        gender	= "male"						#eNOAD use
        genderCd ="M"							#UPAX use
        DoB =	"1900-01-01"					#eNOAD use, MP use
        DoB_UPAX =	"19000101"					#UPAX use
        dobMan = "12251983"					#Man Gen use
        PPnum =	"0123UDN77"					#BOTH
        PPcntry =	"GB"						#BOTH
						##@ArvlPtCd =	UPAX use, must be code for name above and match it - added to vessel - DONE		
						#@DepPtCode = "23661" 					#UPAX "Nassau"(NASSAU INTL, BS) Hard-coded in eNOAD
        #travelerID = "03" + Vess.tripLegId	##Unique per traveler per trip - imo and day baked in
						#@travelerID = "20444444" 				##Unique per traveler per trip
						#@derogRecordId = "2327902"  			## on Date.py
        derogCode01 = "P10C1"	##Intl Child Abductor
        derogCode02 = "I3G"	## Recruitment oor Use of Child Soldiers	
						# ## temporary override 20201007 TC19
						#derogCode01 = "ATF"	##Alcohol Tobacco and Firearms 
						#derogCode02 = "CTFA"	## FIREARMS/MUNITIONS



    case _:
        print("yer preson iz probly spelt wrongue!")
   


