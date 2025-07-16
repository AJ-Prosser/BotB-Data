import pandas
import numpy as np
import requests
from tabulate import tabulate



url = "https://battleofthebits.com/api/v1/battle/list/0/5?sort=id&desc=true&filters=type~3"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    table = [[d["cover_art_url"], d["id"], d["start"], d["title"]] for d in data]

    #sanity check
    print(tabulate(table, headers=["Cover Art URL", "ID", "Start", "Title"]))
    #print(data)
else:
    print(f"failed with status code {response.status_code}")