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
def get_YO_details(yoid):
  yos_list = get_data("yos")
  for yos in yos_list: 
    if yos["ID"] == str(yoid):
      name, surname, email, logged_in = get_YO_user_info(yos["USERID"])
      message_count, some_urgent = get_unread_message_info(yos["ID"], yos["SUPPORTERID"])
      YO_details = {'ID': yos["ID"], 'USERID': yos["USERID"], 'SUPPORTERID': yos["SUPPORTERID"], 'EMOTION': yos["EMOTION"], 'STARTDATE': yos["STARTDATE"],'NAME': name, 'SURNAME': surname, 'EMAIL': email, 'LOGGEDIN': logged_in, 'MESSAGECOUNT': message_count, 'SOMEURGENT': some_urgent}
      return YO_details

print(get_YO_details(4))




