import json
import argparse
import logging


#set up json file
def get_data():
    with open('services.json') as f:
        data = json.load(f)
        return data

data = get_data()

def service_data(p):
    print('Services:')

    for service in p['services']:
        print(f'{service["name"]}:\t{service["service"]}')

def print_service_disk_usages(data):
    print('Disk Usage:')

    for service in data['services']:
        print(f'{service["name"]}:\t{service["disk usage"]}')

def print_service_version(data):
    print('Version:')

    for service in data['services']:
        print(service['name'],":", service['version'])

def service_url(data):
    print('Url:')

    for service in data['services']:
        print(service['name'],":", service['url'])




#adding parameters
parser = argparse.ArgumentParser()
parser.add_argument("-f",
                    "--fullreport",
                    help="printing the full report")
parser.add_argument("-g",
                    "--graphreport",
                    help="printing the graph report")
parser.add_argument("-s",
                    "--services",
                    help="services to be test")
parser.add_argument("-d",
                    "--diskusage",
                    help="see the disk usage")
parser.add_argument("-v",
                    "--version",
                    help="service version")                    
args = parser.parse_args()

if args.fullreport:
    service_data(data)
    print_service_version(data)
    service_url(data)
    print_service_disk_usages(data)    
if args.graphreport:
    print("Añadir funcionalidad")
if args.services:
    service_data(data)
if args.version:
    print_service_version(data)   
if args.diskusage:
    print_service_disk_usages(data)

  