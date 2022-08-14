import datetime

'''
I have borrowed this code from this tutorial: https://www.geeksforgeeks.org/personalized-task-manager-in-python/
I have also customized some of the code to achieve the project goals.
'''

# Function that requires the users data and creates a txt file of it. 
def user_information(ussnm, pssd):
	name = input("Enter your full name: ")
	email_address = (input("Enter your email address: "))+'\n'
	ussnm_ = ussnm+" task.txt"
	f = open(ussnm_, 'a')
	f.write(pssd)
	f.write("\nName: ")
	f.write(name)
	f.write('\n')
	f.write("Email Address: ")
	f.write(email_address)
	f.write('\n')
	f.close()

