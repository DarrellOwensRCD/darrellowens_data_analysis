import sys

import requests
API_KEY = open("token.txt").read().strip()

def main():
    response = requests.get("gtfsrt/tripupdates/?token=" + API_KEY)
    print(response)
    print(response.status_code)


if __name__ == "__main__":
    main()
