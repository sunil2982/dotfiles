from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


def scrape_lifetime_numbers():
  url = "https://lifetimenumber.com/vipmobile-number-filter?start=&end=55&lucky%5B%5D=1&lucky%5B%5D=5&band=&any=37&must=&not=4%2C8&start2="

  with sync_playwright() as p:
    # Launch browser (headless=True runs it in the background)
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    print("Loading page and waiting for content...")
    page.goto(url)

    # Wait until the number articles are rendered on the page
    page.wait_for_selector("article")

    # Get the fully rendered HTML
    html_content = page.content()
    browser.close()

  # Parse HTML with BeautifulSoup
  soup = BeautifulSoup(html_content, "html.parser")

  # Find all product cards (<article> tags)
  articles = soup.find_all("article")
  print(f"Found {len(articles)} items on the page.\n")

  scraped_data = []

  for article in articles:
    # Extract Price
    price_tag = article.find("b")
    price = price_tag.text.strip() if price_tag else "N/A"

    # Extract the Mobile Number parts (usually contained in nested spans/divs)
    # Let's find the text block that makes up the number
    number_div = article.find("div", class_="")
    # Alternatively, extract all text fragments inside the number container
    # Let's grab spans or text inside the card structure
    spans = article.find_all("span")

    # Combine relevant text chunks or look for the specific number formatting
    # Let's extract text elements inside the article carefully:
    text_content = article.get_text(separator=" ", strip=True)

    # Let's filter out or isolate the phone number elements
    # Usually, mobile numbers are 10 digits. Let's find numbers using regex if needed,
    # or extract the specific spans holding the digits.

    scraped_data.append({"price": price, "raw_text": text_content})

  # Print out the extracted results
  for idx, item in enumerate(scraped_data, 1):
    print(f"[{idx}] Price: {item['price']}")
    print(f"    Details: {item['raw_text']}\n")


if __name__ == "__main__":
  scrape_lifetime_numbers()