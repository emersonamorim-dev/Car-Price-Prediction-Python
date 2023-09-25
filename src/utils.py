import requests
import logging

def fetch_data_from_api(url):
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        logging.error(f"Error fetching data from API: {e}")
        return None
