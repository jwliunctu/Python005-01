import logging
def timelog():
    filename='./timelog.log'
    FORMAT = '%(asctime)-15s %(message)s'
    logging.basicConfig(
        filename=filename,
        level=logging.INFO,
        format=FORMAT)
    logging.info('timelog triggered')

timelog()
