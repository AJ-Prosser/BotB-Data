import pandas
import numpy as np
import requests
from tabulate import tabulate
import sqlite3
import json
import time


base_url = "https://battleofthebits.com/api/v1/battle/list"
page_size = 500
page = 0
allXHBs = []
tries = 0

while page<50:
    print(f"retrieving page {page} (of estimated {11000/500})")
    if tries > 5:
        exit()
    url = f"{base_url}/{page}/{page_size}?sort=id&desc=true&filters=type~3"
    response = requests.get(url)

    if response.status_code != 200:
        print("failed with response code " + str(response.status_code))
        time.sleep(3)
        tries += 1
        break
    data = response.json()

    if not data:
        break
    
    allXHBs.extend(data)
    page += 1

with open("all_XHBs.json", "w", encoding="utf-8") as f:
    json.dump(allXHBs, f, indent=2, ensure_ascii=False)

    #table = [[d["cover_art_url"], d["id"], d["start"], d["title"]] for d in data]

    #sanity check
    #print(tabulate(table, headers=["Cover Art URL", "ID", "Start", "Title"]))
    #print(data)