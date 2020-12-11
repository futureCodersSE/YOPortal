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