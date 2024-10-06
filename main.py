import json
import requests
import pytz
from datetime import datetime

class Hezarfen:
    def __init__(self):
        """rasat web site constructors"""
        self.base_url = "https://rasat.mgm.gov.tr/_next/data/YOyqyeAQbN_jNwF3Uc3QG/result.json?"
        self.url_obs_types = "&obsType=1&obsType=2&obsType=3&hours=0"

        """api key constructors"""
        self._api_key = "#yourkey"
        self._api_url = 'https://headers.scrapeops.io/v1/browser-headers'

        """Json and backend data"""
        self.size_of_param = None
        self.searched_airfields = None

        """telegram bot base url"""
        self.telegram_bot = "https://api.telegram.org/bot#yourkey/sendMessage?chat_id=#yourkey&text="

        """Configurations"""
        self.last_metar_report = ""
        self.local_time = pytz.timezone("Europe/Istanbul")
        self.accept = True

    def get_browser_headers(self):
        """This function get a browser header randomly from an api"""
        try:
            browser_head_request = requests.get(self._api_url,
                                                params={"api_key": self._api_key,
                                                        "num_results": 1})
            return browser_head_request.json()["result"][0]

        except:
            return "Script Başlığı Oluşturulamadı"

    def prepare_the_data(self, *args) -> str:
        """This function creates the data"""
        argument_list = [f"&stations={i}" if args.index(i) != 0 else f"stations={i}" for i in args]
        self.size_of_param = len(argument_list)
        self.searched_airfields = [*args]
        argument_list = "".join(argument_list)

        # compile
        return self.base_url + argument_list + self.url_obs_types

    @staticmethod
    def decoder(json_file, metar_size):
        """This function decodes the given json file according to metar taf report"""
        metars = []
        for x in range(metar_size):
            first_stage = json_file["pageProps"]["response"][x]
            second_stage = first_stage["dataLast"]

            metars.append([i["observationText"] for i in second_stage])

        return metars

    def get_json_file(self, request_url: str):
        """This function generate the headers and sends request to rasat website"""
        header = self.get_browser_headers()

        try:
            get_request = requests.get(request_url, headers=header, timeout=(6, 30))

            if get_request.status_code == 200:
                return json.dumps([self.decoder(get_request.json(), self.size_of_param), self.searched_airfields])

        except requests.exceptions.HTTPError:
            return "Hezarfen Sitesine Ulaşılamadı!"

    def run_up_program(self):
        # get now
        valid_time = datetime.now(self.local_time)

        if valid_time.minute == 2 or valid_time.minute == 31:
            data_for_report = self.prepare_the_data("LTAB")
            results_for_report = self.get_json_file(data_for_report)

            for i in json.loads(results_for_report)[0]:
                for x in i:
                    metar_taf_gamet__text = ""
                    if x.strip().startswith("METAR"):

                        if x.strip() != self.last_metar_report:
                            metar_taf_gamet__text += x.strip()
                            metar_taf_gamet__text += "\n"
                            metar_taf_gamet__text += "-" * 50

                            self.last_metar_report = x.strip()
                            self.accept = True

                        else:
                            self.accept = False

                    if x.strip().startswith("TAF") and self.accept:
                        metar_taf_gamet__text += "\nTAF RAPORU\n"
                        metar_taf_gamet__text += x.strip() + "\n"
                        metar_taf_gamet__text += "-" * 50


                    if x.strip().startswith("VALID") and self.accept:
                        metar_taf_gamet__text += "\nGAMET\n"
                        metar_taf_gamet__text += x.strip()

                    if self.accept:
                        metar_report_to_telegram = c.telegram_bot + metar_taf_gamet__text
                        requests.get(metar_report_to_telegram)

# create the class
c = Hezarfen()
while True:
    c.run_up_program()
```
