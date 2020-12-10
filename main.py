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

def get_emotion_image(emotion):
  if emotion == 1:
    return "images/very_sad.png"
  elif emotion == 2:
    return "images/slightly_sad.png"
  elif emotion == 3:
    return "images/ok.png"
  elif emotion == 4:
    return "images/happy.png"
  elif emotion == 5:
    return "images/very_happy.png"
  else:
    return "Enter number between 1 and 5"
emotion1 = get_emotion_image (5)
emotion2 = get_emotion_image (4)
emotion3 = get_emotion_image (3)
emotion4 = get_emotion_image (2)
emotion5 = get_emotion_image (1)

print(emotion1)
print(emotion2)
print(emotion3)
print(emotion4)
print(emotion5)
