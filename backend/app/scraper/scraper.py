import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import time
import os
from dotenv import load_dotenv
import cohere
from bs4 import BeautifulSoup
import re
import html
import stealth_requests as requests
    
class Scraper():
    def __init__(self):
        load_dotenv()
        self.driver = None
        self.co = cohere.Client(api_key=os.getenv("COHERE_PROD_API_KEY"))

    def download_html(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                time.sleep(2)
                return response.text
            else:
                print(f"Failed to retrieve the page. Status code: {response.status_code}")
                return None
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def scrape(self, url: str, schema: str):
        try:
            chrome_options = uc.ChromeOptions()
            chrome_options.add_argument("--start-maximized")
            
            self.driver = uc.Chrome(options=chrome_options)
            self.driver.get(url)
            
            wait = WebDriverWait(self.driver, 30)
            wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

            # Short sleep to ensure content is fully rendered
            time.sleep(3)
            html_content = self.driver.execute_script("return document.body;")
            html_content_cleaned = self.clean_html(html_content.text)
            
            result = self.process_with_ai(html_content_cleaned, schema)            
            return result
        
        except Exception as e:
            print(f"An error occurred in Scraper: {str(e)}")
            return []
        
        finally:
            if self.driver:
                self.driver.quit()

    def clean_html(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        for element in soup(["script", "style", "meta", "link", "svg"]):
            element.decompose()
        for comment in soup.find_all(text=lambda text: isinstance(text, str) and text.strip().startswith('<!--')):
            comment.extract()
        for tag in soup.find_all(True):
            tag.attrs = {}
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        text = html.unescape(text)
        text = re.sub(r'http\S+', '', text)
        text = re.sub(r'\S+@\S+', '', text)
        text = re.sub(r'[^a-zA-Z\s]|\b[a-zA-Z]\b', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        text = '\n'.join([line for line in text.split('\n') if line.strip()])
        text = re.sub(r'\b(\w+)(\s+\1)+\b', r'\1', text, flags=re.IGNORECASE)
        text = '\n'.join([line for line in text.split('\n') if len(line.split()) > 2])
        return f"<html><body>{text}</body></html>"

    # Function to mimic human typing
    def human_type(self, text, element=None, min_delay=0.1, max_delay=0.5):
        if element:
            for char in text:
                element.send_keys(char)
                time.sleep(random.uniform(min_delay, max_delay))
        else:
            actions = ActionChains(self.driver)
            for char in text:
                actions.send_keys(char)
                time.sleep(random.uniform(min_delay, max_delay))
            actions.perform()

    # Function to mimic human-like button clicks
    def human_click(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).pause(random.uniform(0.25, 0.75)).click().perform()

    # Function to mimic human-like navigation to a URL
    def human_navigate(self, url):
        self.driver.get(url)
        self.random_sleep()  # Mimic human pause upon navigation

    # Random sleep to mimic human pause
    def random_sleep(self, min_sec=1, max_sec=2):
        time.sleep(random.uniform(min_sec, max_sec))

    def process_with_ai(self, html_content: str, schema: str):
        response = self.co.chat(
            message=f"Return data from the following html with the following json scheme {schema}. Only give the data, no yapping. {html_content}",
            connectors=[{"id": "web-search"}],
        )
        return response.text