
#pbar = tqdm(total=100)
#pbar.update(100)
#pbar.close()



print('[AMADEUS] Initializing Amadeus...')
print('[AMADEUS] Importing libraries...')
print('\n\n')

from tqdm import tqdm
import handler as hl
import database as db
import time
import test3


print('\n[AMADEUS] All libraries installed.')


def mainloop(InnerFun, timeout=30, block=['None']):
	
	people = db.get_contacts()
	[people.remove(i) if i != 'None' else people for i in block]
	
	while True:
		try:
			for contact in range(1, 18): #Tener al menos 18 contactos
				

					
				db.extract_data(contact)

				if db.newMsg() and db.get_name() == 'Abpapa': #in people:  #CHAT FIJADO

					hl.open_conversation(db.get_xpath_num(contact))
					text 	 = db.get_message()
					response = InnerFun(text)

				
					hl.write(response, db.get_xpath_num(contact))
					hl.open_conversation(db.get_xpath_num(contact + 1))

					
		except:		
			hl.refresh()
			hl.wait_until_window(timeout)

			people = db.get_contacts()
			[people.remove(i) if i != 'None' else people for i in block]

		
				


def fun(arg):
	return test3.chat(arg)




print('[AMADEUS] Starting Chrome Driver...\n')

hl.init()

driver = hl.driver()

db.init(driver)

print('\n[AMADEUS] Chrome Driver started successfully.')
print('[AMADEUS] Amadeus initialized.')

print('[AMADEUS] Waiting for user to login')
hl.wait_until_window()

print('[AMADEUS] Starting...')
mainloop(InnerFun= fun, timeout=30, )