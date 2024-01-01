import os
import datetime

runtime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
called_file = ""


class Initialize:

    def __init__(self, file):

        global called_file

        self.filename = file
        called_file = self.filename

        # Create the 'logger' directory if it doesn't exist
        os.makedirs('logger', exist_ok=True)

        with open(f'logger/{runtime}.txt', 'a') as file:
            time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file.write(f"[{time}] [{self.filename}] : logger successfully ran\n")
            file.flush()


def log(logs):

    # Create the 'logger' directory if it doesn't exist
    os.makedirs('logger', exist_ok=True)

    with open(f'logger/{runtime}.txt', 'a') as file:
        time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file.write(f"[{time}] [{called_file}] : " + logs + "\n")
        file.flush()
