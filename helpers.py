from datahandlers import get_data


def get_YO_user_info(userid):
#Joe and Isaac
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

def get_emotion_image(emotion):
  # Harrison
  # return correct image for icon
  if emotion == "1":
    return "images/verysad.png"
  elif emotion == "2":
    return "images/slightlysad.png"
  elif emotion == "3":
    return "images/ok.png"
  elif emotion == "4":
    return "images/mildlyhappy.png"
  elif emotion == "5":
    return "images/veryhappy.png"
  else:
    return "Unknown emotion" ##


# get number of messages and if any are urgent
def get_unread_message_info(yoid, supporterid):
  message_list = get_data("message")
  message_count = 0
  some_urgent  = False
  for message in message_list:
    if message["YOID"] == yoid and message["SUPPORTERID"] == supporterid:
      if message["READ"] == "unread":
        message_count += 1
        if message["URGENT"] == "urgent":
          some_urgent = True
  return message_count, some_urgent

def get_YO_details(yoid):
  yos_list = get_data("yos")
  for yos in yos_list: 
    if yos["ID"] == str(yoid):
      name, surname, email, logged_in = get_YO_user_info(yos["USERID"])
      message_count, some_urgent = get_unread_message_info(yos["ID"], yos["SUPPORTERID"])
      YO_details = {'ID': yos["ID"], 'USERID': yos["USERID"], 'SUPPORTERID': yos["SUPPORTERID"], 'EMOTION': yos["EMOTION"], 'STARTDATE': yos["STARTDATE"],'NAME': name, 'SURNAME': surname, 'EMAIL': email, 'LOGGEDIN': logged_in, 'MESSAGECOUNT': message_count, 'SOMEURGENT': some_urgent}
      return YO_details


