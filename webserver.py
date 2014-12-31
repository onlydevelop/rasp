#!/usr/bin/python

import web
import os

urls = (
		'/led/(.*)', 'LEDController'
	)

class LEDController:

	def GET(self, opt):
		if(opt == ""):
			opt = "auto"
		command = "sudo ./LEDBlinker.py " + opt
		os.system(command)
		return "Executing command: " + command

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()

