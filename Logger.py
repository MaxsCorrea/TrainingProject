import logging
import json


#set up json file
def get_data():
    with open('services.json') as f:
        data = json.load(f)
        return data
data = get_data()

# Logger configuration
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename= r"C:\Users\Maximiliano\Documents\TrainingProject\Monitoring.log",
                    level= logging.DEBUG, 
                    format=LOG_FORMAT, 
                    filemode='w')
logger = logging.getLogger()

#Messages
logger.debug("Debuggin services...")


for s in data["services"]:
    sr = (s["service"])
    if "stopped" == sr:
        logger.warning(f'Service {s["name"]} service stopped. Bounce needed')
    elif "error" == sr:
        logger.critical(f'Service {s["name"]} service error. Review ASAP')
    elif "running" == sr:
        logger.info(f'Service {s["name"]} service running')    

for s in data["services"]:
    du = float(s["disk usage"][:-1])
    if 50 < du:
     logger.error(f'Service {s["name"]} disk usage {du}% overheated disk')
    elif 40 < du < 50:
     logger.warning(f'Service {s["name"]} disk usage {du}% please check the disk')
    elif 40:
     logger.info(f'Service {s["name"]} disk usage {du}%')


