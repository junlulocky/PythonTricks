import logging
import os

def set_logger(save_path):
    """
    setup logger
    :param save_path: path to save the log.log file
    :return: logger handler
    """
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    logging.basicConfig(level=logging.INFO, filename=save_path + '/log.log')
    logging.getLogger().addHandler(logging.StreamHandler())

    from time import gmtime, strftime
    curtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    logging.info(curtime)

    return logging

