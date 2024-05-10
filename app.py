from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def fetch_concert_info(info_types):
    url = 'http://localhost:8000/index.html'
    response = requests.get(url)
    results = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        events = soup.find_all('li', class_='event')
        for event in events:
            event_data = {}
            if 'city' in info_types:
                event_data['city'] = event.find('h2').text.strip()
            if 'date' in info_types:
                event_data['date'] = event.find('p', text=lambda x: 'Date' in x).text.replace('Date: ', '').strip()
            if 'price' in info_types:
                event_data['price'] = event.find('p', class_='price').text.replace('Price: ', '').strip()
            results.append(event_data)
    return results

@app.route('/', methods=['GET', 'POST'])
def index():
    data = []
    if request.method == 'POST':
        info_types = request.form.getlist('info_type')
        data = fetch_concert_info(info_types)
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
