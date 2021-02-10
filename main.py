import time
from multiprocessing import Process, shared_memory
import threading

share = threading.Condition()
init = 0

class Screen(threading.Thread):
	def __init__(self, name):
		threading.Thread.__init__(self)
		self.name = name

	def run(self):
		global init

		count = 0
		while True:
			share.acquire()
			print(init)
			if init == 1:
				share.release()
				break

			if count % 5 == 0:
				count = 1

			prompt = 'Loading' + '.'*count
			print(prompt, end='\r')
			time.sleep(1)
			count += 1



class Load(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.name = name

	def run(self):
		global init

		try:
			import sys
			from google_trans_new import google_translator
			time.sleep(5)
			share.acquire()
			init = 1
			share.notify_all()
			share.release()

		except ImportError as error:
			print(f"Execution Error: {error}")
			sys.exit()

"""
def load(id, state):
	if state == 'init':
		try:
			import sys
			from google_trans_new import google_translator
			time.sleep(5)
			ext_init = shared_memory.SharedMemory(name='initial')
			existing = ext_init.buf
			existing = 1


		except ImportError as error:
			print(f"Execution Error: {error}")
			sys.exit()

	elif state == 'screen':
		count = 1
		ext_init = shared_memory.SharedMemory(name='initial')
		ext = ext_init.buf
		while ext != 0:
			if count % 5 == 0:
				count = 1

			prompt = 'Loading' + '.'*count
			print(prompt, end='\r')
			time.sleep(0.5)
			count += 1
			
			ext_init = shared_memory.SharedMemory(name='initial')
			ext = ext_init.buf

	else:
		pass
"""

def main():
	#initialization
	#shd_init = shared_memory.SharedMemory(name = 'initial', create=True, size = 1)
	#initial = shd_init.buf
	#initial = 0

	"""
	states = ['init', 'screen']
	tasks = []
	for i, state in enumerate(states):
		thread = Process(target=load, args=(i+1, state))
		tasks.append(thread)
		thread.start()

	for tsk in tasks:
		tsk.join()
	"""

	th1 = Screen("screen")
	th2 = Load("load")

	th1.start()
	th2.start()

	th1.join()
	th2.join()


	#translator = google_translator()
	#translate_text = translator.translate('Hola!',lang_tgt='en')  
	#print(translate_text)


if __name__ == '__main__':
	main()