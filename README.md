# Email Scraper

## Overview

This Python script is a simple email scraper that extracts email addresses from a given URL and displays them in the console. It uses the `requests` library to fetch the HTML content of the provided URL and the `re` module for regular expression matching to extract email addresses.

## Usage

To use this script, follow these steps:

1. Save the script to a Python file (e.g., `email_scraper.py`).

2. Install the `requests` library if you haven't already:

   ```bash
   pip install requests
   ```

3. Run the script with the URL as a command-line argument:

   ```bash
   python email_scraper.py <URL>
   ```

   Replace `<URL>` with the URL you want to scrape email addresses from.

4. The script will fetch the HTML content of the provided URL, extract email addresses, and display them in the console.

## Example

```bash
python email_scraper.py https://example.com
```

## Dependencies

- Python 3.x
- `requests` library

## Disclaimer

Please use this script responsibly and ensure that you have the right to scrape the website in question. Disabling SSL certificate verification (`verify=False`) can expose you to security risks, so exercise caution and consider the implications before using it.

The authors and contributors of this script are not responsible for any misuse or legal consequences that may arise from its use.

## License

This script is open-source software licensed under the [MIT License] Feel free to use, modify, and distribute it as per the terms of the license.

---

Happy Email Scraping! 📧✨
```
