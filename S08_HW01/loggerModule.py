import logging
 
module_logger = logging.getLogger("phoneBook.loggerModule")
 
def add(x, y):
    logger = logging.getLogger("phoneBook.loggerModule.add")
    logger.info("added %s and %s to get %s" % (x, y, x+y))
    return x+y