import json
import argparse
import logging
import csv
from fpdf import FPDF



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


#configure PDF view
pdf = FPDF('P', 'mm', 'A4')
WIDTH = pdf.w - 2 * pdf.l_margin
pdf.add_page()
pdf.set_font('Arial', 'B', 18)
pdf.cell(WIDTH, 0.0, 'Service Report', align='C')
pdf.ln(10)
pdf.image("Disk Usage.png", 55, 30, WIDTH/2)
pdf.ln(10)
pdf.set_font('Arial', 'I', 11)
pdf.cell(WIDTH, 0.0, 'Yellow disk will need a clean up soon.Red disk need cleaning ASAP', align='C' )
#pdf.add_page()
pdf.ln(90)
TWIDTH = WIDTH/4

#Read csv 
table = open("Table.csv", "r")
read_file = csv.reader(table)    
    
for s in read_file:

        pdf.cell(5, 5, '', 0, 2, 'C')
        pdf.cell(TWIDTH, 4, str(s[0]), border=1)
        pdf.cell(TWIDTH, 4, s[1], border=1)
        pdf.cell(TWIDTH, 4, s[2], border=1)
        pdf.cell(TWIDTH, 4, s[4], border=1)
        pdf.ln(1)
table.close()        
pdf.output('Service Report.pdf', 'F')





#adding parameters
parser = argparse.ArgumentParser()
parser.add_argument("-f",
                    "--fullreport",
                    help="printing the full report")
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
if args.services:
    service_data(data)
if args.version:
    print_service_version(data)   
if args.diskusage:
    print_service_disk_usages(data)

  