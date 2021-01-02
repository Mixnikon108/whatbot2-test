from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


global browser, data, contacts


def init(driver):
	global browser, data, contacts

	browser  = driver
	data 	 = None
	contacts = {}

	

def __new_contact(name):
	global contacts

	contacts[str(name)] = []

	

def __analize():
	contacts = get_contacts()
	[__new_contact(i) for i in contacts if i not in contacts]
		


def save_message(text, contact, sender='Me'):
	global contacts

	__analize()
	records = get_records_from(contact)
	records.append({sender:str(text)})
	contacts[str(contact)] = records


def get_records_from(contact):
	return contacts[str(contact)]




def __contactXpath(num):
	if num > 1 and num < 20:
		return 20 - num
	elif num == 1:
		return num


def get_xpath_num(contact):
	return __contactXpath(contact)


def __ComHandler(XPath_num):
	grupo    = False
	arg      = browser.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div['+str(XPath_num)+']').text
	textList = arg.split('\n')
	#print(textList)            ####Arreglar emojis
	if ': ' in textList:
		textList.remove(': ')
		grupo = True

	if '' in textList:
		textList.remove('')
			
	if grupo == False and len(textList) == 4:	
		try:
			Msg_num = int(textList[-1])
		except ValueError:
			grupo = True
		

	contacto		  = textList[0]
	Last_message_time = textList[1]

	if grupo:
		Last_message_user = textList[2]
		message 		  = textList[3]

		if len(textList) == 5:
			Msg_num		  = textList[4]
		else:
			Msg_num		  = None
	else:
		Last_message_user = None
		message 		  = textList[2]

		if len(textList) == 4:
			Msg_num		  = textList[3]
		else:
			Msg_num		  = None

	return  contacto, Last_message_time, Last_message_user, message, Msg_num, grupo


def extract_data(conv_num):
	global data

	num = __contactXpath(conv_num)
	data = __ComHandler(num)



def get_name():
	return data[0]

def get_Last_message_time():
	return data[1]

def get_Last_message_user():
	return data[2]

def get_message():
	return data[3]

def get_Msg_num():
	return data[4]

def get_group():
	return data[5]

def get_contacts():
	contacts = []
	try:
		for i in range(1, 19):
			extract_data(i)
			contacts.append(get_name())
	except:
		pass

	return contacts
		
def newMsg():
	return True if get_Msg_num() != None else False
	

