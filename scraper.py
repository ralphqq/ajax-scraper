from datetime import datetime
import json

import pytz
import requests


class Scraper:
    headers = {
        'Host': 'www.pse.com.ph',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.pse.com.ph/stockMarket/home.html',
        'X-Requested-With': 'XMLHttpRequest',
        'DNT': '1',
        'Connection': 'keep-alive'
    }

    def __init__(self):
        self.raw_results = None
        self.index_values = None

    def run(self):
        """Executes the entire scraping workflow."""
        try:
            print('Obtaining values')
            self.scrape()
            print('Processing results')
            self.parse()
            print('Saving data')
            self.save()
            print('Finished')
        except Exception as e:
            print(e)


    def scrape(self):
        """Sends get request and obtains raw JSON response.

        This method stores the de-serialized response body in 
        the variable self.raw_results.
        """

        # Define query parameters
        payload= {
            'method': 'getMarketIndices',
            'ajax': 'true',
            '_dc': self.get_timestamp()
        }

        # Send get request
        r = requests.get(
            url='https://www.pse.com.ph/stockMarket/dailySummary.html',
            params=payload,
            headers=self.headers
        )

        self.raw_results = r.json()


    def parse(self):
        """Extracts relevant data from raw results."""
        self.index_values = self.raw_results.get('records')


    def save(self):
        """Writes parsed data to file."""
        if self.index_values is None:
            raise ValueError('No data to write')

        t = datetime.now()
        fname = f"index-values{t.strftime('%Y%m%d-%H%M%S')}.json"
        with open(fname, 'w') as fp:
            json.dump(self.index_values, fp, indent=3)


    def get_timestamp(self):
        """Gets current timestamp."""
        utc_now = pytz.utc.localize(datetime.utcnow())
        phl_now = utc_now.astimezone(pytz.timezone('Asia/Manila'))
        ts = int(phl_now.timestamp()) * 1000
        return ts


if __name__ == '__main__':
    s = Scraper()
    s.run()
