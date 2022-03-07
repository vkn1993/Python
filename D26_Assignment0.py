

def validate_mail(email):
  
  username_validaity_final = -1
  user_mail= email.split("@")
  
  if user_mail[1].startswith("."):

    username_validaity_final ==0
  
  if email.endswith("@gmail.com") or email.endswith("@yahoo.in") or email.endswith("@outlook.com") or email.endswith("@icloud.com")or email.endswith("@live.com") :
    
    user_mail = email.split("@")
    user_name= user_mail[0]
    flag_x =0
    
    for x in user_name:
      if x == "." :
        user_mail_1 = user_name.split(".")
        flag_x =1
        break
      
      if x == "_":
        user_mail_1 = user_name.split("_")
        flag_x = 1
        break
        
    if flag_x == 1:
      len_1 = len(user_mail_1)
      flag_1 = 0
      
      for k in range (len_1):
        if user_mail_1[k].isalnum()==1:
          flag_1 =1
        else:
          flag_1 =0         
          
      if flag_1 ==1:
        
        username_validaity_final = 1
        
      else:
        username_validaity_final = 0
      
    else:
      
      if user_name.isalnum() == 1:
        
        username_validaity_final = 1
      
      else:
        username_validaity_final = 0
      
  else:
    username_validaity_final = 0
  
  return username_validaity_final


def validate_password(password):

  import re

  flag = 0
  password_validity = -1
  while True:  
    if (len(password)>16) or (len(password)<5) :
        flag = -1
        break
    elif not re.search("[a-z]", password):
        flag = -1
        break
    elif not re.search("[A-Z]", password):
        flag = -1
        break
    elif not re.search("[0-9]", password):
        flag = -1
        break
    elif not re.search("[_@$]", password):
        flag = -1
        break
    elif re.search("\s", password):
        flag = -1
        break
    else:
        flag = 0
        password_validity = 1
        break
        
  if flag ==-1:
    
    password_validity = 0
  
  return password_validity

def store_data(user_dict):

  with open('User_Details.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in user_dict.items():
       writer.writerow([key, value])

def search_data(data1):
  data_exist = 0
  with open('User_Details.csv') as csv_file:
    reader = csv.reader(csv_file)
    mydict = dict(reader)

  for user_mailid,user_pass_word in mydict.items():

    if user_mailid == data1:

      data_exist = 1
      break
          
    else:

      data_exist =0

  return data_exist

def validate_login(loginid,loginpass):
  user_validation =0
  with open('User_Details.csv') as csv_file:
    reader = csv.reader(csv_file)
    mydict = dict(reader)
  
  for user_mailid,user_pass_word in mydict.items():

    if user_mailid == loginid:

      if user_pass_word == loginpass:

        user_validation = 1
        break
      else:

        user_validation = 0
    else:
      user_validation = 0
  
  return user_validation




#Driver Code:

import csv
csv_columns = ['UserId','Password']
user_data = {}


while True:
  print("\n")
  print("1.Registration")
  print("2.Login")
  print("3.Forgot Password")   
  print("4:Exit") 
    
  userinput= input(print("Enter the action to be done (1-4): "))
    
  if userinput.isnumeric() ==1:
    userinput = int(userinput)
      
  else:
    print("Enter an integer from the 1 to 4 depending on the action to be taken")
      
  if userinput == 1:
    userin = input(print("Enter mail"))
    v1 = validate_mail(userin)
    
    if v1 ==1:
      user_pass = input(print("Enter password"))
      v2 = validate_password(user_pass)
        
      if v2==1:
        print("Email and Password verified.")

        if userin in user_data:
          print("Username already exist")
        else:
          user_data[userin] =  user_pass
          store_data(user_data)
      else:
        print("Enter valid Password")
    else:
      print("Enter valid mail id")
  

  elif userinput ==2:

    user_login = input(print("Enter login id : "))
    login_pass = input(print("Enter password: "))

    lg_1 = validate_mail(userin)

    if lg_1 == 1:

      lg_2 = validate_login(user_login,login_pass)

      if lg_2 ==1:

        print("Login Successful")

      else:

        print("Login Failed")
        print("Enter correct mailid and password")

    else:
      print("Invalid login id")
    
  
  elif userinput ==3:

    user_login_id = input(print("Enter login id : "))
    ui_3  = search_data(user_login_id)

    if ui_3 ==1:

      new_password = input(print("Enter new password: "))
      ui_31 = validate_password(new_password)

      if ui_31 == 1:
        
        print("Password changed successfully. Proceed to login")
        user_data[user_login_id] =  new_password

      else:

        print("Invalid Password")

    else:

      print("Mail id not found. Proceed to Registration")

  elif userinput ==4:
    break
  
  else:

    print("Incorrect Choice")
