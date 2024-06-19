"""Example script."""

from os import environ as ENV

from dotenv import load_dotenv
import requests as req



if __name__ == "__main__":

    load_dotenv()

    response = req.get(f"{ENV['API_URL']}?key={ENV['API_KEY']}&name={ENV['NAME']}&exact=true")
    data = response.json()

    if response.status_code == 200 and isinstance(data, list):
        name = data[0]
        print(f"Name: {name['name']}")
        print(f"Gender: {name['gender'].upper() if len(name['gender']) == 1 else "M/F"}")
        print(f"Languages: {', '.join(set([u['usage_full'] for u in name['usages']]))}")
    else:
        print("Unable to access the API; please try again later.")
