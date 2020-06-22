import yaml
import requests
import re


def mon_num(value):
    if value == "Jan":
        return "01"
    if value == "Feb":
        return "02"
    if value == "Mar":
        return "03"
    if value == "Apr":
        return "04"
    if value == "May":
        return "05"
    if value == "Jun":
        return "06"
    if value == "Jul":
        return "07"
    if value == "Aug":
        return "08"
    if value == "Sep":
        return "09"
    if value == "Oct":
        return "10"
    if value == "Nov":
        return "11"
    if value == "Dec":
        return "12"


def flat_date(value):
    value = value.split()[0]
    if re.match(r"^\d{1,2}\/\d{1,2}\/\d{4}$", value):
        return value
    else:
        value = value.split("-")
        return value[0] + "/" + mon_num(value[1]) + "/20" + value[2]


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
        print(flat_date(ele["date"]) + " -> " + ele["tt"])

for ele in data_1["tested"]:
    print(
        flat_date(ele["updatetimestamp"])
        + " -> "
        + ele["samplereportedtoday"]
        + " -> "
        + ele["totalsamplestested"]
    )
