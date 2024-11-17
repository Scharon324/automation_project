def test_calculation_logic(setup_browser):
    driver = setup_browser
    driver.get("https://laenutaotlus.bigbank.ee/?amount=5000&period=60&productName=SMALL_LOAN&loanPurpose=DAILY_SETTLEMENTS")
    
    loan_amount_input = driver.find_element(By.ID, "loan-amount")
    period_input = driver.find_element(By.ID, "loan-period")
    calculate_button = driver.find_element(By.ID, "calculate-button")
    
    loan_amount_input.clear()
    loan_amount_input.send_keys("3000")
    period_input.clear()
    period_input.send_keys("30")
    calculate_button.click()
    
    monthly_payment = driver.find_element(By.CLASS_NAME, "input-group")
    monthly_payment = driver.find_element(By.NAME, "input-group")
    monthly_payment = driver.find_element(By.CSS_SELECTOR, ".input-group")

assert monthly_payment.text == "Correct Calculated Value", "Calculation is incorrect!"
