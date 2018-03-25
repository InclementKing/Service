import time
import serviceProcesses as service


def introText():
	print "\nWhat would you like to do today?"
	print "  1. Manage accounts"
	print "  2. Log in"
	print "  3. End"
	return raw_input("> ")

def manage():
	print "\nWhat action would you like to perform?"
	print "  1. Create an account"
	print "  2. Remove an account"
	print "  3. Change a password"

	return raw_input("> ")

def Create():
	username = raw_input("What would you like your username to be? ")
	password = raw_input("What would you like your password to be? ")
	return service.Create(username, password)

def Login():
	return service.Login()

def Remove():
	toRemove = raw_input("What account would you like to remove? ")
	return service.Remove(toRemove)

def changePass():
	return service.changePass()



while 1:
	choice = introText()
	if choice == "1":
		menuStatus = manage()
		if menuStatus == "1":
			status = Create()

			if status == 1:
				pass

			elif status == 0:
				print "Please try again.\n"

		elif menuStatus == "2":
			status = Remove()

			if status == 1:
				pass

			elif status == 0:
				print "Please try again.\n"

			else:
				print "Error."

		elif menuStatus == "3":
			status = changePass()

			if status == 1:
				pass

			elif status == 0:
				print "Please try again.\n"

		else:
			print "Please enter a valid option."

	elif choice == "2":
		status = Login()

		if status == 1:
			pass

		elif status == 0:
			print "Please try again.\n"

		else:
			print "Error."

	elif choice == "3":
		print "Finished.\n"
		break

	else:
		print "Please enter a valid option."

	time.sleep(1)