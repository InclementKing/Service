import time
import serviceProcesses as service


def introText():
	print('\nWhat would you like to do today?')

	options = ['1. Manage accounts', '2. Log in', '3. End']
	for i in options:
		print('  ' + i)
	return input('> ')

def manage():
	print('\nWhat action would you like to perform?')

	options = ['1. Create', '2. Remove', '3. Change']
	for i in options:
		print('  ' + i + ' an account.')

	choice = input('> ')

def Create():
	username = input('What would you like your username to be? ')
	password = input('What would you like your password to be? ')
	return service.Create(username, password)

def Login():
	return service.Login()

def Remove():
	toRemove = input('What account would you like to remove? ')
	return service.Remove(toRemove)

def changePass():
	return service.changePass()



while 1:
	choice = introText()
	if choice == '1':
		menuStatus = manage()
		if menuStatus == '1':
			status = Create()

			if status == 1:
				pass

			elif status == 0:
				print('Please try again.\n')

		elif menuStatus == '':
			status = Remove()

			if status == 1:
				pass

			elif status == 0:
				print('Please try again.\n')

			else:
				print('Error.')

		elif menuStatus == '3':
			status = changePass()

			if status == 1:
				pass

			elif status == 0:
				print('Please try again.\n')

		else:
			print('Please enter a valid option.')

	elif choice == '2':
		status = Login()

		if status == 1:
			pass

		elif status == 0:
			print('Please try again.\n')

		else:
			print('Error.')

	elif choice == '3':
		print('Finished.\n')
		break

	else:
		print('Please enter a valid option.')

	time.sleep(1)