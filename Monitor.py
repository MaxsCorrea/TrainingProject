import json
import logging




#open json data
with open('services.json') as f:
    data = json.load(f)

#reading json data
for service in data["services"]:
    print(service['name'], 
    service['service'],
    service['disk usage']) 

    if service ['disk usage'] < "50%":
        print("disk is working well")

    else:
        print("overheated disk")   
