import os
import requests
from datetime import datetime
import pytz
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def ping_server(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Server {url} pinged successfully at {datetime.now(pytz.timezone('Pacific/Auckland')).strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print(f"Server {url} ping failed with status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while pinging the server {url}: {e}")

def is_within_business_hours():
    nz_time = datetime.now(pytz.timezone('Pacific/Auckland'))
    start_hour = 11
    end_hour = 19
    end_minute = 30  # 7:30 PM
    # Check if current time is within business hours
    return start_hour <= nz_time.hour < end_hour or (nz_time.hour == end_hour and nz_time.minute <= end_minute)

def main():
    if is_within_business_hours():
        server_urls_env = os.getenv('SERVER_URLS')  # Notice the plural in the variable name
        if server_urls_env:
            # Split the SERVER_URLS environment variable by commas (or your chosen delimiter)
            server_urls = server_urls_env.split(',')
            for url in server_urls:
                ping_server(url.strip())  # Strip whitespace to clean the URLs
        else:
            print("SERVER_URLS environment variable is not set or is empty.")
    else:
        print("Currently outside business hours in New Zealand. No action taken.")

if __name__ == "__main__":
    main()
