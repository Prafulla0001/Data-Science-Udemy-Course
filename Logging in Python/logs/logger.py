import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    force = True,
    filename = 'app.log',
    filemode = 'w'
)