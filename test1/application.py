import signal
import time
import threading


class Application:
	def __init__(self):
		self.action = True
		self.thread = threading.Thread(target=self.normal, args=())
		self.thread.deamon  = True
		self.thread.start()

	def normal(self):
		while self.action:
			print('all normal...')
			time.sleep(2)

	def stop(self):
		self.thread.join()

application = Application()

def sigterm_handler(signal, frame):
    print('Got a sigterm!!!')
    application.action = False


signal.signal(signal.SIGTERM, sigterm_handler)

