# TrainingProject
this is a training project.
important to read de documentation before to edit or use the code.


Reporting app Documentation

Useful links: https://github.com/MaxsCorrea/TrainingProject (app repository)
                      https://www.python.org/downloads/ (python download)


Pre-Requisites: 
1.	you will need to clone the Reporting app repo 
2.	install Python3 and pip
3.	install pandas, plotly and fpdf
4.	install Ansible
                       

Clone or Download the repository 
In terminal:
 $ git clone https://github.com/MaxsCorrea/TrainingProject
     
centOS/Fedora/RHEL
Sudo dnf install -y gcc python3-devel

macOS
$ brew install python3

* If you are using a windows machine in the useful link section at the biggening of the documentation you will find the link to download python3. The latest python version comes with pip setting up to install for default but, if after installing python you cannot run pip just go to the terminal using the PATH where you install python and type:
C:\PythonXY\python.exe get-pip.py
Install pandas and plotly
pip install pandas
pip install plotly==4.14.3
pip install fpdf

Running the program:
open the terminal and go to the python path and repository path.
C:/Users/Maximiliano/AppData/Local/Programs/Python/Python39/python.exe c:/Users/Maximiliano/Documents/TrainingProject/Monitor.py
*you can replace Monitor.py for Logger.py or Graphreport.py according on how you want to see the reports.
Running Logger.py
C:/Users/Maximiliano/AppData/Local/Programs/Python/Python39/python.exe c:/Users/Maximiliano/Documents/TrainingProject/Logger.py
This will generate a log file in the local repository.

Running Graphreport.py
C:/Users/Maximiliano/AppData/Local/Programs/Python/Python39/python.exe c:/Users/Maximiliano/Documents/TrainingProject/Graphreport.py
This will generate a graphic in the local repository and will save the data frame table in to a csv file to be used for the Monitor.py pdf report.


Parameters to Monitor.py:

Parameter	Description	help
 -f	fullreport	Prints a full report on the terminal
 -s	services	prints all serivces in terminal
 -d	disk usage	prints all disk usage in terminal
 -v	version	pritns all versions services in terminal

Example to run the Monitor.py
C:/Users/Maximiliano/AppData/Local/Programs/Python/Python39/python.exe c:/Users/Maximiliano/Documents/TrainingProject/Monitor.py -s services -d diskusage 

This will show the services and disk usage only.

Generating the PDF report

Previous steps to be done: 
run the GraphReport to get the most recent graphic and to save the latest table of the services performance.
Run the Monitor app and check the local repository for the Service Report.pdf
*remember pushing the latest report to master to have up to date every shift.

Common errors running the app

Generating another pdf report with the last one open:
    f=open(name,'wb')
PermissionError: [Errno 13] Permission denied: 'Service Report.pdf'

Generating another pdf report with the excel table open:

ValueError: I/O operation on closed file.
