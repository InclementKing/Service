import os, shutil
sData = "/Users/benrohrs/Documents/Service/"
sUsers = sData + "Users/"
sPass = sData + "Passwords/"
sLog = sData + "loggedIn"



def startup():
	if os.path.exists(sData):
		pass

	else:
		os.makedirs(sPass)
		os.makedirs(sUsers + "admin/")
		os.makedirs(sUsers + "ben/")


		adminPass = open(sPass + "admin", "w")
		adminPass.write("password")
		adminPass.close()

		benPass = open(sPass + "ben", "w")
		benPass.write("pass")
		benPass.close()

def Create(username, password):
	usrPath = sUsers + username + "/"

	if os.path.exists(usrPath):
		print "An account already exists under that username."
		return 0

	elif username == "All":
		print "That username is not allowed."
		return 0

	else:
		os.makedirs(usrPath)
		passwordFile = open(sPass + username, "w")
		passwordFile.write(password)
		passwordFile.close()
		print "Account created successfully."
		return 1

def logout():
	os.remove(sLog)

def login(username):
	if os.path.exists(sLog):
		logout()
		nowLoggedIn = open(sLog, "w")
		nowLoggedIn.write(username)
		nowLoggedIn.close()

	else:
		nowLoggedIn = open(sLog, "w")
		nowLoggedIn.write(username)
		nowLoggedIn.close()

def Login():
	if os.path.exists(sLog) == True:
		logged = open(sLog, "r")
		loggedIn = logged.read()
		logged.close()

		sure = raw_input(loggedIn + " is currently logged in. Do you wish to login under a different account? (y/n) ")
		if sure == "y":
			username = raw_input("Username: ")

			if os.path.exists(sUsers + username) == True:

				usersPassword = open(sPass + username, "r")
				correctPassword = usersPassword.read()
				usersPassword.close()

				passwrd = raw_input("Password: ")

				if passwrd == correctPassword:
					login(username)
					return 1

				else:
					print "Incorrect password."
					return 0

			else:
				print "There is no account under that username."
				return 0

		elif sure == "n":
			print "Remained logged in under account '" + loggedIn + "'"
			return 1

		else:
			print "Please enter either y or n."
			return 0

	else:
		username = raw_input("Username: ")
		if os.path.exists(sUsers + username) == True:
			usersPassword = open(sPass + username, "r")
			correctPassword = usersPassword.read()
			usersPassword.close()

			passwrd = raw_input("Password: ")

			if passwrd == correctPassword:
				nowLoggedIn = open(sLog, "w")
				nowLoggedIn.write(username)
				nowLoggedIn.close()

				print "Successfully logged in."
				return 1

			else:
				print "Incorrect password."
				return 0
		else:
			print "There is no account under that username."
			return 0

def Remove(username):
	admin = 0
	if os.path.exists(sLog) == True:
		logged = open(sLog, "r")
		loggedIn = logged.read()
		logged.close()

		if loggedIn == "admin":
			admin = 1

		else:
			pass
	else:
		pass

	if admin == 1:
		if username == "All":
			sure = raw_input("Are you sure you wish to remove all accounts? (y/n) ")
			if sure == "y":
				adminPath = sUsers + "admin/"
				adminPass = sPass + "admin"

				shutil.rmtree(sUsers)
				shutil.rmtree(sPass)
				os.makedirs(sUsers)
				os.makedirs(sPass)

				os.makedirs(adminPath)
				passwordFile = open(adminPass, "w")
				passwordFile.write("password")
				passwordFile.close()

				print "All accounts succesfully removed."
				return 1

		else:
			if os.path.exists(sUsers + username) == True:
				sure = raw_input("Are you sure you wish to remove account '" + username + "'? (y/n) ")
				if sure == "y":
					shutil.rmtree(sUsers + username + "/")
					os.remove(sPass + username)
					print "Account removed successfully."
					return 1
				else:
					print "Account not removed."
					return 0

	elif username == "admin":
		print "That account cannot be removed."
		return 0

	else:
		if os.path.exists(sUsers + username) == True:
			usersPassword = open(sPass + username, "r")
			correctPassword = usersPassword.read()
			usersPassword.close()

			passwrd = raw_input("Password: ")

			if passwrd == correctPassword:
				sure = raw_input("This will remove the account '" + username + "' and all associated data. Continue? (y/n) ")
				if sure == "y":
					shutil.rmtree(sUsers + username + "/")
					os.remove(sPass + username)
					print "Account removed successfully."
					return 1
				else:
					print "Account not removed."
					return 0
			else:
				print "Incorrect password."
				return 0
		else:
			print "There is no account under that username."
			return 0

def changePass():
	username = raw_input("Username: ")
	usrPath = sUsers + username + "/" 

	if os.path.exists(usrPath):
		newPass = raw_input("New password: ")
		os.remove(sPass + username)

		passwordFile = open(sPass + username, "w")
		passwordFile.write(newPass)
		passwordFile.close()

		print "Password changed successfully."
		return 1

	else:
		print "No account under that username."
		return 0

startup()