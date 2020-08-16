import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://www.tripadvisor.com/Restaurant_Review-g190328-d8867662-Reviews-Storie_Sapori_La_Valletta-Valletta_Island_of_Malta.html"
WAIT = 10 # seconds

CURR_PAGE_NUM =  (By.CSS_SELECTOR, "a.pageNum.current")
MORE_BTN = (By.CSS_SELECTOR, "span.taLnk.ulBlueLinks")
NEXT_BTN = (By.CSS_SELECTOR, "a.nav.next")
LAST_PAGE = (By.CSS_SELECTOR, "a.pageNum.last")
ALL_LANGS = (By.ID, "filters_detail_language_filterLang_ALL")
LOADING_DIV = (By.ID, "taplc_hotels_loading_box_rr_resp_0")
REVIEW_LIST = (By.ID, "taplc_location_reviews_list_resp_rr_resp_0")
REVIEWS = (By.CSS_SELECTOR, "div.ui_column.is-9")
SCORE = (By.XPATH, ".//span[contains(@class, 'ui_bubble_rating bubble_')]")
DATE = (By.CSS_SELECTOR, "span.ratingDate")
TITLE = (By.CSS_SELECTOR, "span.noQuotes")
REVIEW_TEXT = (By.CSS_SELECTOR, "p.partial_entry")
REVIEW_LANG = (By.CSS_SELECTOR, "div.prw_reviews_google_translate_button_hsx")

class more_loads_full_reviews(object):
    def __init__(self, locator):
        self.locator = locator
    def __call__(self, driver):
        try:
            button = find_element(driver, self.locator)
            text = button.text
            print("[DEBUG] button =", text)
            if text == 'Show less':
                return True
            button.click()
            return False
        except Exception as e:
            print("[DEBUG]", str(e))
            return False

def find_element(find_from, element):
    return find_from.find_element(element[0], element[1])

def find_elements(find_from, element):
    return find_from.find_elements(element[0], element[1])

def start_browser():
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome("./chromedriver", options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(WAIT)
    driver.get(URL)
    return driver

def get_language(review):
    lang = "en" #assume English
    lang_divs = find_elements(review, REVIEW_LANG)
    if len(lang_divs) > 0:
        button = lang_divs[0]
        span = button.find_elements_by_tag_name("span")[0]
        url = span.get_attribute("data-url")
        index = url.find("sl=")
        if index != -1:
            lang = url[index+3: index+5]

    return lang

if __name__ == "__main__":
    # Prepare CSV file
    csvFile = open("reviews.csv", "w", newline='', encoding="utf-16")
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(['Score','Date','Title','Review', 'Language'])

    driver = start_browser()

    # Get reviews in all languages (wait for load)
    find_element(driver, ALL_LANGS).click()
    WebDriverWait(driver, WAIT).until(EC.invisibility_of_element_located(LOADING_DIV))

    # Find the last page number
    last_page = find_element(driver, LAST_PAGE)
    pages = int(last_page.get_attribute("data-page-number"))
    print("[INFO] found", pages, "pages in total")
    curr_page = 1

    while True:
        print("[INFO] Scraping page", curr_page)

        # Make sure all assumptions hold
        page = find_element(driver, CURR_PAGE_NUM)
        page_number = page.get_attribute("data-page-number")
        assert curr_page == int(page_number)
        assert find_element(driver, ALL_LANGS).get_attribute("checked") == "true"

        # Load and get all reviews
        WebDriverWait(driver, 30).until(more_loads_full_reviews(MORE_BTN))
        review_list = find_element(driver, REVIEW_LIST)
        reviews = find_elements(review_list, REVIEWS)
        print("[INFO]", len(reviews), "reviews found")

        for review in reviews:
            # Read the interesting review information
            score_span = find_element(review, SCORE)
            score = score_span.get_attribute("class").split("_")[3]
            date = find_element(review, DATE).get_attribute("title")
            title = find_element(review, TITLE).text
            text = find_element(review, REVIEW_TEXT).text.replace("\n", "")
            lang = get_language(review)
            # Save to CSV
            csvWriter.writerow((score, date, title, text, lang))

        print("[INFO] Page ready")
        if curr_page == pages:
            break
        else:
            next_page = find_element(driver, NEXT_BTN)
            driver.get(next_page.get_attribute("href"))
            curr_page += 1

    # Close CSV file and browser
    csvFile.close()
    driver.close()
    print("[INFO] Scraping finished")