import json
import argparse
import logging


#argparse config
parser = argparse.ArgumentParser()





#open json data
with open('services.json') as f:
    data = json.load(f)

#reading json data
for service in data["services"]:
    print(service['name'])
    print(service['service'])
    print(service['url'])
    print(service['disk usage'])
 

    if service ['disk usage'] < "50%":
        print("disk is working well")

    else:
        print("overheated disk")   
