try:
	import keyboard as kb
	from datetime import datetime, timedelta
	import lorem
except ImportError:
	print("Missing dependencies")
	exit()
import sys, os, math

set = " abcdefghijklmnopqrstuvwxyz1234567890,."
skip = lambda string: string[1:]

def prompt(inputString):
	string = inputString

	print("Press SPACE to start or Q to quit")
	while not kb.is_pressed(" ") and not kb.is_pressed("q"):
		pass
	if kb.is_pressed("q"):
		exit()

	os.system("cls")
	oldTime = datetime.now()

	while len(string) > 0:

		while not string[0].lower() in set:
			string = skip(string)

		print(string)
		while not kb.is_pressed(string[0]):
			pass
		os.system("cls")
		string = skip(string)

	delta = datetime.now() - oldTime
	print("\n - Stats - ")
	print("\nTime used: {m}m : {s}s : {micro} ".format(m = math.floor(delta.seconds/60), s = delta.seconds % 60, micro = delta.microseconds))
	print("\nWords/min: {}".format(len(inputString.split(" ")) / delta.seconds * 60))
	print("\nText:\n - length: {len}\n - words: {cou}".format(len = len(inputString), cou = len(inputString.split(" "))))

while True:
	text = lorem.text().split(".")
	text = "".join(text[i] + "." for i in range((lambda l: l if l <= 4 else 4)(len(text))))
	prompt(text)
