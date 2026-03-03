import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def fetch_page(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text

def main():
    if len(sys.argv) != 2:
        print("Usage: python scraper.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    try:
        html = fetch_page(url)
    except Exception as e:
        print("Error fetching page:")
        print(e)
        sys.exit(1)

    soup = BeautifulSoup(html, "html.parser")

    # Remove scripts and styles
    for tag in soup(["script", "style"]):
        tag.decompose()

    # Title
    title = ""
    if soup.title and soup.title.string:
        title = soup.title.string.strip()
    print(title)

    # Body text
    body = soup.body
    if body:
        body_text = body.get_text(separator=" ")
        body_text = " ".join(body_text.split())
    else:
        body_text = ""
    print(body_text)

    # links (one per line)
    for link in soup.find_all("a", href=True):
        full_url = urljoin(url, link["href"])
        print(full_url)

if __name__ == "__main__":
    main()