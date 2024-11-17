import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def setup_browser():
    # Get the directory where the test is located (current directory)
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Define the path to geckodriver (Firefox driver)
    geckodriver_path = os.path.join(current_directory, 'geckodriver.exe')
    
    # Check if geckodriver exists at the specified path
    if not os.path.exists(geckodriver_path):
        raise FileNotFoundError(f"Geckodriver not found at {geckodriver_path}")
    
    # Configure Firefox WebDriver options
    options = Options()
    options.headless = False  # Set to True to run headlessly
    
    # Set path to GeckoDriver
    service = Service(geckodriver_path)

    # Initialize Firefox WebDriver
    driver = webdriver.Firefox(service=service, options=options)
    
    # Set an implicit wait of 10 seconds for all element searches
    driver.implicitly_wait(10)
    
    yield driver  # Provide the WebDriver instance to the test
    
    # Quit the browser after the test
    driver.quit()

def test_modal_opens_on_page_load(setup_browser):
    driver = setup_browser
    driver.get("https://laenutaotlus.bigbank.ee/?amount=5000&period=60&productName=SMALL_LOAN&loanPurpose=DAILY_SETTLEMENTS")
    
    # Explicit wait to check if the modal is visible within 10 seconds
    try:
        modal = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "header-calculator-amount"))
        )
        assert modal.is_displayed()  # Check if modal is displayed
    except TimeoutException:
        print("Timed out waiting for modal to be visible")
        driver.quit()
        raise  # Re-raise the TimeoutException