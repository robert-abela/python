class click_interactable_element(object):
  def __init__(self, locator):
    self.locator = locator
  def __call__(self, driver):
    try:
        element = driver.find_element(*self.locator)
        element.click()
        return element
    except ElementNotInteractableException:
        return False

#WebDriverWait(driver, 30).until(
#	click_interactable_element((By.ID, 'filters_detail_language_filterLang_ALL'))
#)

