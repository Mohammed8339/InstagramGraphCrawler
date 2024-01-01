import datetime
import os
import argparse

parser = argparse.ArgumentParser(description='main file which will run the needed files in proper order')
parser.add_argument('--query', help='Query for data', required=True)
parser.add_argument('--location', help='Location', required=True)


if __name__ == '__main__':

    print(datetime.date)

    # args = parser.parse_args()
    # query = args.query
    # location = args.location
    #
    # os.system(f"""python dataExtraction.py --query "{query}" --location {location}""")
