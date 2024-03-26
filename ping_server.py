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
    server_urls_env = os.getenv('SERVER_URLS')  # Notice the plural in the variable name
    if server_urls_env:
        # Split the SERVER_URLS environment variable by commas (or your chosen delimiter)
        server_urls = server_urls_env.split(',')  
        for url in server_urls:
            ping_server(url.strip())  # Strip whitespace to clean the URLs
    else:
        print("SERVER_URLS environment variable is not set or is empty.")

if __name__ == "__main__":
    main()
