from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_modal_opens_on_page_load(setup_browser):
    driver = setup_browser
    driver.get("https://laenutaotlus.bigbank.ee/?amount=5000&period=60&productName=SMALL_LOAN&loanPurpose=DAILY_SETTLEMENTS")
    
    try:
        # Wait for the modal to appear
        modal = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "calculator-modal-class"))
        )
        assert modal.is_displayed(), "Modal is not displayed!"
    except Exception as e:
        print("Modal not found. Debugging page source...")
        print(driver.page_source)  # Debugging the issue
        raise e
