import yaml
import requests

with open("config.yaml", "r") as config_yaml:
    try:
        config = yaml.safe_load(config_yaml)
    except yaml.YAMLError as yaml_err:
        print(yaml_err)

data_1 = requests.get(config["data_1"])

if data_1.status_code == 200:
    data_1 = data_1.json()
else:
    print("Data Load Error, HTTP : " + str(data_1.status_code))

print(data_1)
