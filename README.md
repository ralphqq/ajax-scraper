# ajax-scraper
This is a basic scraper built with requests that demonstrates how to replicate Ajax calls on the [PSE website homepage](https://www.pse.com.ph/stockMarket/home.html). The idea for this scraper was also used in a [previous project](https://github.com/ralphqq/pse-indices-scoreboard).

## Raw JSON Response Content
Here's a snippet of the raw JSON response body:
```
{
   "count": 8,
   "records": [
      {
         "percentageChange": -2.413,
         "changeIndicator": "D",
         "indexId": "PSE_MKTIN20080000001",
         "sortOrder": 2,
         "indexName": "All Shares",
         "class": "class ph.com.headway.dto.MarketIndexRecord",
         "changeValue": -115.46,
         "marketStatus": "OPEN",
         "indexPoints": 4668.65
      },
      {
         "percentageChange": -2.7289999999999996,
         "changeIndicator": "D",
         "indexId": "PSE_MKTIN20080000002",
         "sortOrder": 1,
         "indexName": "PSEi",
         "class": "class ph.com.headway.dto.MarketIndexRecord",
         "changeValue": -214.36,
         "marketStatus": "OPEN",
         "indexPoints": 7640.03
      },

      ...

      {
         "percentageChange": -1.951,
         "changeIndicator": "D",
         "indexId": "PSE_MKTIN20080000006",
         "sortOrder": 6,
         "indexName": "Services",
         "class": "class ph.com.headway.dto.MarketIndexRecord",
         "changeValue": -31.05,
         "marketStatus": "OPEN",
         "indexPoints": 1560.54
      }
   ]
}
```

## Output
Based on the above, the relevant data to be parsed are found under the `'records'` key. The script dumps the contents of `'records'` into a JSON file saved in the root project directory.

## Running the Script
Make sure dependencies have been installed in a virtual environment and activated.
```
$ python scrape.py
```

## License
[MIT license](https://opensource.org/licenses/MIT)