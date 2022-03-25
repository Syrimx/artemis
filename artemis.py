import sys, os
import traceback
import requests
import time
import re
'''
Artemis (inspired by Gobuster)
-------
URL Mapper detecting directories on a Web Application.
You need to parse the whole url > {https://example.com}.
Have fun :)

Usage:
python3 <script> <url> <wordlist>
@Ely Schybol 16.03.2022
'''
b = '\033[92m'
c = '\033[93m'
reset = '\033[0m'

def welcome(url, wordlist):
	print("\nWelcome to Artemis. A URL Mapper")
	print("==================================================================================")
	print(f"[+]Url: {url}")
	print(f"[+]Wordlist: {wordlist}")
	print(f"[+]Time: {time.ctime(time.time())}")
	print("[+]Scanning...")
	print("==================================================================================")

def usage():
	print("\nWelcome to Artemis. A URL Mapper")
	print("=====================================")
	print(c+"usage:python3 <script> <url> <wordlist>"+reset)

def main(url, wordlist):
	try:
		welcome(url, wordlist)
		with open(wordlist, 'rb') as wordlist:
			for i in wordlist:
				try:
					word = i.decode().strip()
					path = os.path.join(url, f"{word}")
					response = requests.get(path)
					#print(f"[+]{path}:{response.status_code}")
					if(response.status_code != 404 and re.findall('[#]', word) == []):
						print(c+f"[+]{response.status_code}: /{word}"+reset)
					else:
						continue

				except requests.exceptions.MissingSchema:
					continue

				except requests.exceptions.TooManyRedirects:
					print(b+f"[+]{response.status_code}: /{word} is redirect =>"+reset)
					continue

	except KeyboardInterrupt as error:
		print(b+"\nEscaping Artemis..C ya"+reset)
		sys.exit()

if __name__ == '__main__':
	if(len(sys.argv) < 2 or sys.argv[1] == '-h'):
		usage()
	else:	
		main(sys.argv[1], sys.argv[2])
	sys.exit()
