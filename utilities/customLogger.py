import os
import logging
import inspect


class LogGen:

    @staticmethod
    def loggen():
        # Create a log directory if it doesn't exist
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)

        # Get the name of the calling script (without extension)
        caller_name = inspect.stack()[1].filename
        script_name = os.path.splitext(os.path.basename(caller_name))[0]

        # Only configure logging for files ending with '_test.py'
        if script_name.endswith('_test'):
            log_file = os.path.join(log_dir, f"{script_name}.txt")
            logger = logging.getLogger(script_name)
            logger.setLevel(logging.INFO)

            formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
            file_handler = logging.FileHandler(log_file, mode='w')
            file_handler.setLevel(logging.INFO)
            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            return logger
        else:
            return logging.getLogger(script_name)
