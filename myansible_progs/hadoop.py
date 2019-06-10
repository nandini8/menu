def hadoop():



	import subprocess as sb
	import pyttsx3
	sp = pyttsx3.init()
	import getpass
	import signal



	def interupt(x,y):

	      print(" \n thank you for using my tool")
	      exit()
	signal.signal(2, interupt )



	password = "redhat"

	menu_pass = getpass.getpass("please enter ur password :") 
	if password != menu_pass:
		print("please enter a valid password")
	else:
	

		sp.say("what you wanna do in haddop")
		sp.runAndWait()
		print("what you wanna do in hadoop")
		sp.say(" press 1: to create a master of ur hadoop system")
		sp.runAndWait()
		print("press 1:  to create a master of ur hadoop system")
		sp.say("press 2: to create a datanode of ur hadoop system")
		sp.runAndWait()
		print("press 2: to create a datanode of ur hadoop system")
		sp.say("press 3: to create client of your hadoop system")
		sp.runAndwait()
		print("press 3: to create client of your hadoop system")
		sp.say("press 4: if you want to upload some data or file in hadoop")
		sp.runAndWait()
		print("press 4: if you want to upload some data or file in hadoop")
		
		sp.say("press 5: if you want to retrive your data")
		sp.runAndWait()
		print("press 5: if you want to retrive your data")
		
		
		choice = int(input("enter your choice"))
	
		if choice == 1:
		
		  nn =   sb.getstatusoutput("ansible-playbook haddop_nn.yml")
		  if nn[0] == 0:
		     sp.say("master created successfully")
		     sp.runAndWait()
		     print("master created successfully")
		  else:
		     sp.say("there is some problem please check your entry")
		     sp.runAndWait()
		     print("there is some problem please check your entry")
	        elif choice == 2:
		 dn  = sb.getstatusoutput("ansible-playbook haddop_nn.yml")	
		 if dn[0] == 0:
		     sp.say("datanodes created successfully")
		     sp.runAndWait()
		     print("datanodes created successfully") 
		 else:
		     sp.say("there is some problem please check your entry")
		     sp.runAndWait()
		     print("there is some problem please check your entry")
	       elif choice == 3:
		 cn = sb.getstatusoutput("ansible-playbook hadoop_cn.yml")
		 if cn[0] == 0:
		     sp.say("client created successfully")
		     sp.runAndWait()
		     print("client created successfully")
		 else:
		     sp.say("there is some problem please check your entry")
		     sp.runAndWait()
		     print("there is some problem please check your entry")
	      elif choice == 4:
		put  = sb.getstatusoutput("ansible-playbook hadoop_put.yml")
		if put[0] == 0:
		     sp.say("file put successfully")
		     sp.runAndWait()
		     print("file put successsfully")
		else:
		     sp.say("there is some problem please check your entry")
		     sp.runAndWait()
		     print("there is some problem please check your entry")
	      if choice == 5:
		read = sb.getstatusoutput("ansible-playbook hadoop_read.yml")
		if read[0] == 0:
		     sp.say("please read your file")
		     sp.runAndWait(0
		     print("please read your file")
		else:
		     sp.say("there is some problem please check your entry")
		     sp.runAndWait()
		     print("there is some problem please check your entry")
	      else:
		sp.say("THank you for using our tool")
		sp.runAndWait()
		print("thank you for using our tool")  
hadoop()
