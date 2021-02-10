import threading
import time, os
import subprocess, platform

value = 0
def load():
	global value

	try:
		global sys
		import sys
		global google_translator, constant, outro
		from google_trans_new import google_translator, constant
		import outro
		value += 1

	except ImportError as error:
		print(f"Execution Error: {error}")
		sys.exit()


def screen():
	global value

	count = 1
	prompt = "Loading" + '.'*count
	print(prompt, end = '\r')
	count += 1
	
	while value != 1:
		time.sleep(0.3)
		if count % 6 == 0:
			count = 1
		prompt = "Loading" + '.'*count
		print(prompt, end = '\r')
		count += 1



def detection(TXT, translator):
	detected = translator.detect(TXT)
	return detected


def translation(ORIGIN, DESTINATION, translator):
	os.system('cls' if os.name == 'nt' else 'clear')
	print("FINISH>  ' :f! '\n")

	TEXT = input("Enter text:\n")
	TEMP = ''
	while TEMP != ':f!':
		TEMP = input()
		TEXT += TEMP
		if TEMP == '':
			TEXT += '\n'
	TEXT = TEXT[:-3]

	remove()

	if ORIGIN == 'auto':
		DETECTED = detection(TEXT, translator)
		print("\n````````````````````````````````````````````")
		print(f"{DETECTED[1].upper()} is detected")
		print(f"Language Key Word --- {DETECTED[0]}")
		print(f"{constant.LANGUAGES[DETECTED[0]].capitalize()} → {constant.LANGUAGES[DESTINATION].capitalize()}")
		print("````````````````````````````````````````````")

	else:
		print(f"\n{constant.LANGUAGES[ORIGIN].capitalize()} → {constant.LANGUAGES[DESTINATION].capitalize()}")

	TRANSLATED = translator.translate(TEXT, lang_src = ORIGIN, lang_tgt=DESTINATION)

	print("\nResult:")
	print(TRANSLATED)
	######################



def list():
	for key, value in constant.LANGUAGES.items():
		print(f"{value} ---- {key}")
	ANS = input("Enter the language you want to translate? (N : Not found) ")
	return ANS

def usrANS(index):
	while True:
		if index == 0:
			print("Enter: auto\t--list: Language List\t--exit: System Exit\n")
			TEMP = input("Which language the original text is? (Enter: auto) ")
		else:
			TEMP = input("\nWhat is the destination language? (Enter: eng) ")


		if TEMP == '':
			TEMP = 'auto'
			#print(TEMP)
			return TEMP
		elif TEMP == '--list':
			TEMP = list()
			if TEMP.lower() == 'n':
				os.system('cls' if os.name == 'nt' else 'clear')
				print("THANK YOU FOR USING THIS APPLICATION")
				sys.exit()
		elif TEMP == '--exit':
			print("THANK YOU FOR USING THIS APPLICATION")
			sys.exit()	
		else:
			pass


		TEMP = TEMP.lower()
		if TEMP in constant.LANGUAGES.keys():
			break
			#print('keys')

		elif TEMP in constant.LANGUAGES.values():
			for key, value in constant.LANGUAGES.items():
				if TEMP == value:
					TEMP = key
					break
			break 
			#print(ORIGIN)

		else:
			os.system('cls' if os.name == 'nt' else 'clear')
			print("WARNING> INPUT AGAIN\n")
			continue

	os.system('cls' if os.name == 'nt' else 'clear')
	print("Enter: eng\t--list: Language List\t--exit: System Exit\n")
	if index == 0:
		print("Which language the original text is? (Enter: auto) ", end='')
	else:
		print("What is the destination language? (Enter: eng) ", end ='')
	print(TEMP)

	return TEMP


def remove():
	sys.stdout.write("\033[F") #back to previous line 
	sys.stdout.write("\033[K") #clear line 



def main():
					#####################
					#  INITIALIZATION	#
	######################################################
	os.system('cls' if os.name == 'nt' else 'clear')
	load_thread = threading.Thread(target=load)
	screen_thread = threading.Thread(target=screen)
	load_thread.start()
	screen_thread.start()

	load_thread.join()
	screen_thread.join()

	os.system('cls' if os.name == 'nt' else 'clear')
	print('\b'*12 +'done')
	os.system('cls' if os.name == 'nt' else 'clear')
	#######################################################


				   #######################
			       #  TRANSLATION & UI   #
	#######################################################
	translator = google_translator() # Class Creation
	
	ORIGIN = usrANS(0)
	DESTINATION = usrANS(1)
	if DESTINATION == 'auto':
		DESTINATION = 'en'

	translation(ORIGIN, DESTINATION, translator)
	while True:
		translator = google_translator()
		ANS = input("\nExit: q!\tSame Language: s!\t Other Language: o!\nCommand: ")
		os.system('cls' if os.name == 'nt' else 'clear')
		if ANS == 'q!':
			break
		elif ANS == 's!':
			translation(ORIGIN, DESTINATION, translator)
		elif ANS == 'o!':
			ORIGIN = usrANS(0)
			DESTINATION = usrANS(1)
			translation(ORIGIN, DESTINATION, translator)
		else:
			pass
	#######################################################



	#OUTRO
	os.system('cls' if os.name == 'nt' else 'clear')
	print(outro.TXT)

if __name__ == '__main__':
	main()