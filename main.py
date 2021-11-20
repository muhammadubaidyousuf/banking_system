import datetime 
import random

# in print body i am using "\t" the meaning is 1 space 
# "\n" for new line   

t = datetime.datetime.now()
time = t.strftime("%m-%d-%Y %I:%M %p") # THIS VARIABLE GET DEFAULT TIME AND DATE

master_password = "admin123" #THIS IS MASTER PASSWORD VARIABLE

# This program runs first when you run the program, this is a main function 
def main():
	# This is prigram head just print bank name 
	print("\t\t\t ######################################################################")
	print('\t\t\t WELLCOME TO OUR BANK \n')
	print('\t\t\t Please login or create new account, Choose a option \n')
	print("\t\t\t ######################################################################\n\n")
	# when x=TRUE program in runing when user give in put 3 x=False and program is close!
	x = True
	while x:
		# The print is asking user what you want to do
		print('\t\t\t 1) LOGIN STAFF OR USERS ACCOUNT')
		print('\t\t\t 2) CREATE A NEW ACCOUNT')
		print('\t\t\t 3) EXIT')
		# Option1 is input VARIABLE where user give a input and option1 hold a value
		option1 = input("\t\t\t choose: ")
		# It checks if the user has not entered an empty value!
		if option1 == "":
			print("Please select a option! 1, 2, 3")
		# This elif check if user give input (1) that user send to login function 
		elif option1 == "1":
			Login()
			x = False
		# This elif check if user give input (2) that user send to CreateUser function
		elif option1 == "2":
			CreateUser()
			x = False
		# This elif check if user give input (3) programme will be closed
		elif option1 == "3":
			x = False

# createing user
def CreateUser():
	# when user come on this function, all code run in while body, because if user type wrong command while loop ask again new command until user type right command
	x = True
	while x:
		# This VARIABLE by default set user Balance $100
		user_balance = 100
		# This VARIABLE set a default user type if user say it  is a user account or it is a staff account
		status = "user"
		# This line generate a random number for user account, in this line I am using random package for auto generated account 
		account_no = random.randrange(1000000000, 9000000000)
		print("\t\t\t Create New Account\n")
		# here user give input username as string, and username VARIABLE hold a value 
		username = input("\t Username: ")
		first_name = input("\t First Name: ")
		last_name = input("\t Last Name: ")
		password = input("\t Password: ")
		# here we ask to user is an staff account or user account, is_staff VARIABLE hold a string value
		is_staff = input("\t Is that an staff account? say yes or no: ").lower()
		# It checks whether the user has entered a new empty value
		if username =="":
			print("Please Enter Username!")
		elif first_name =="":
			print("Please Enter First Name!")
		elif last_name =="":
			print("Please Enter Last Name!")
		elif password =="":
			print("Please Enter Password!")
		else:
			# If all goes well, it will allow him to move on
			# We start another loop here to see if the user has created a staff account or a user account.
			m = True
			while m:
				# As we talked about above, if is_staff have a value "staff", we run it
				if is_staff == "yes":
					# and we change VARIABLE value
					status = "staff" 
					# here we ask a master password, master is admin123 
					pass_inp = input("\t ENTER MASTER PASSWORD: ").lower()
					# If the master password = matches the user's password, you will create a new account, otherwise it asks again.
					if pass_inp == master_password:
						# Now we will write this variable in the database.csv file that we opened above
						data_append = f"{account_no},{username},{first_name},{last_name},{password},{time},{user_balance},{status}"
						write_data(data_append, "a")
						# and user will get this message 
						print('\t Staff Accunt Created Successfully\n')
						# here x=false because we are in loop body when x = flase loop will be break, Then we will go out of the loop
						x = False
						# Then send the user to the login filed
						Login()
						m = False
					# If the above condition does not match then the user gets this message
					else:
						print("\t OPPS! Master Password Not Match, TRYAGIN.")
				else:
					# If the condition is not match then we run this part in which only user account is created
					status = "user" 
					# write.writerow([account_no, username, first_name, last_name, password, time, user_balance, status])
					data_append = f"{account_no},{username},{first_name},{last_name},{password},{time},{user_balance},{status}"
					# call write_data that function rewrite data in text file
					write_data(data_append, "a")
					print('\t User Accunt Created Successfully\n')
					x = False
					# After everything is done, we send the user to the login
					Login()
				
# This function allows the user to login
def Login():
	x = True
	# Like all functions, the loop is used here. If the user does something wrong, the loop repeatedly asks him to enter the correct value, until the user returns the correct value.
	while x:
		# Here user see a menu list
		print("\t\t\t LOGIN STAFF OR USERS ACOUNT\n")
		print("\t\t\t 1) STAFF ACCOUNT")
		print("\t\t\t 2) USER ACCOUT")
		print("\t\t\t 3) BACK TO MAIN MANU")
		# this is a input. staff_or_user_ip VARIABLE hold a string value given by the user
		staff_or_user_ip = input("\t\t\t choose: ")
		# first of all we check if user give (3), so we break the loop and send it to main menu
		if staff_or_user_ip =="3":
			main()
			break
			x = False

		else:
			is_staff = 'user'
			# here we open database file as a read mode
			reader = OpenFile()
			# and then we get a value from user as username and password
			username = input("\t\t\t USERNAME: ")
			password = input("\t\t\t PASSWORD: ")
			# here we check if user login by staff or user, if user given 1, user will login as a staff account
			if staff_or_user_ip == '1':
				# and then we change is_staff VARIABLE value as "staff"
				is_staff = "staff"
				# Here we extrct data from database file through for loop
				# If the data given by the user from any database row matches, we send the user to the login
				for row in reader:
					# row[1] gate username value, from database file second value
					if row[1] == username and password == row[4]:
						# row[0] gate account no, from database file first value in the row
						account_no = row[0]
						# here we send user as a staff account 
						AdminDashBoard(account_no)
						# when everything done we will break while loop
						break
						# and also break main loop
						x = False
			# if user say 2 it will be send user login as a user account
			elif staff_or_user_ip == '2':
				is_staff = 'user'
				# here we used forloop as data extrct from database file 
				for row in reader:
					# row[1] get username row[4] get password and row[7] get account status  
					if row[1] == username and row[4] == password:
						account_no = row[0]
						# user redirect User dashboard
						UserDashboard(account_no)
						break
						x = False
			else:
				print("ERROR")


# This is user dashboard function where user can parfom multiple task
def UserDashboard(account_no):
	x = True
	while x:
		print("######################################################################\n")
		# here you can see we call a function UserShowData, This function get 2 argomint first account no, and second colmnu no
		print(f"\t\t\t WELLCOME {UserShowData(account_no, 1)}\n")
		# here we also used UserShowData
		print(f"\t\t\t YOUR A/C NO {UserShowData(account_no, 0)} BALANCE ${UserShowData(account_no, 6)}")
		print("\t\t\t 1) ADD MONEY")
		print("\t\t\t 2) WITHDRAW MONEY")
		print("\t\t\t 3) CHECK BALANCE")
		print("\t\t\t 4) MONEY TRANSFER")
		print("\t\t\t 5) CHANGE PASSWORD")
		print("\t\t\t 6) LOGOUT\n")
		# user input for choose a command
		option_usr = input("\t choose: ")
		lines = OpenFile()
		# if user give empty values
		if option_usr == "":
			# user will get this message
			print("Please Enter A value!")
		# if user give input (1) so this part Will be run ADD MONEY  
		elif option_usr == "1":
			# here we ask to user a amount of no
			add_money = input("\t amount: ")
			# we used for loop to extract data from lines variable that we defined above
			for ln in lines:
				if account_no in ln[0]:
					ln[6] = int(ln[6]) + int(add_money)
					value_change(lines)
	        # print(f"\t\t\t New Balance Is ${row[6]}")
		# if user given (2) this part will be run Withdra Money 
		elif option_usr == "2":
			# amount input ask for user amount 
			widr_money = input("\t amount: ")
			# I don't need to repeat it here as I have mentioned above. The same thing is happening here
			for wd in lines:
				if account_no in wd[0]:
					wdb = int(wd[6])
					if int(widr_money) > wdb:
						print(f"\t\t\t OPPS! Your Withdra Greater Than Balance: ${UserShowData(account_no, 6)} \n")		 
					else:
						# Just here we subtract the amount from the user account
						wdb = wdb - int(widr_money)
						wr2 = wd[6] = str(wdb)
						print(f"\t\t\t Withdra Successfully New Balance Is: ${UserShowData(account_no, 6)} \n")
						# finally data write database file wd[6] column
						value_change(lines)
		# if user given (3) this part will be run (CHECK BALANCE)
		elif option_usr =="3":
			# this print show user balance on user profile
			print(f"\t\t\t Your Balance Is ${UserShowData(account_no, 6)}")
		# Transfar Money
		elif option_usr =="4":
			# if user input 4, this part will be run with this message and account balance
			print(f"\t\t\t PLEASE ENTER A ACCOUNT NUMBR {UserShowData(account_no, 0)}")
			# t_acc holds a input value given by the user as account no
			t_acc = input("\t\t\t: A/C NO: ")
			# here user given Transfar amount 
			t_amount = input("\t\t\tENTER AMOUNT: ")
			# this forloop extrct values from lines variable
			for row1 in lines:
				# this forloop also extrct values from lines variable
				for row2 in lines:
					# here we check loin user account no, if we found on database this part will be run
					if account_no in row1[0]:
						# here we check a account no given by the user
						if t_acc in row2[0]:
							# convert values str to int
							amt = int(row2[6])
							# amount has bin plus
							amt = amt + int(t_amount)
							# Here we again convert intager to string because database only accepts string values
							row2[6] = str(amt)
							t_no = int(row1[6])
							# here we subtract amount from login user
							t_no = t_no - int(t_amount)
							# convert int to str
							row1[6] = str(t_no)
							# here we create user transaction history and save into a text file
							value_change(lines)
							save_history = f"{time},{account_no},{t_acc},{t_amount},histry"
							write_data(save_history, 'a')
		# if user given (5) this part will be run PASSWORD CHANGE  
		elif option_usr =="5":
			# get 3 input from user 
			old_pass = input("\told password: ")
			new_pass = input("\tnew password: ")
			conf_pass = input("\tconfirm password: ")
			# extract data from lines variable as we define above
			for passw in lines:
				# find account no in database file if match this part will be run
				if account_no in passw:
					p = passw[4]
					if old_pass == p and new_pass == conf_pass:
						passw[4] = conf_pass
						value_change(lines)
						print("\t\t\t PASSWORD CHANGE SUCCESSFULLY\n")
						break
					else:
						print("\tPASSWORD NOT MATCH\n")
						break
		elif option_usr =="6":
			x = False
			main()

# when you login staff account, Login function will  be send on this function
def AdminDashBoard(account_no):
	x = True
	# As we have seen over and over again, we have to do this to run the loop
	while x:
		# call OpenFile function to get data 
		file = OpenFile()
		print("######################################################################\n")
		# this print showing staff account data like Balance, Account No 
		print(f"\t\t\t STAFF DASHBOARD WELLCOME {UserShowData(account_no, 1)} BALANCE ${UserShowData(account_no, 6)}\n")
		print("\t\t\t 1) SHOW ALL ACCOUNT")
		print("\t\t\t 2) SHOW STAFF ACCOUT")
		print("\t\t\t 3) DELETE ACCOUNT")
		print("\t\t\t 4) CHANGE USER ACCOUNT NO")
		print("\t\t\t 5) ACCOUNT REPORT GENERAT")
		print("\t\t\t 6) EXIT")
		# here we get a input from user as command
		admin_opt = input("\t choose: ")
		if admin_opt =="1":
			# forloop extrcting data
			for index, users in enumerate(file):
				# if user string in available it will be run
				if 'user\n' in users:
					# show all users accounts
					print(f"''\t\t\t{index}) AccuntNo:{users[0]} Username:{users[1]} Status:{users[7]}")
		elif admin_opt =="2":
			for index, staff in enumerate(file):
				if 'staff\n' in staff:
					# show all staff accounts
					print(f"\t\t\t{index}) AccuntNo:{staff[0]} Username:{staff[1]} Status:{staff[7]}")
		# if user input (3) this part will be run DELETE ACCOUNT
		elif admin_opt =="3":
			# here we get an Account no from Staff member
			dl_acc_inp = input("\t ENTER A/C NO: ")
			for dl_acc in file:
				# find account no 
				if dl_acc_inp in dl_acc:
					# if account number exist it will be deleted
					file.remove(dl_acc)
					# and write data into database file
					value_change(file)
					# show sucess message
					print(f"\n\t\t\t {dl_acc_inp} THIS ACCOUNT HISBIN REMOVED\n")
		# if user give input (4) this part will be run USER ACCOUNT NUMBER CHANGE  
		elif admin_opt =="4":
			# here we get an account number from staff member
			change_acc = input("\t ENTER A/C NO: ")
			# extrct data 
			for ch_acc in file:
				# find Account number in database
				if change_acc in ch_acc:
					# Get the account number to change
					new_acc = input("\t ENTER NEW A/C NO: ")
					# Replace the new account number with the old one
					ch_acc[0] = new_acc
					# write data in database file
					value_change(file)
		# if staff member given input (5) this part will be run GENERAT USER ACCOUNT REPORT
		elif admin_opt =="5":
			# staff member input account number, which needs a report
			inq_acc = input("\t ENTER A/C NO: ")
			# extrct data loop through
			report_data = []
			for iq_acc in file:
			# if staff given account number in database And it should be in the user's history
				if 'histry\n' in iq_acc:
					# we design user report with trepal kot string
					re = f'''
					---------------------------------------------------------------------------------------
					Recever A/C No {inq_acc} Date {iq_acc[0]} Sender A/C No {iq_acc[1]} Amount ${iq_acc[3]}
					---------------------------------------------------------------------------------------\n
					'''
					report_data.append(re)
			print("Report Generated! Check Program Folder")
			# here we write user account report into text file
			t_f = open(f"{inq_acc} Report.txt", "w")
			t_f.writelines(report_data)
			t_f.close()
		# if staff member given (6) program will be close
		elif admin_opt == "6":
			x = False
			Login()

# this function get an account no and colmnu no and return a value 
# The value that returns the function can be anything like datetime, user balance, account no
def UserShowData(acc_no, opt):
	with open('textdata.txt', 'r') as f:
	    results = []
	    for line in f:
	        words = line.split(',')
	        results.append(words) 
	    for result in results:
	    	if result[0] == acc_no:
	    		return result[opt]
	    		break
	f.close()

# here we define a OpenFile function, that function open database file and return a row given by user command 
def OpenFile():
	with open('textdata.txt', 'r') as f:
	    results = []
	    for line in f:
	        words = line.split(',')
	        results.append(words)
	    return results
	f.close()

# Here we define a write_data function, that function save data in database file as a new line mode 
# This function get 2 perameter, frist file name, and second read and write mode
def write_data(lines, mode):
	with open('textdata.txt', mode) as f:
		f.write(f'{lines}\n')
	f.close()

# this function get a list from program where user write data and save it on text file 
def value_change(lists):
	list2 = []
	for j in lists:
	    chan1 = ','.join(str(v) for v in j)
	    list2.append(chan1)
	fw = open('textdata.txt', 'w')
	fw.writelines(list2)
	fw.close()


if __name__ == '__main__':
	main()