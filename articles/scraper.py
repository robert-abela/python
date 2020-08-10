import csv
import time
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://www.tripadvisor.com/Restaurant_Review-g190328-d8867662-Reviews-Storie_Sapori_La_Valletta-Valletta_Island_of_Malta.html"
WAIT = 10 # seconds

LOADING_DIV = (By.ID, "taplc_hotels_loading_box_rr_resp_0")
ALL_LANGS = (By.ID, "filters_detail_language_filterLang_ALL")
MORE_BTN = (By.CSS_SELECTOR, "span.taLnk.ulBlueLinks")
NEXT_BTN = (By.CSS_SELECTOR, 'a.nav.next')
LAST_PAGE = (By.CSS_SELECTOR, 'a.pageNum.last')
REVIEWS = (By.CSS_SELECTOR, 'div.ui_column.is-9')
SCORE = (By.XPATH, ".//span[contains(@class, 'ui_bubble_rating bubble_')]")
DATE = (By.CSS_SELECTOR, 'span.ratingDate')
TITLE = (By.CSS_SELECTOR, 'span.noQuotes')
REVIEW_TEXT = (By.CSS_SELECTOR, 'p.partial_entry')

def find_element(find_from, element):
    return find_from.find_element(element[0], element[1])

def load_full_reviews(driver):
    time.sleep(1) #StaleElementReferenceException: Message: stale element reference: element is not attached to the page document
    more_btn = WebDriverWait(driver, WAIT).until(EC.element_to_be_clickable(MORE_BTN))
    more_btn.click()
    WebDriverWait(driver, WAIT).until(EC.staleness_of(more_btn))
    assert find_element(driver, MORE_BTN).text != 'More'

def start_browser():
    driver = webdriver.Chrome("./chromedriver")
    driver.maximize_window()
    driver.implicitly_wait(WAIT)
    driver.get(URL)
    return driver

# Prepare CSV file
csvFile = open("reviews.csv", "w", newline='', encoding="utf-8")
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['Score','Date','Title','Review'])

driver = start_browser()

# Get reviews in all languages
all_langs = find_element(driver, ALL_LANGS)
all_langs.click()

# Wait for reviews to load
WebDriverWait(driver, WAIT).until(EC.invisibility_of_element_located(LOADING_DIV))

# Find the last page number
last_page = find_element(driver, LAST_PAGE)
pages = int(last_page.get_attribute("data-page-number"))
print("[INFO] found", pages, "pages in total")
curr_page = 1

while curr_page <= pages:
    print("[INFO] Scraping page", curr_page)
    load_full_reviews(driver)

    reviews = driver.find_elements(REVIEWS[0], REVIEWS[1])
    num_page_items = min(len(reviews), 10)

    # Loop through the reviews found
    for i in range(num_page_items):
        # get the score, date, title and review
        score_span = find_element(reviews[i], SCORE)
        score_class = score_span.get_attribute("class")
        score = score_class.split("_")[3]
        date = find_element(reviews[i], DATE).get_attribute("title")
        title = find_element(reviews[i], TITLE).text
        review = find_element(reviews[i], REVIEW_TEXT).text.replace("\n", "")
        # Save to CSV
        csvWriter.writerow((score, date, title, review))

    next_page = find_element(driver, NEXT_BTN)
    driver.get(next_page.get_attribute("href"))
    print("[INFO] Page ready")
    curr_page += 1

# Close CSV file and browser
csvFile.close()
driver.close()
print("[INFO] Scraping finished")