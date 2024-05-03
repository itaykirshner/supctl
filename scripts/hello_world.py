# {"name": "hello_world", "version": 0.1}

import sys
sys.path.append("..")

def hello_world(*args, **kwargs):
    from common.create_logger import create_logger
  
    logger = create_logger("hello_world")
    main(logger)


def main(logger, *args, **kwargs):
    logger.info("Hello World!")
