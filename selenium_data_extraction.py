from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import fitz  # PyMuPDF
from io import BytesIO
import urllib.parse


def get_file_name_from_url(url):
    """Generate a clean, valid file name from the URL."""
    base_name = urllib.parse.urlparse(url).netloc  # Get the domain name from URL
    path = urllib.parse.urlparse(url).path  # Get the path from the URL
    file_name = base_name + path.replace("/", "_") + ".txt"  # Convert path into a valid file name
    return file_name

#Extracting content from webpages
def selenium_webscrap(url):
    """Scrape text from a webpage using Selenium."""
    file_name = get_file_name_from_url(url)
    with open(file_name, "w", encoding="utf-8") as f:
        driver = webdriver.Chrome()
        driver.get(url)

        try:
            # Wait for the page to load and elements to be present
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "div")))

            # Find elements again inside the loop to avoid stale element exception
            paragraphs = driver.find_elements(By.TAG_NAME, "div")
            for p in paragraphs:
                f.write(p.text + "\n")  # Append newline for readability

        except Exception as e:
            print(f"Error scraping {url}: {e}")

        finally:
            driver.quit()  # Ensure the browser is closed

#Extracting urls from the file
def url_extract(file):
    """Extract URLs from a text file."""
    with open(file, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f.readlines() if line.strip()]
    return urls

#Extract content from pdf files
def pdf_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        doc = fitz.open(stream=BytesIO(response.content), filetype="pdf")
        text = "\n".join([page.get_text() for page in doc])

        #print("Extracted PDF Text:\n", text[:500])  # Print first 500 characters for preview
        file_name = get_file_name_from_url(url)
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(text)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching PDF {url}: {e}")

def selenium_extract(url_file):

    urls = url_extract(url_file)

    # Decode URLs before checking for ".pdf"
    pdf_urls = [url for url in urls if urllib.parse.unquote(url).lower().endswith(".pdf")]

    print("PDF URLs:", len(pdf_urls))
    print("All URLs:", len(urls))

    # Scrape text from normal web pages
    for url in urls:
        if not url.lower().endswith(".pdf"):
            selenium_webscrap(url)

    # Extract text from PDF links
    for pdf_url in pdf_urls:
        pdf_data(pdf_url)


