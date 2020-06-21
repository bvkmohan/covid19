import yaml
import requests

with open("config.yaml", "r") as config_yaml:
    try:
        config = yaml.safe_load(config_yaml)
    except yaml.YAMLError as yaml_err:
        print(yaml_err)

data_1 = requests.get(config["data_1"])
data_2 = requests.get(config["data_2"])

if data_1.status_code == 200 and data_2.status_code == 200:
    data_1 = data_1.json()
    data_2 = data_2.json()
else:
    print("Data 1 Load Error, HTTP : " + str(data_1.status_code))
    print("Data 2 Load Error, HTTP : " + str(data_2.status_code))

for ele in data_2["states_daily"]:
    if ele["status"] == "Confirmed":
        print(ele["date"] + " -> " + ele["tt"])

for ele in data_1["tested"]:
    print(
        ele["updatetimestamp"]
        + " -> "
        + ele["samplereportedtoday"]
        + " -> "
        + ele["totalsamplestested"]
    )
