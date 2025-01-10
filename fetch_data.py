import requests

def fetch_website_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Data fetched from {url}")
            return response.text
        else:
            print(f"Failed to fetch data: {response.status_code}")
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    url = "https://webbook.radianterp.in/"  # Modify this URL as needed
    data = fetch_website_data(url)
    # Process or save the fetched data as needed

if __name__ == "__main__":
    main()
