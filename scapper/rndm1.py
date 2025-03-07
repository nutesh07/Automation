from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchWindowException
import time

# Proxy credentials

proxy_username = "nutesh07"
proxy_password = "Nuteshtajne07@"
proxy_url = "sg.proxymesh.com:31280"  # Replace with your proxy URL

# Twitter credentials
username = "nuteshtajne77@gmail.com"  # Replace with your Twitter username
password = "Nutesh077@@"  # Replace with your Twitter password

# Set up Chrome options with proxy
chrome_options = Options()
chrome_options.add_argument(f'--proxy-server={proxy_url}')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

# Set up Chrome WebDriver with proxy
service = Service(r"C:\Users\Nutesh\scapper\chromedriver.exe")  # Replace with the path to your ChromeDriver executable
driver = webdriver.Chrome(service=service, options=chrome_options)

def human_like_scrolling(driver):
    for _ in range(5):
        driver.execute_script("window.scrollBy(0, 200);")
        time.sleep(1)
    for _ in range(5):
        driver.execute_script("window.scrollBy(0, -200);")
        time.sleep(1)

def human_like_cursor_movement(driver):
    action = ActionChains(driver)
    for _ in range(10):
        action.move_by_offset(50, 0).perform()
        time.sleep(0.5)
    for _ in range(10):
        action.move_by_offset(-50, 0).perform()
        time.sleep(0.5)
    action.reset_actions()  # Reset actions to ensure no out of bounds movement

def login_to_twitter(driver):
    driver.get("https://x.com/i/flow/login")
    wait = WebDriverWait(driver, 30)  # Wait up to 30 seconds for elements to appear

    # Human-like scrolling and cursor movement
    human_like_scrolling(driver)
    human_like_cursor_movement(driver)

    # Wait until the username input field is visible
    username_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@class, 'r-30o5oe') and contains(@class, 'r-1dz5y72')]")))
    username_input.send_keys(username)
    print("Username input sent!")

    # Human-like scrolling and cursor movement
    human_like_scrolling(driver)
    human_like_cursor_movement(driver)

    # Wait until the "Next" button is clickable
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']")))
    next_button.click()
    print("Next button clicked!")

    # Add a small delay to allow the transition
    time.sleep(3)

    try:
        # Wait until the password input field is visible
        password_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
        password_input.send_keys(password)
        print("Password input found and sent!")
    except TimeoutException:
        print("Password input field not found! Checking for other elements...")

    try:
        # Look for login error message or other indications
        error_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'css-901oao') and contains(@class, 'r-1awozwy')]")))
        print("Error message found:", error_message.text)
    except TimeoutException:
        print("No error message found. Proceeding with login attempt.")
    except NoSuchWindowException:
        print("The browser window was closed unexpectedly.")

    try:
        # Click on the "Log in" button
        login_button = driver.find_element(By.XPATH, "//span[text()='Log in']")
        login_button.click()
        print("Login button clicked!")
    except NoSuchElementException:
        print("Login button not found!")
    except NoSuchWindowException:
        print("The browser window was closed unexpectedly.")

def fetch_trending_topics(driver):
    wait = WebDriverWait(driver, 30)
    try:
        # Scroll to the "What’s Happening" section
        trending_section = wait.until(EC.presence_of_element_located((By.XPATH, "//section[@aria-labelledby='accessible-list-0']")))
        driver.execute_script("arguments[0].scrollIntoView(true);", trending_section)

        # Find the trending topics
        trending_topics = driver.find_elements(By.XPATH, "//section[@aria-labelledby='accessible-list-0']//div[@dir='ltr']")
        for i, topic in enumerate(trending_topics[:5]):  # Get top 5 topics
            print(f"Trending {i+1}: {topic.text}")
    except TimeoutException:
        print("Trending topics section not found.")
    except NoSuchElementException:
        print("An element was not found while fetching trending topics.")
    except NoSuchWindowException:
        print("The browser window was closed unexpectedly.")

def main():
    try:
        login_to_twitter(driver)
        fetch_trending_topics(driver)
    except NoSuchWindowException:
        print("The browser window was closed unexpectedly.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Close the WebDriver after a delay to see the result
        time.sleep(10)
        driver.quit()

if __name__ == "__main__":
    main()
