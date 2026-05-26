# Created 20260523
# Jennifer E. Henderson
# This program is for text message formatting, based on a similar BOLA X12 message format. This is for Health Care 837 P message formatting.  This program is not for sending messages, but is for creating the text of the message that can be sent.  It may be used for testing the formatting of the message, and for creating the text of the message that can be sent to the MQ queue.  It may also be used for creating data text files that can be used for testing the MQ message sending code.  The 837 message is a complex message with many segments and data elements, so this program is used to create the text of the message in a structured way.  The equipment segments are synched with the BOLA load combinations, so if you change one, change the other.  The 837 message uses "*" as a data element separator and "~" as a segment terminator, so these are used in the formatting of the message.  The message is created in parts, with the header and trailer segments created separately from the equipment segments, so that the individual elements can be easily modified without affecting the header and trailer segments.  The equipment segments are created in a way that allows for easy modification of the container information, such as container number, weight, and cargo description.  The message is created as a string that can be printed or written to a file, and can also be sent to an MQ queue using the mqME(message) function in venv/HC837me.py.
# May be used for data text file creation. Also can use Databot helper functions to submit message via a web UI interface.

# Planned upgrade(s) - Add additional versions of 837, the I and D versions.
# Also - parameterize the message for providers, patients, subscribers, medical codes etc.


import time
import os
#import pymqi


## Data files for BAPLIE message creation.  These are synched with the BOLA load combinations as indicated in the comments.  If you change one, change the other
import Date  
import Submitter
"""## needs to go first so tripleg ID and voyage nos are available
import Vess  ## Trip and Voyage are computed here
import Pers
import Port """

# BAPLIE type Codes:
bapType = "9"  #Original   ##most used - If used on an update, will not update will create new.
#bapType = "2"   #Add		## second most used - Updates w more containers. 20250415 - actually saw it add, not rplace the list when I added 3180 to a 3 cont load = 3183 !!
#bapType = "3" # DELETE // Activated 20241028  ##   [For CANCELATION - look at and use code around line 380 - 202405522 << VALID??]
#bapType = "4"  #With Changes
#bapType = "5" #Replace
#bapType = "22"  #Final did not seem to work 20221122

"""
"connName": "Stowplan Queue US SAT ",
"destName": "ATS.SECFIL.EDI.STOWPLAN.INBOUND",
"hostname": "ats-s01.cbp.dhs.gov",
"port": "1414",
"qManager": "QM_ATSS01",
"qChannel": "QM_ATSS01.ATS"
"""

## Foreign SP
"""      
"connName": "Stowplan Queue Foreign SAT ",
"destName": "ATS.SECFIL.EDI.STOWPLAN.CO.INBOUND",
"hostname": "ats-s01.cbp.dhs.gov",
"port": "1414",
"qManager": "QM_ATSS01",
"qChannel": "QM_ATSS01.ATS"
"""


'''def mqME(message):  #THIS IS CARGO // Validated 20250717
    queue_manager = 'QM_ATSS01'
    #channel = myChannel 
    channel = "QM_ATSS01.ATS"
    host = 'ats-s01.cbp.dhs.gov'
    port = '1414'
    #queue_name = destination  ## 
    queue_name ="ATS.SECFIL.EDI.STOWPLAN.INBOUND" ##For foreign this would be CO.INBOUND
    conn_info = '%s(%s)' % (host, port)
    qmgr = pymqi.connect(queue_manager, channel, conn_info)
    queue = pymqi.Queue(qmgr, queue_name) 

    queue.put(message)

    queue.close()
    qmgr.disconnect()
#End mqME(message)'''

###################### 837P Message Creation #########################
## Example 837 P message - for reference only.  This is here for reference to the format of the message and the use of the "*" and "~" delimiters.  The BAPLIE message uses the same delimiters, but different segment identifiers and data elements.

## placeholder variable data.
timeNowDate837 = "20260523"  ## Date of message creation - use Date.timeNowDte for this element in the message.  This is not the same as the date of service, which is used in the DTP segment of the message.
timeNowTime837 = "1741"  ## Time of message creation - use Date.timeNowTme for this element in the message.  This is not the same as the time of service, which is used in the DTP segment of the message.

provider = "BILLING PROVIDER"  ## This is the name of the billing provider, which is used in the NM1 segment of the message.  This is not the same as the name of the submitter, which is used in the NM1 segment of the message.
 
header83701 = "ISA*00*          *00*          *ZZ*1234567        *ZZ*11111          *170508*1141*^*00501*000000101*1*P*:~\nGS*HC*XXXXXXX*XXXXX*"+Date.timeNowDate837+"*"+Date.timeNowTime837+"*101*X*005010X222A1~\nST*837*1239*005010X222A1~"



submitter = "\nBHT*0019*00*010*"+Date.timeNowDate837+"*"+Date.timeNowTime837+"*CH~\nNM1*41*2*SUBMITTER*****46*ABC123~\nPER*IC*"+Submitter.fName+" "+Submitter.lName+"*TE*4805551212~\nNM1*40*2*RECEIVER*****46*44556~"

"""
\nHL*1**20*1~
\nNM1*85*2*BILLING PROVIDER*****XX*1122334455~
\nN3*1234 SOME ROAD~
\nN4*CHICAGO*IL*606739999~
\nREF*EI*999999999~

\nHL*2*1*22*0~
\nSBR*P*18*******12~
\nNM1*IL*1*BLOGGS*JOE****MI*1234567890~
\nN3*1 SOME BLVD~
\nN4*CHICAGO*IL*606129998~
\nDMG*D8*19570111*M~
\nNM1*PR*2*PAYER*****PI*12345~
\nN3*1 PAYER WAY~
\nN4*ST LOUIS*MO*212441850~
\nREF*2U*W1014~
\nCLM*1000A*140***19:B:1*Y*A*Y*Y~
\nHI*ABK:I10~
\nLX*1~
\nSV1*HC:99213*140*UN*1***1~
\nDTP*472*D8*20151124~

\nHL*3*1*22*0~
\nSBR*P*18*******12~
\nNM1*IL*1*BLOGGS*FRED****MI*9876543201~
\nN3*1 ANOTHER STR~
\nN4*CHICAGO*IL*606129998~
\nDMG*D8*19700601*M~
\nNM1*PR*2*PAYER*****PI*12345~
\nN3*1 PAYER WAY~
\nN4*ST LOUIS*MO*212441850~
\nREF*2U*W1014~

\nCLM*1001A*140***19:B:1*Y*A*Y*Y~
\nHI*ABK:I10~
\nLX*1~
"""
## SV1 is the service line segment, SV1 is unique to the 837P.
## Used to report the details of the service provided, such as the procedure code, the charge amount, and the units of service.  
SV101= "\nSV1*HC:99213*140*UN*1***1~\nDTP*472*D8*20151124~"

ender837 = "\nSE*41*1239~\nGE*1*101~\nIEA*1*000000101~"

### End of 837P Msg



## BAPLIE message
""" bapliePt1 = "UNB+UNOB:2+MSCU+USCS+171022:0618+14840'UNH+14840+BAPLIE:D:95B:UN:SMDG20'BGM++"+Vess.trip+"+"+bapType+"'DTM+137:"	
## timeNowBap here
bapliePt2 = ":201'TDT+20+"+Vess.trip+"+++MSCU:172:182+++"+Vess.imo+":172:11:"+Vess.vName+"'"   ## same for every vessel
#bapliePt2alt = ":201'TDT+20+++"+Vess.imo+":172:11:"+Vess.vName+"'" ## There must have been a Thiagu Test case to NOT have a trip ID on a BAPLIE

##  bapliePt2a = "LOC+5+DEHAM:139:6'LOC+61+USJAX'DTM+132:" ## Are you insane?  This only sends Hamburg to Jax! This is pre-2018 code >:(
#For US_ARRIVAL BAPLIES ############### This is the default setting for running all of this on Arrival SP BAPLIES
bapliePt2a = "\nLOC+5+"+Port.bapDepPtCode+":139:6'\nLOC+61+"+Port.bapArvlPtCd+"'DTM+132:" 		##>>> BAPLIE ports set to agree with eNOAD ports"			
#For US_DEPARTURE BAPLIES ############### This is the default setting for running all of this on Departure SP BAPLIES
# bapliePt2a = "\nLOC+5+"+Port.bapArvlPtCd+":139:6'\nLOC+61+"+Port.bapDepPtCode+"'DTM+132:" 		##>>>BAPLIE ports switched with US Departure port as "+@BapArvlPtCd+", and Foreign Arrival port as "+@BapDepPtCode+"-- to make Departure SP Segment."

## DTM+132 = Estimated arrival time - use Date.arrDateJaxBap
bapliePt3 = ":201'DTM+136:"    
## DTM+136 = Departure time - use Date.depDateGerBap 
bapliePt4 = ":201' LOC+147+0420414::5' MEA+WT++KGM:29640' " ## This is actually part of equip01 and may mess up the format if that container is not picked. PLS fix after first good BAPLIE is sent in python.
bapliePt4 = ":201' "  ## Corrected to take first part of CONTAINER 1 out of it
## Example LOcation - B/R/T 52/02/18 = LOC+147+0520218::

######### Equipment from here to ender "UNT"  // This list is synched w BOLA Loads as indicated.
equip01 = "\nLOC+9+DEHAM'\nLOC+11+USJAX'\nLOC+76+ESVLC'\nRFF+BM:MSCUVY766809'\nEQD+CN+OOLU1402250+2210+++5'\nDGS+IMD+2.2+1073+:CEL+1'\nFTX+AAA+++OXYGEN REFRIGERATED'\nNAD+CA+MSC:172:20'"	##  OOLU1402250  Hazmat not T1
equip01 = "\nLOC+147+0420414::5' \nMEA+WT++KGM:29640'\nLOC+9+DEHAM'\nLOC+11+USJAX'\nLOC+76+ESVLC'\nRFF+BM:MSCUVY766809'\nEQD+CN+OOLU1402250+2210+++5'\nDGS+IMD+2.2+1073+:CEL+1'\nFTX+AAA+++OXYGEN REFRIGERATED'\nNAD+CA+MSC:172:20'"	##  OOLU1402250  Hazmat not T1 - CORRECTED

equip02 =	"\nLOC+147+0410502::5'\nMEA+WT++KGM:22485'\nLOC+9+BEANR'\nLOC+11+USJAX'\nLOC+76+RUNVS'\nRFF+BM:MSCURP869036'\nEQD+CN+OOLU1402251+2210+++4'\nDGS+IMD+6.1+1564+07.0:KGM+2+++++6.1'\nFTX+AAA+++Illudium Q-36 Explosive Modulators'\nNAD+CA+MSC:172:20'" ## OOLU1402251 Empty HazmatT1
				
equip03 =	"\nLOC+147+0500314::5'\nMEA+WT++KGM:18820'\nLOC+9+DEHAM'\nLOC+11+BBBGI'\nLOC+76+RULED'\nRFF+BM:MSCURP862692'\nEQD+CN+OOLU1402252+4510+++5'\nNAD+CA+MSC:172:20'"	## OOLU1402252  FROB
				
equip04 =	"\nLOC+147+0060204::5'\nMEA+WT++KGM:23813'\nLOC+9+DEHAM'\nLOC+11+USJAX'\nLOC+76+GBGRG'\nRFF+BM:MSCUU7275425'\nEQD+CN+OOLU1402253+4510+++5'\nNAD+CA+MSC:172:20'" ## OOLU1402253
				
equip05 =	"\nLOC+147+0181584::5'\nMEA+WT++KGM:24047'\nLOC+9+DEHAM'\nLOC+11+USJAX'\nLOC+76+DEBRV'\nRFF+BM:MSCUOJ643367'\nEQD+CN+OOLU1402254+4510+++4'\nNAD+CA+MSC:172:20'"	## OOLU1402254  Empty
				
equip06 =	"\nLOC+147+0070411::5'\nMEA+WT++KGM:23712'\nLOC+9+DEHAM'\nLOC+11+USJAX'\nLOC+76+GBGRG'\nRFF+BM:MSCUU7275425'\nEQD+CN+OOLU1402255+4510+++5'\nNAD+CA+MSC:172:20'" ##  OOLU1402255
				
equip07 =	"\nLOC+147+0070410::5'\nMEA+WT++KGM:23712'\nLOC+9+DEHAM'\nLOC+11+USJAX'\nLOC+76+GBGRG'\nRFF+BM:MSCUU7275425'\nEQD+CN+OOLU1402256+4510+++5'\nNAD+CA+MSC:172:20'" ##  OOLU1402256
				
equip08 =	"\nLOC+147+0040406::5'\nMEA+WT++KGM:22485'\nLOC+9+BEANR'\nLOC+11+USJAX'\nLOC+76+RUNVS'\nRFF+BM:MSCUU7275425'\nEQD+CN+OOLU1402257+4510+++5'\nNAD+CA+MSC:172:20'" ##  OOLU1402257
				
equip09 =	"\nLOC+147+0070406::5'\nMEA+WT++KGM:23813'\nLOC+9+DEHAM'\nLOC+11+USJAX'\nLOC+76+DEBRV'\nRFF+BM:MSCUU7275425'\nEQD+CN+OOLU1402258+4510+++5'\nNAD+CA+MSC:172:20'" ##  OOLU1402258
				
equip10 =	"\nLOC+147+0060305::5'\nMEA+WT++KGM:23813'\nLOC+9+DEHAM'\nLOC+11+USJAX'\nLOC+76+GBGRG'\nRFF+BM:MSCUU7275425'\nEQD+CN+OOLU1402259+4510+++5'\nNAD+CA+MSC:172:20'" ##  OOLU1402259

equip11 =	"\nLOC+147+0180484::5'\nMEA+WT++KGM:24047'\nLOC+9+DEHAM'\nLOC+11+USJAX'\nLOC+76+DEBRV'\nRFF+BM:MSCUOJ643367'\nEQD+CN+MEDU4797256+4510+++4'\nNAD+CA+MSC:172:20'" ##  MEDU4797256 Empty
				
equip12 =	"\nLOC+147+0060207::5'\nMEA+WT++KGM:23813'\nLOC+9+DEHAM'\nLOC+11+USJAX'\nLOC+76+GBGRG'\nRFF+BM:MSCUU7275425'\nEQD+CN+MEDU8341747+4510+++5'\nNAD+CA+MSC:172:20'" ## MEDU8341747
				
equip13 =	"\nLOC+147+0500514::5'\nMEA+WT++KGM:22485'\nLOC+9+BEANR'\nLOC+11+USJAX'\nLOC+76+RUNVS'\nRFF+BM:MSCURP869055'\nEQD+CN+OOLU1402249+4510+++5'\nDGS+IMD+6.1+1564+07.0:KGM+2+++++6.1'\nFTX+AAA+++BORG Cybernetic Nanoprobes'\nNAD+CA+MSC:172:20'"	## OOLU1402249  Full HazmatT1. My BOLA Container. BOLA00
				
equip14 =	"\nLOC+147+0500712::5'\nMEA+WT++KGM:22485'\nLOC+9+BEANR'\nLOC+11+USJAX'\nLOC+76+RUNVS'\nRFF+BM:MSCURP869055'\nEQD+CN+STAR1402666+4510+++5'\nDGS+IMD+6.1+1564+07.0:KGM+2+++++6.1'\nFTX+AAA+++Dwemer parts, Spider or Centurion automatons'\nNAD+CA+MSC:172:20'"	## STAR1402666  Full HazmatT1. My BOLA Container.  was BOLA01				
				
equip15 = "LOC+147+0210208::5'  FTX+AAA+++STP FATTY TUNA'  MEA+VGM++KGM:21912'  LOC+9+DEHAM:139:6'  LOC+11+USASF:139:6'  RFF+BM:1'  EQD+CN+TSAT3326669+22G0+++5'  NAD+CA+TS:172:20'"  ## TSAT3326669

equip16 =	"LOC+147+0210404::5'  FTX+AAA+++STP SUSHI TUNA'  MEA+VGM++KGM:21912'  LOC+9+DEHAM:139:6'  LOC+11+USASF:139:6'  RFF+BM:1'  EQD+CN+TSAT3170510+22G0+++5'  NAD+CA+TS:172:20'"  ## TSAT3170510

equip17 =	"\nLOC+147+0200207::5'\nMEA+WT++KGM:23813'\nLOC+9+DEHAM'\nLOC+11+USJAX'\nLOC+76+GBGRG'\nRFF+BM:MSCUU7275425'\nEQD+CN+OOLU1402342+4510+++5'\nNAD+CA+MSC:172:20'" ##  OOLU1402342   Srini Unified Cargo Manifested

equip18 =	"\nLOC+147+0500514::5'\nMEA+WT++KGM:22485'\nLOC+9+BEANR'\nLOC+11+USJAX'\nLOC+76+RUNVS'\nRFF+BM:MSCURP869055'\nEQD+CN+OOLU1402343+4510+++5'\nDGS+IMD+6.1+1564+07.0:KGM+2+++++6.1'\nFTX+AAA+++Live Samples, Solanum Virus, Human'\nNAD+CA+MSC:172:20'" ##OOLU1402343     ACE Container No. Unified Cargo Manifested HAZMAT

equip19 =	"\nLOC+147+0070207::5'\nMEA+WT++KGM:23813'\nLOC+9+DEHAM'\nLOC+11+USJAX'\nLOC+76+GBGRG'\nRFF+BM:MSCUU7275425'\nEQD+CN+MEAU1502647+4510+++5'\nFTX+AAA+++Tater-Tots,Cheese Curds, and Simulated Emesis, Frozen'\nNAD+CA+MSC:172:20'" ## MEAU1502647  was BOLA02

equip20 =	"\nLOC+147+0080207::5'\nMEA+WT++KGM:23813'\nLOC+9+DEHAM'\nLOC+11+USJAX'\nLOC+76+GBGRG'\nRFF+BM:MSCUU7275425'\nEQD+CN+MEAU1502648+4510+++5'\nFTX+AAA+++Fidget Spinners, Previously Owned'\nNAD+CA+MSC:172:20'" ## MEAU1502648  BOLA03

equip21 =	"\nLOC+147+0460514::5'\nMEA+WT++KGM:23813'\nLOC+9+DEHAM'\nLOC+11+USJAX'\nLOC+76+GBGRG'\nRFF+BM:MSCUU7275425'\nEQD+CN+EGLV1502649+4510+++5'\nNAD+CA+MSC:172:20'" ## EGLV1502649 - Cargo descr intentionally left to BOLA only  Flat Rack Carrier BOLA04

equip22 =	"\nLOC+147+0460512::5'\nMEA+WT++KGM:23813'\nLOC+9+DEHAM'\nLOC+11+USJAX'\nLOC+76+GBGRG'\nRFF+BM:MSCUU7275425'\nEQD+CN+EGLV1502650+4510+++5'\nNAD+CA+MSC:172:20'" ## EGLV1502650 - Cargo descr intentionally left to BOLA only
				
equip23FB = "\nLOC+147+0300314::5'\nMEA+WT++KGM:23813'\nLOC+9+BSNAS'\nLOC+11+USMIA'\nLOC+76+USMIA'\nRFF+BM:MSCUU7275425'\nEQD+CN+EGLV20000000+22P3+++5'\nEQA+CN+EGLV20000001'\nNAD+CA+MSC:172:20'"  ##Flat Rack
equip23FB4 = "\nLOC+147+0300314::5'\nMEA+WT++KGM:23813'\nLOC+9+BSNAS'\nLOC+11+USMIA'\nLOC+76+USMIA'\nRFF+BM:MSCUU7275425'\nEQD+CN+EGLV20000000+22P3+++5'\nEQA+CN+EGLV20000001'\nEQA+CN+EGLV20000002'\nEQA+CN+EGLV20000003'\nEQA+CN+EGLV20000004'\nNAD+CA+MSC:172:20'"  ##Flat Rack w four folded BOLA07
#@equip23FB4 = "\nLOC+147+0300314::5'\nMEA+WT++KGM:23813'\nLOC+9+BSNAS'\nLOC+11+USMIA'\nLOC+76+USMIA'\nRFF+BM:MSCUU7275425'\nEQD+CN+EGLV20000000+22P3+++5'\nEQA+CN+EGLV20000001+CN+EGLV20000002+CN+EGLV20000003+CN+EGLV20000004'\nNAD+CA+MSC:172:20'"

## Add Container w CSM record - AKLU6002431  Example B/R/T 52/02 /18 = LOC+147+0520218
equip24 = "\nLOC+147+0520218::5'\nMEA+WT++KGM:23813'\nLOC+9+BSNAS'\nLOC+11+USMIA'\nLOC+76+GBGRG'\nRFF+BM:MSCUU7275425'\nEQD+CN+AKLU6002431+4510+++5'\nFTX+AAA+++Dog Treats of the Most Delish Sort'\nNAD+CA+MSC:172:20'" ##Container w CSM record - AKLU6002431  

##Stand alone mega load of 3180 containers.
# removed for space. Not needed on this program.

######### Ender
ender = "\nUNT+27561+14840'UNZ+1+14840'"	

## OK KIDS, HERE COMES THE FUN PART....

### ################# ######################  BOLA TESTING  ######################### #################### ######################  ALSO USED FOR REGRESSION TESTING WHERE *EXAM COUNT* UPDATE IS A PORTION OF THE TEST.
##################################################################################################################  REGRESSION w BOLA ALFA 
###	>>> REGRESSION STEP 1 - 3x containers  ***USE THIS FOR DEFAULT STEP 1 OF REGRESSION!!!! (then 22x container below as step 3 (after BOLA)***
message = bapliePt1+Date.timeNowBap+bapliePt2+bapliePt2a+Date.arrDateJaxBap+bapliePt3+Date.depDateGerBap+bapliePt4+equip01+equip02+equip03+ender
bolaLoad = "NONE"


## UPDATE BAPLIES:
### >>> !!! FLAT RACKs DEFAULT STEP 2 of REGRESSION // total of 22 Containers // **ALSO w 2x equip from BOLA - ALFA** and w 1x Flat Rack w 4x stored Flat Racks EGLV SCACs +CSM Container
message = bapliePt1+Date.timeNowBap+bapliePt2+bapliePt2a+Date.arrDateJaxBap+bapliePt3+Date.depDateGerBap+bapliePt4+equip01+equip02+equip03+equip04+equip05+equip06+equip07+equip08+equip09+equip10+equip11+equip12+equip13+equip14+equip21+equip22+equip23FB4+equip24+ender
bolaLoad = "ALFA"	
 """

##################
## 837P Message ##
message = header83701 + submitter + SV101 + ender837



## ALWAYS test print before dropping - also maybe for manual drop.
#DEBUG
print(message)

## The following prints this to a text file.
## TBD- update w TYPE of 837 - P, I, or D.


## The following prints this to a text file (backup of message).
## creates the Messages folder if it doesn't exist before writing.
out_dir = "Messages"
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "Form 837P_message_"+provider+"_01.txt")
with open(out_path, "w", encoding="utf-8") as file:
    file.write("\n" + message)


# THE BIZ LINE:  Sends the Message to MQ  !!! COMMENT OUT WHEN TESTING MSG or GENERATING TEXT
#mqME(message)