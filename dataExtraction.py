import os
import json
import requests
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser(description='get data to post for Instagram')
# command-line arguments
parser.add_argument('--query', help='Query for data', required=True)
parser.add_argument('--location', help='Location', required=True)

# Parses the command-line arguments
args = parser.parse_args()

# Access's and stores the values of command-line arguments
query = args.query
location = args.location


# getName, gets the name of the graph that we are trying to find using the variable "query"
def getName():
    global query

    # prevents errors by replacing spaces given by the user to %20, which is used in URLS
    query = query.replace(' ', '%20')

    response = requests.get(f'https://data.worldbank.org/token-search?q={query}&exclude=&locale=en&maxComposites=100')

    # saves the output to a json format since the website uses a json format to present the data
    output = json.loads(response.text)

    firstValue = 0
    ID = ''

    for item in output:
        for element in item:

            # variables used to save each type of data we would want.

            matched_on = element["matchedOn"]
            value = element["value"]
            label = element["label"]
            category = element["category"]
            # Extract more fields as needed

            # Process the extracted data
            # print(f"Matched On: {matched_on}")
            # print(f"Value: {value}")
            # print(f"Label: {label}")
            # print(f"Category: {category}")
            if firstValue == 0:
                ID = str(value)

                firstValue = 1

            else:
                pass
    return ID


# getData uses the variable "location" and method "getName" to get the data
# that we will need in order to graph what the user is trying to look for.
def getSuggestedQuery():
    global query
    response = requests.get(f'https://data.worldbank.org/token-search?q={query}&exclude=&locale=en&maxComposites=100')
    querys = json.loads(response.text)

    suggestedNames = []

    try:
        for item in querys:
            for label in item:
                name = label.get("label")

                if name:
                    suggestedNames.append(name)

    except IndexError:
        pass

    for labels in suggestedNames:
        print(labels)


def getData():
    try:

        global location

        # sends the request with the needed query's
        response = requests.get(f'https://api.worldbank.org/v2/country/{location}/indicator/{getName()}')

        # saves the
        with open('output.xml', 'w') as file:
            file.write(response.text)
            file.flush()

        tree = ET.parse("output.xml")
        root = tree.getroot()

        # Define the namespace prefix
        namespace = {"wb": "http://www.worldbank.org"}

        # Iterate over 'wb:data' elements

        dates = []
        values = []
        indicatorValue = 0
        indicator = ""
        countryValue = 0
        country = ''
        title = ''
        done = False
        for data_element in root.findall(".//wb:data", namespace):
            # Extract required data
            indicator_id = data_element.find("wb:indicator", namespace).attrib["id"]
            if not done:
                title = str(data_element.find("wb:indicator", namespace).text)
                print(f'found graph: {title}')
                done = True

            country_id = data_element.find("wb:country", namespace).attrib["id"]
            country_name = data_element.find("wb:country", namespace).text

            if countryValue == 0:
                country = str(country_name)
                countryValue = 1

            date = data_element.find("wb:date", namespace).text
            value = data_element.find("wb:value", namespace).text

            # Process the extracted data as needed
            # print(f"Indicator ID: {indicator_id}")
            # print(f"Country ID: {country_id}")
            # print(f"Country Name: {country_name}")
            # print(f"Date: {date}")
            # Process the extracted data as needed
            dates.append(str(date))
            values.append(str(value))
            # print(f"Value: {value}")

        # Convert values to numeric format
        values = pd.to_numeric(values, errors='coerce')  # 'coerce' will replace "None" with NaN

        # Create a DataFrame from the data
        df = pd.DataFrame({"Date": dates, "Value": values})

        # Convert the "Date" column to datetime type
        df["Date"] = pd.to_datetime(df["Date"])

        # Set the "Date" column as the DataFrame index
        df.set_index("Date", inplace=True)

        # Plot the graph using Pandas plot function
        fig, ax = plt.subplots(figsize=(10, 6))  # Adjust figure size as needed

        # Calculate the maximum width and height for the title
        max_width = fig.get_figwidth() * 0.7  # 70% of the figure width
        max_height = fig.get_figheight() * 0.1  # 10% of the figure height

        # Reduce font size iteratively until the title fits within the image dimensions
        title_font_size = 20  # Starting font size for the title
        min_font_size = 10  # Minimum font size to avoid excessive reduction
        max_font_size = 20  # Maximum font size to avoid too much enlargement
        while True:
            title_font = {'fontsize': title_font_size}
            ax.set_title(f"{title}  LOCATION: {country}", fontdict=title_font)
            fig.canvas.draw()

            # Gets the width and height of the title text in pixels
            # which is then used to check whether the font size is too big
            title_width, title_height = ax.title.get_window_extent(renderer=fig.canvas.get_renderer()).size

            if title_width <= max_width and title_height <= max_height or title_font_size <= min_font_size:
                break

            # Reduces the font size for the title if it's too large (makes it look better)
            if title_font_size > max_font_size:
                title_font_size = max_font_size
            else:
                # Reduces the font size for the title by 1
                title_font_size -= 1

        # Grabs the last value and date
        last_value = values[0]
        last_date = pd.to_datetime(dates[0])

        # Annotate the last value on the y line
        plt.annotate(f"Current Value: {last_value:.2f}", xy=(last_date, last_value), xytext=(-150, 15),
                     textcoords='offset points', arrowprops=dict(arrowstyle="->"))

        # Annotates the date on the x line
        plt.annotate(f"Date: {last_date.strftime('%Y-%m-%d')}", xy=(last_date, last_value), xytext=(-150, -15),
                     textcoords='offset points')

        # Plots the graph
        df.plot(kind="line", marker='o', xlabel="Date", ylabel="Value", ax=ax)

        # Saves the graph as a PNG image to be used for instagram
        fig.savefig("graph.png")

        with open("caption.txt", 'w') as file:
            file.write(title + f" in {country}!")
            file.flush()

        # Print a message confirming the graph has been saved
        print("graph saved")

    except IndexError as error:

        print("graph not found / does not exist")
        print("perhaps your trying to find this?")
        getSuggestedQuery()


if __name__ == '__main__':
    getData()
    os.system(f"""python instagram.py""")
