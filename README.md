
### README.md

```markdown
# Hezarfen Weather Fetcher

Hezarfen Weather Fetcher is a Python application that retrieves METAR, TAF, and GAMET reports from Turkish Meteorological Service (rasat.mgm.gov.tr) and sends them to a Telegram channel. It also retrieves browser headers from a header API to simulate realistic web requests.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-repo/hezarfen-weather-fetcher.git
   cd hezarfen-weather-fetcher
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your API keys:

   ```bash
   TELEGRAM_BOT_KEY=#yourkey
   TELEGRAM_CHAT_ID=#yourkey
   HEADER_API_KEY=#yourkey
   ```

## Usage

1. Run the script:

   ```bash
   python hezarfen.py
   ```

   The script will check the weather reports from the Turkish Meteorological Service every half hour at minute 2 and 31. The retrieved reports will be sent to your configured Telegram channel.

## Configuration

- You can customize the weather stations by modifying the parameters in the `prepare_the_data` function.

- Change the timezone in the constructor to your local timezone using `pytz`.

## Dependencies

- `requests`
- `pytz`

## License

This project is licensed under the MIT License.
```

### Açıklamalar:
- Kod içerisindeki API anahtarlarını ve Telegram bot anahtarlarını "#yourkey" ile değiştirdim.
- README dosyası uygulamanın kurulumu, kullanımı ve konfigürasyonu hakkında bilgi vermektedir.
