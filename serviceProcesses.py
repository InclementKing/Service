import os, shutil

sHome = os.path.expanduser('~/.Service/')
accountsDir = sHome + 'Users/'
currentlyLoggedIn = sHome + 'loggedIn'


def writePassword(account, password):
	passwordFile = open(accountsDir + account + '/password', 'w')
	passwordFile.write(password)
	passwordFile.close()

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

def startup():
	if os.path.exists(sHome):
		pass

	else:
		os.makedirs(accountsDir + 'admin/')
		writePassword('admin', 'password')
		login('admin')

def getCurrentlyLoggedIn():
	loggedInFile = open(currentlyLoggedIn, 'r')
	loggedIn = loggedInFile.read()
	loggedInFile.close()

	return loggedIn

def getAccountPassword(account):
	accountPasswordFile = open(accountsDir + account + '/password', 'r')
	accountPassword = accountPasswordFile.read()
	accountPasswordFile.close()

	return accountPassword

def logout():
	os.remove(currentlyLoggedIn)

def remove(account):
	shutil.rmtree(accountsDir + account + '/')



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
	admin = False
	if os.path.exists(currentlyLoggedIn):
		loggedIn = getCurrentlyLoggedIn()

		if loggedIn == 'admin':
			print('\nAs admin, you have a few extra powers.')
			print('Removing accounts only requires the admin password,')
			print("and you can remove all acounts with the keyword 'All'.")
			print('Make sure to use this power responsibly.\n')
			admin = True

	accountToRemove = input("Enter the name of the account to be removed: ")

	if accountToRemove == 'All':
		if admin:
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

	elif accountToRemove == 'admin':
		print('That account cannot be removed.')

		return 0

	elif os.path.exists(accountsDir + accountToRemove):
		loggedIn = getCurrentlyLoggedIn()

		if admin == True:
			adminPassword = getAccountPassword('admin')
			passwordAttempt = input('Enter the admin password: ')

			if passwordAttempt == adminPassword:
				remove(accountToRemove)
				if loggedIn == accountToRemove:
					logout()

				print('Account successfully removed.')

				return 1

			else:
				print('Incorrect password.')

				return 0

		else:
			correctPassword = getAccountPassword(accountToRemove)
			passwordAttempt = input('Password: ')

			if passwordAttempt == correctPassword:
				sure = input('This will remove the account ' + accountToRemove + ' and all associated data. Continue? (y/n) ')

				if sure == 'y':
					remove(accountToRemove)
					if loggedIn == accountToRemove:
						logout()
					print('Account removed successfully.')

					return 1

				else:
					print('Account not removed.')

					return 1

			else:
				print('Incorrect password.')

				return 0

	
	else:
		print('There is no account under that username.')

		return 0

def ChangePass():
	account = input('Username: ')
	accountPath = accountsDir + account + '/' 

	if os.path.exists(accountPath):
		newPassword = input('New password: ')

		writePassword(account, newPassword)

		print('Password changed successfully.')

		return 1

	else:
		print('No account under that username.')
		
		return 0






startup()