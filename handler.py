from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

global browser


def init():
	global browser
	ChromeDriver_path = ChromeDriverManager().install() 
	browser = webdriver.Chrome(executable_path= ChromeDriver_path)
	browser.get('https://web.whatsapp.com/')
	'''
	options = webdriver.ChromeOptions()
	options.add_argument('--user-data-dir=./User_Data')
	browser = webdriver.Chrome(executable_path= ChromeDriver_path,chrome_options=options)
	browser.get('https://web.whatsapp.com/')
	'''

def driver():
	return browser

def write(text, XPath_num):
	browser.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div['+str(XPath_num)+']').click()
	browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]").send_keys(text + '\n')
	time.sleep(2) #Espera a que se envie el mensaje porque sino aparece ventana emergente

def Is_existing(XPath_num):
	try:
		browser.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div['+str(XPath_num)+']')
		print(' existe  /*[@id="pane-side"]/div[1]/div/div/div['+str(XPath_num)+']')
		return True
	except:
		return False



def wait_until_window(timeout=30):
	WebDriverWait(browser, timeout).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[1]')))
	
def quit():
	browser.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/div').click()
	time.sleep(0.5)
	browser.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[6]/div').click()
	browser.quit()

def open_conversation(XPath_num):
	browser.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div['+str(XPath_num)+']').click()

def refresh():
	browser.refresh()
	


