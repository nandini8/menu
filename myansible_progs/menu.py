def menu():
	import  subprocess
	from hadoop import hadoop
	from yum import yum

	import  pyttsx3 as ps 
	import  os
	 
	sp= ps.init()
	sp.say(" welcome in world of automation please enter your choice")
	sp.runAndWait()
	print("\t\t\t welcome in world of automation please enter your choice \t\t\t")
	sp.say("press 1: you can add a user with some specific password of user")
	sp.runAndWait()
	print("press 1 :you can add a user with some specific password of user")
	sp.say("press 2 :you can configure any package or yum")
	sp.runAndWait()
	print("press 2:you can configure any package or yum")
	sp.say("press 3 : you can setup your hadoop cluster")
	sp.runAndWait()
	print("press 3 : you can setup your hadoop cluster") 
	sp.say("plaese enter ur choice")
	sp.runAndWait()
	choice  = int(input("plaese enter ur choice"))
	if choice == 1:
		sp.say("what you wanna do")
		sp.runAndWait()
		print("what you wanna do")
		sp.say("press 1 : for add user with password")
		sp.runAndWait()
	
		print("press 1 : for add user with password")
		sp.say("press 2 : for add user of an   specific group")
		sp.runAndWait()
		print("press 2 : for add user of an   specific group")
		sp.say("please enter a choice")
		sp.runAndWait()
		usr_choice = int(input("please enter a choice"))
		if usr_choice == 1:
			useradd()
		elif usr_chice == 2:
			groupadd()
		else:
			print("sorry plaese enter a right choice")
menu()
