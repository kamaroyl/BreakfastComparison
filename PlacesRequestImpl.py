import requests

"""
    Places Request is a light wrapper around the GCP Places API. It takes a key on construction and makes
    all further queries with that key.
"""


class PlacesRequest:
    def __init__(self, api_key):
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            "X-goog-api-key": api_key
        }

    def get_places(self, query_text):
        body = f'{{"textQuery":"{query_text}"}}'
        print(body)
        result = requests.post('https://places.googleapis.com/v1/places:searchText?fields=*',
                               headers=self.headers,
                               data=body)
        print(result.text)
