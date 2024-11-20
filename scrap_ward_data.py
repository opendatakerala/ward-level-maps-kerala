import requests
import pandas as pd
import json
from pathlib import Path

with open("district_localbody_mapping.json", "r") as f:
    dist_json = json.load(f)

dist_list = []
ward_list = []
link_list = []
for v, k in enumerate(dist_json.items()):
    for j in k[1]:
        dist_list.append(k[0])
        ward_list.append(j["LocalBody"])
        link_list.append(j['HTMLPage'][:-4].replace(" ","%20") + "json")

df = pd.DataFrame({"District" : dist_list,
                    "LocalBody": ward_list,
                    "json_link":link_list})


for num, i in enumerate(df["json_link"]):
    path = Path(df["District"].to_list()[num])
    local_body =  df["LocalBody"].to_list()[num] 
    path.mkdir(parents=True, exist_ok=True)
    res = requests.get(i)
    with open(path / f"{local_body}.json", "w") as file:
        json.dump(res.json(),file, indent = 4)