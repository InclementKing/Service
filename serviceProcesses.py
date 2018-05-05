import os, shutil
sHome = os.path.expanduser('~/.Service/')
accountsDir = sHome + 'Users/'
passwordDir = sHome + 'Passwords/'
currentlyLoggedIn = sHome + 'loggedIn'


def startup():
	if os.path.exists(sHome):
		pass

	else:
		os.makedirs(passwordDir)
		os.makedirs(accountsDir + 'admin/')
		os.makedirs(accountsDir + 'ben/')


		adminPass = open(passwordDir + 'admin', 'w')
		adminPass.write('password')
		adminPass.close()

		benPass = open(passwordDir + 'ben', 'w')
		benPass.write('pass')
		benPass.close()

def writePassword(account, password):
	passwordFile = open(passwordDir + account, 'w')
	passwordFile.write(password)
	passwordFile.close()

def Create():
	username = input('What would you like your username to be? ')
	password = input('What would you like your password to be? ')
	userPath = accountsDir + username + '/'

	if os.path.exists(userPath):
		print('An account already exists under that username.')

		return 0

	elif username == 'All':
		print('That username is not allowed.')

		return 0

	else:
		os.makedirs(userPath)
		writePassword(username, password)
		print('Account created successfully.')

		return 1

def logout():
	os.remove(currentlyLoggedIn)

def getCurrentlyLoggedIn():
	loggedInFile = open(currentlyLoggedIn, 'r')
	loggedIn = loggedInFile.read()
	loggedInFile.close()

	return loggedIn

def getAccountPassword(account):
	accountPasswordFile = open(passwordDir + account, 'r')
	accountPassword = accountPasswordFile.read()
	accountPasswordFile.close()

	return accountPassword

def login(username):
	if os.path.exists(currentlyLoggedIn):
		logout()
		nowLoggedIn = open(currentlyLoggedIn, 'w')
		nowLoggedIn.write(username)
		nowLoggedIn.close()

	else:
		nowLoggedIn = open(currentlyLoggedIn, 'w')
		nowLoggedIn.write(username)
		nowLoggedIn.close()

def Login():
	if os.path.exists(currentlyLoggedIn):
		loggedIn = getCurrentlyLoggedIn()
		sure = input(loggedIn + ' is currently logged in. Do you wish to login under a different account? (y/n) ')

		if sure == 'y':
			account = input('Username: ')

			if os.path.exists(accountsDir + account):
				correctPassword = getAccountPassword(account)
				passwordAttempt = input('Password: ')

				if passwordAttempt == correctPassword:
					login(account)
					print('Successfully logged in.')

					return 1

				else:
					print('Incorrect password.')

					return 0

			else:
				print('There is no account under that username.')
				return 0

		elif sure == 'n':
			print('Remained logged in under account ' + loggedIn + '.')

			return 1

		else:
			print('Please enter either y or n.')

			return 0

	else:
		account = input('Username: ')

		if os.path.exists(accountsDir + account):
			correctPassword = getAccountPassword(account)
			passwordAttempt = input('Password: ')

			if passwordAttempt == correctPassword:
				login(account)
				print('Successfully logged in.')

				return 1

			else:
				print('Incorrect password.')

				return 0
		else:
			print('There is no account under that username.')

			return 0

def Remove():
	#TODO: Fix 'if admin is logged in' choice process
	accountToRemove = input("Enter the name of the account to be removed: ")
	admin = 0
	if os.path.exists(currentlyLoggedIn):
		loggedIn = getCurrentlyLoggedIn()

		if loggedIn == 'admin':
			admin = 1

	if accountToRemove == 'All':
		if admin == 1:
			sure = input('Are you sure you wish to remove all accounts? (y/n) ')
			if sure:
				shutil.rmtree(sHome)
				startup()

				print('All accounts succesfully removed.')

				return 1

			else:
				print('No accounts deleted.')

		else:
			print('Must be admin to remove all accounts.')

	else:
		if os.path.exists(accountsDir + accountToRemove):
			sure = input('Are you sure you wish to remove account '' + username + ''? (y/n) ')

			if sure == 'y':
				shutil.rmtree(accountsDir + accountToRemove + '/')
				os.remove(passwordDir + accountToRemove)
				print('Account removed successfully.')

				return 1

			else:
				print('Account not removed.')

				return 0

	elif accountToRemove == 'admin':
		print('That account cannot be removed.')

		return 0

	else:
		if os.path.exists(accountsDir + accountToRemove):
			correctPassword = getAccountPassword(accountToRemove)
			passwordAttempt = input('Password: ')

			if passwordAttempt == correctPassword:
				sure = input('This will remove the account '' + username + '' and all associated data. Continue? (y/n) ')

				if sure == 'y':
					shutil.rmtree(accountsDir + accountToRemove + '/')
					os.remove(passwordDir + accountToRemove)
					print('Account removed successfully.')

					return 1

				else:
					print('Account not removed.')

					return 0

			else:
				print('Incorrect password.')

				return 0

		else:
			print('There is no account under that username.')

			return 0

def changePass():
	account = input('Username: ')
	accountPath = accountsDir + account + '/' 

	if os.path.exists(userPath):
		newPassword = input('New password: ')
		os.remove(passwordDir + account)

		writePassword(account, newPassword)

		print('Password changed successfully.')

		return 1

	else:
		print('No account under that username.')
		
		return 0

startup()