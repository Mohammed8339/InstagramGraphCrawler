import os
import json
import requests


def getSuggestedQuery(query):
    query = query.replace(' ', '%20')

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

    if len(suggestedNames) != 0:
        print()
        for labels in suggestedNames:
            print(labels)
        print()
        os.system('pause')

    else:
        print("no suggestions found")
        os.system('pause')


if __name__ == '__main__':
    print("what graph are you looking for")
    querys = input()
    getSuggestedQuery(querys)
