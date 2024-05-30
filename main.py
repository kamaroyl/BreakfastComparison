import requests
import csv


def main():
    restaurants = ["Denny's", "Waffle House"]
    for restaurant in restaurants:
        scrape_ratings(restaurant)

def scrape_ratings(name):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    states = [""]



    with open('dennys_ratings.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['State', 'Location', 'Rating'])

        for state in states:
            url = f"https://www.google.com/maps/search/Denny's+in+%7Bstate%7D"
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')

            locations = soup.find_all('div', class='section-result-content')
            for location in locations:
                name = location.find('h3', class='section-result-title').text.strip()
                rating = location.find('span', class='cards-rating-score')
                if rating:
                    rating = rating.text.strip()
                else:
                    rating = 'Not Available'
                writer.writerow([state, name, rating])

            print(f"Finished scraping Denny's in {state}")

    print("Scraping completed. Data saved in dennysratings.csv")


if name == "_main":
    main()
    scrape_dennys_ratings()