import requests
from bs4 import BeautifulSoup

def fetch_concert_info(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        events = soup.find_all('li', class_='event')

        concert_info = []
        for event in events:
            city = event.find('h2').text.strip()
            date = event.find('p', text=lambda x: x and 'Date' in x).text.replace('Date: ', '').strip()
            price = event.find('p', class_='price').text.replace('Price: ', '').strip()

            concert_info.append({
                'city': city,
                'date': date,
                'price': price
            })
        return concert_info
    else:
        return "Failed to fetch data. Status Code: {}".format(response.status_code)

url = 'http://localhost:8000/index.html'
concert_data = fetch_concert_info(url)
print(concert_data)
