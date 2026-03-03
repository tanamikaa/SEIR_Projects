import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def main():
    if len(sys.argv) != 2:
        return
    url = sys.argv[1]
    if not url.startswith("http"):
        url = "https://" + url

    options = Options()
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)   # wait up to 10 sec for elements

    try:
        driver.get(url)
        
        # Title
        print(driver.title)

        # Body text
        body = driver.find_element(By.TAG_NAME, "body")
        print(body.text)

        # Links
        links = driver.find_elements(By.TAG_NAME, "a")
        seen = set()

        for link in links:
            href = link.get_attribute("href")
            if href and href not in seen:
                print(href)
                seen.add(href)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
