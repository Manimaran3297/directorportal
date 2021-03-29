import logging

def test_logging():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log') #file name
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)   #filehandler object
    #set level is core concepts.it start to print from setting level

    logger.setLevel(logging.DEBUG)
    logger.debug("A debug statement is executed")
    logger.info("information statement")
    logger.warning("warning mode")
    logger.error("error is occured")
    logger.critical("issue is critical")