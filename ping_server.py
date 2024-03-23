import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def ping_server(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Server {url} pinged successfully at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print(f"Server {url} ping failed with status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while pinging the server {url}: {e}")

def main():
    server_url = os.getenv('SERVER_URL')
    if server_url:
        ping_server(server_url)
    else:
        print("SERVER_URL environment variable is not set.")

if __name__ == "__main__":
    main()