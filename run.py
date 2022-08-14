import datetime


# pssd means password, ussnm is username
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

