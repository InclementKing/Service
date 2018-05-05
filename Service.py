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

	return input('> ')

def successChecker(returnCode):
	if returnCode == 1:
		pass

	elif returnCode == 0:
		print('Please try again.')

	else:
		print('Something has gone horribly wrong. Unrecognized return code.')

while 1:
	choice = introText()
	if choice == '1':
		menuChoice = manage()

		if menuChoice == '1':
			successChecker(service.Create())

		elif menuChoice == '2':
			successChecker(service.Remove())

		elif menuChoice == '3':
			successChecker(service.changePass())

		else:
			print('Please enter a valid option.')

	elif choice == '2':
		successChecker(service.Login())

	elif choice == '3':
		print('Finished.\n')
		break

	else:
		print('Please enter a valid option.')