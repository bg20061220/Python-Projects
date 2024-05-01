passwordDict = { }
user_action= input("Do you want to add a new PassWord ? (yes or no ) : ").lower()
while user_action == 'yes':
    account_name = input("Please enter the account for which the password is : ")
    password_name = input("Please  enter the password for your account : ")
    passwordDict[account_name] = password_name
    print("Password Added")
    user_action = input("Do you want to add a new password ? (yes / no ) : ").lower()
    if user_action == "no" :
        break
if user_action == "no ":
    user_action2 = input("Do you want to update a password (yes / no )  : ").lower()
    if user_action2 == "yes" :
       updatedaccount_name = input("Please enter the account to be updated  : ")
       updatedpassword = input("Please enter the new password : ")
       if updatedaccount_name in passwordDict :
           passwordDict[updatedaccount_name] = updatedpassword
print(passwordDict)           
