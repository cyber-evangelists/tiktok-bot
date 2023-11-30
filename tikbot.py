from os import system
from time import sleep
from colorama import init, Fore
import undetected_chromedriver as uc
from selenium.common.exceptions import NoSuchElementException


try:
    # driver = uc.Chrome()
    driver = uc.Brave()
except Exception as e:
    print(Fore.RED + "[!] No internet connection")
    print(Fore.RED + f"[!] Error: {e}")
    exit()
url = "https://zefoy.com"
driver.get(url)
# driver.minimize_window()
sleep(2)
driver.save_screenshot("nowsecure.png")
sleep(10)


try:
    driver.close()
except OSError as e:
    print(f"Error during driver quit: {e}")
