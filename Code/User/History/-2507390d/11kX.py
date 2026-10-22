from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


def scrape_and_save():
  url = "https://lifetimenumber.com/vipmobile-number-filter?start=&end=55&lucky%5B%5D=5&any=37&must=&not=4%2C8&total%5B%5D=10&total%5B%5D=15&total%5B%5D=37&total%5B%5D=50&total%5B%5D=51&total%5B%5D=55&total%5B%5D=60"

  with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    print("Loading page and waiting for content...")
    page.goto(url)
    page.wait_for_selector("article")

    html_content = page.content()
    browser.close()

  soup = BeautifulSoup(html_content, "html.parser")
  articles = soup.find_all("article")
  print(f"Found {len(articles)} items. Saving to file...\n")

  # Open a text file in write mode ('w') with UTF-8 encoding
  filename = "scraped_numbers.txt"
  with open(filename, "w", encoding="utf-8") as file:
    file.write("--- VIP MOBILE NUMBERS SCRAPED DATA ---\n\n")

    for idx, article in enumerate(articles, 1):
      # Extract Price
      price_tag = article.find("b")
      price = price_tag.text.strip() if price_tag else "N/A"

      # Get clean text content of the article
      text_content = article.get_text(separator=" ", strip=True)

      # Format the entry for the text file
      entry = f"[{idx}] Price: {price}\n    Details: {text_content}\n\n"

      # Write each entry into the file
      file.write(entry)

  print(f"Successfully saved all data to '{filename}'!")


if __name__ == "__main__":
  scrape_and_save()