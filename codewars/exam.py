# create account 
account = []
name = input("Enter your name: ")
lastname = input("Enter your lastname: ")
age = int(input("Enter your age: "))
number = int(input("Enter your phone number: "))
email = input("Enter your email: ")
password = input("Enter new password: ")

account.append(name)
account.append(lastname)
account.append(age)
account.append(number)
account.append(email)
account.append(password)

print(account)




print("registration completed successfully")
print("Now log in")
# now log in 
log_in = False

while log_in != True:
    user_input_email = input("Ente your email:  ")
    if user_input_email == email:
       print("correct")

    else:
        print("incorrect email, try again")
    user_input_pass = input("Enter your password: ")
    if user_input_pass == password:
        print("You are logged in ")
        log_in = True
    else:
        print("incorrect password, try again")


# transaction  


account_balance1 = []
account_balance2 = []
account_id = []

balance  = int(input("Enter your balance ($): "))
account_balance1.append(balance)

transaction = input("Where do you want to transact money?(enter his id): ")
account_id.append(transaction)


transact = int(input("How much money do you want to transact?($): "))
account_balance2.append(transact)
print("Transaction completed successfully")


# accounts

# print(account)
# print(account_balance1)
# print(account_balance2)
# print(account_id)

# delete acc 

print("delete account")

print(" 1. account" )
print(" 2. account_balance1" )
print(" 3. account_balance2" )
print(" 4. account_id ") 
print("Enter number beetwen 1-4!") 
user = int(input("Wich account you want delete?: "))



if user == 1:
    account.clear
    print("account deleted")
elif user == 2:
    account_balance1.clear
    print("account deleted")
elif user == 3:
    account_balance2.clear
    print("account deleted")
elif user == 4:
    account_id.clear
    print("account deleted")
else:
    print("Enter number beetwen 1-4!")

# exit system


print("1. yes")
print("2. no")
exit = int(input("Do you want exit system? "))

if exit == 1:
    print("bye")
else:
    print("You are still logged in ")



