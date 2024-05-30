import PlacesRequestImpl
import os


def main():
    api_key = os.getenv('GCP_API_KEY')
    client = PlacesRequestImpl.PlacesRequest(api_key)
    restaurants = ["Denny's"]
    for restaurant in restaurants:
        scrape_ratings(restaurant, client)


def scrape_ratings(restaurant_name, client):
    states = ['CO']
    for state in states:
        template = f"{restaurant_name} in {state}"
        client.get_places(template)


if __name__ == "__main__":
    main()
