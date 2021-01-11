import logging

# Logger configuration
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename= r"C:\Users\Maximiliano\Documents\TrainingProject\Monitoring.log",
                    level= logging.DEBUG, 
                    format=LOG_FORMAT, 
                    filemode='w')
logger = logging.getLogger()

#Messages
logger.debug("Debuggin services...")
logger.info("The service is health")
logger.warning("A service reboot will be good")
logger.error("Some Services are not working correctly")
logger.critical("service DOWN!!!")

