import requests
import json
import random
import discord
from discord import Webhook, RequestsWebhookAdapter, File
import time
import targetlinkopener
from playsound import playsound
import threading

goodlink = ""#paste your target api link here

#Fill the two strings in the next line with webhook id, webhook token respectively
webhook = Webhook.partial("", "",\
 adapter=RequestsWebhookAdapter())

webhook.send("Hi")


ps5link = "https://www.target.com/p/playstation-5-console/-/A-81114595"
checkoutlink = "https://www.target.com/co-review"

class targetLocation:
    def __init__(self, jsonfile):
        self.locationid = jsonfile["location_id"]
        self.storename = jsonfile["store_name"]
        self.address = jsonfile["store_address"]
        self.availqty = jsonfile["location_available_to_promise_quantity"]
        order = jsonfile["order_pickup"]
        self.orderpickup = order["availability_status"]
        curbside = jsonfile["curbside"]
        self.curbsidepickup = curbside["availability_status"]
        storeship = jsonfile["ship_to_store"]
        self.shiptostore = storeship["availability_status"]
        instore = jsonfile["in_store_only"]
        self.instorestock = instore["availability_status"]
    def printSelf(self):
        print("Store "+self.locationid +" "+self.storename+" at "+self.address)
        print("Promised qty: "+str(self.availqty))
        print("Order pickup: "+self.orderpickup)
        print("Curbside pickup: "+self.curbsidepickup)
        print("Ship to store: "+self.shiptostore)
        print("In store only: "+self.instorestock)
    def sendSelf(self, webhook):
        newstorename = self.storename.replace(" ", "-")
        webhook.send("Store "+self.locationid +" "+self.storename+" at "+self.address+"\n"\
                     "Promised qty: "+str(self.availqty)+"\n"\
                     "Order pickup: "+self.orderpickup+"\n"\
                     "Curbside pickup: "+self.curbsidepickup+"\n"\
                     "Ship to store: "+self.shiptostore+"\n"\
                     "In store only: "+self.instorestock+"\n"\
                     "PS5 Link: <"+ps5link+">\n"\
                     "Checkout Link: <"+checkoutlink+">\n"\
                     "Store link: <https://www.target.com/sl/"+newstorename+"/"+str(self.locationid)+">")
    def data(self):
        return self.locationid, self.storename, self.address, self.availqty, self.orderpickup, self.curbsidepickup, self.shiptostore, self.instorestock


def playalarm0():
    for i in range(5):
        playsound("alarm.mp3")
        playsound("alarm2.mp3")


def playalarmthread():
    t = threading.Thread(target=playalarm0)
    t.start()



def pollTarget():
    responsereceived = False
    while not responsereceived:
        try:
            response = requests.get(goodlink)
            responsereceived = True
        except:
            print("Error accessing target api")
            webhook.send("Error accessing target api")
            time.sleep(.5)
    if response.status_code!=200:
        print("ERROR")
        return -1
    else:
        return response.json()




def interpretTarget():
    jsontext = pollTarget()
    target = jsontext["products"]
    target = target[0]
    target = target["locations"]
    locationobjects = []
    for location in target:
        locationobjects.append(targetLocation(location))
    #for location in locationobjects:
        #location.sendSelf(webhook)
    return locationobjects, jsontext
print("Getting first value")
prevlocdata, prevreading = interpretTarget()
print("Starting loop")
while True:
    interpreted = False
    while not interpreted:
        try:
            currentlocdata, currentreading = interpretTarget()
            interpreted = True
        except:
            print("Error interpreting target api")
    if(currentreading!=prevreading):
        print("STOCK CHANGE")
        webhook.send("@everyone target stock changed!\n"+ps5link+"\n"+checkoutlink)            
        f = open("current"+str(time.time())+".txt", "w")
        f.write(str(currentreading))
        f.close()
        f = open("previous"+str(time.time())+".txt", "w")
        f.write(str(prevreading))
        f.close()
        for i in range(len(currentlocdata)):
            curobj = currentlocdata[i]
            prevobj = prevlocdata[i]
            if curobj.data() != prevobj.data():
                for item in curobj.data():
                    try:
                        if "IN_STOCK" in item:
                            targetlinkopener.open_store(curobj.storename, curobj.locationid)
                            playalarmthread()
                    except:
                        pass
                curobj.sendSelf(webhook)
                webhook.send("Store link "+"https://www.target.com/sl/"+curobj.storename+"/"+str(curobj.locationid))
                curobj.printSelf()
        if "IN_STOCK" in str(currentreading):
            playalarmthread()
    else:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print("no", current_time)
        webhook.send("No Change, checked at "+str(current_time))
    time.sleep(random.random()*2+1)
    prevreading = currentreading
    prevlocdata = currentlocdata

