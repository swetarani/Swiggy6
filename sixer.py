import requests
import sys
import time

while(True):
    url = "https://www.cricbuzz.com/match-api/livematches.json"
    r = requests.get(url)
    data = r.json()

    match = data["matches"]
    ipl_index = 0

    for id in match:
        if (match[id]["series"]["short_name"] == "IPL 2019"):
            ipl_index = id
            break

    temp = match[ipl_index]["score"]["prev_overs"]
    temp = temp.split(" ")

    for k in range(len(temp) - 3, len(temp)):
        if(temp[k] == "6"):
            print("SWIGGY SIXER")
            print('\a')
    time.sleep(30)
