# Portal app to work with goals database
from datahandlers import get_data
from login import login_supporter
from yolist import list_yos

# main program
# print(get_data("yos"))
# print(get_data("message"))
# print(get_data("task"))
# print(get_data("user"))
# print(get_data("goal"))
# print(get_data("notification"))
# print(get_data("supporter"))

# supporterid, supportername = login_supporter()
# supportername = "Boris"
# supporterid = 1
# list_yos(supporterid, supportername)

# ADD CHALLENGE CODE HERE

def get_YO_user_info(userid):
#get user with an ID of userid
  name = ""
  surname = ""
  email = ""
  logged_in = False

  user_list = get_data("user")
  for user in user_list:
    if user["ID"] == str(userid):
      name = user["NAME"]
      surname = user["SURNAME"]
      email = user["EMAIL"]
      if user["LOGGEDIN"] == "Y":
        logged_in = True
      
  return name, surname, email, logged_in

name, surname, email, logged_in = get_YO_user_info(3)
print(name, surname, email, logged_in)