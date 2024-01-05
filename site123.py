import requests

def check_url_status(url):
    try:
        response = requests.head(url, timeout=10)
        return response.status_code
    except requests.ConnectionError:
        return None  # Connection error, URL is likely dead

def check_bulk_urls_status(file_path):
    try:
        with open(file_path, 'r') as file:
            url_list = [line.strip() for line in file]

        url_status = {}
        for url in url_list:
            status_code = check_url_status(url)
            if status_code is not None:
                url_status[url] = status_code
            else:
                url_status[url] = "Connection Error"

        return url_status
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return {}

# Example usage:
if __name__ == "__main__":
    print("Welcome to URL Status Checker!")
    file_path = input("Hi Sagar ..Please provide the path to the file containing the list of URLs: ")

    result = check_bulk_urls_status(file_path)

    print("\nURL Status:")
    for url, status in result.items():
        print(f"{url}: {status}")
