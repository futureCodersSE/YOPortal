# Portal app to work with goals database
#from datahandlers import get_data

# main program
#print(get_data("yos"))
#print(get_data("message"))
#Harrison's
#print(get_data("task"))
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
