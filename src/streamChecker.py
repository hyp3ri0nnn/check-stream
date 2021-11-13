#!python 

from datetime import date, datetime
import requests
from bs4 import BeautifulSoup
from datetime import datetime



#send request the telegram page.
#take the last posts date. 
#compare it with now.
#
gunhan = "https://t.me/s/mertgunhan"
cs = "https://t.me/s/csnaber"
tancan = "https://t.me/s/tancanfumentwitch"
streamList = [gunhan,cs,tancan]
now = datetime.now()
today = now.day

class CheckStream:

    def __init__(self):
        self.start = True

    def checkStream(self):
        for s in streamList:
            req  = requests.get(s)
            
            page = BeautifulSoup(req.text,"html.parser")

            dates = page.find_all(class_="time")

            streamDate = dates[-1]["datetime"]
            date_format = datetime.fromisoformat(streamDate)
            streamDateDay = date_format.day
            

            if streamDateDay == today: 
                print(f"{s[15:]} is on stream check more from here -> {req.url}") 
            
            else:

                if streamDateDay  == today -1 and 3 >= now.hour >= 0 :
                    print(f"{s[15:]}'s stream may continue check for details from here: -> {req.url}") 
                else: 
                    print(f"{s[15:]} is not Streaming")


if __name__ == "__main__":
    
    stream = CheckStream()
    stream.checkStream()
    while True:
        print("q to quit")
        print("r to refresh")
        button = input()
        if button == "q":
            break
        if button == "r":
            stream.checkStream()

# print(dates[-1].find_all("datetime"))
# for i in dates[-1]:
#     print(i)
