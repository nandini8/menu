def yum():
	import pyttsx3
	import subprocess as sb
	sp  = pyttsx3.init()

	sb.getoutput("ansible-playbook yum1.yml")
	sp.say("your yum is ready")
	sp.runAndWait()
	print("your yum is ready")
yum()
