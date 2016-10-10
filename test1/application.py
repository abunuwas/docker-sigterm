import signal
import time
import threading


class Application:
	def __init__(self):
		self.action = True

	def connect(self):
		print('Connectign...')
		while self.action:
			print('Working...')
			time.sleep(2)

	def disconnect(self):
		print('Disconnecting...')
		self.action = False

def sigterm_handler(signal, frame):
    print('Got a sigterm!!!')
    application.disconnect()


signal.signal(signal.SIGTERM, sigterm_handler)

application = Application()
application.connect()

