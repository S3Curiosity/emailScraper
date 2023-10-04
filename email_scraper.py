import sys
import requests
import re

def extract_emails_from_url(url):
    try:
        # Disable SSL certificate verification
        response = requests.get(url, verify=False)
        response.raise_for_status()

        # Use regular expression to find email addresses in the HTML content
        emails = re.findall(r'\S+@\S+', response.text)

        return emails
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching the URL: {}".format(e))
        return []
    except Exception as e:
        print("An unexpected error occurred: {}".format(e))
        return []

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python email_scraper.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    # Extract and print the email addresses
    emails = extract_emails_from_url(url)

    if emails:
        print("\nExtracted email addresses:")
        for email in emails:
            print(email)
    else:
        print("No email addresses found on the provided URL.")
