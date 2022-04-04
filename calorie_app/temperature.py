import requests
from selectorlib import Extractor


class Temperature():
    """Web-scrapes the current temperauture of a city from the parameters 
    inputted"""

    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"
     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} 

    base_url = "https://www.timeanddate.com/weather/"
    yml_path = "calorie_app/temperature.yaml"

    def __init__(self, country, city):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def _build_url(self):
        """Build the url string"""

        return(self.base_url + self.country + "/" + self.city)

    def _scrape(self):
        """Extracts a value as instructed by the yml file and returns a 
        dictionary"""
        extractor = Extractor.from_yaml_file(self.yml_path)
        url = self._build_url()

        r = requests.get(url, headers=self.headers)
        content = r.text

        raw_result = extractor.extract(content)
        return(raw_result)
        
        

    def get(self):
        """Cleans output of the scrape"""
        scraped_content = self._scrape()
        return( float(scraped_content['temp'].replace('\xa0°C', '')))
        
