import PySimpleGUI as sg
from datahandlers import get_data
from helpers import get_emotion_image, get_YO_details



def show_yo_profile(yoid):
  # show profile for selected YO
  yo_details = get_YO_details(yoid)
  yo_header = "YO " + yo_details["NAME"] + " " + yo_details["SURNAME"] + " profile"
  urgent = "red" if yo_details["SOMEURGENT"] else "white"
  messages_text = "Messages: " + str(yo_details["MESSAGECOUNT"])
  online_colour = "green" if yo_details["LOGGEDIN"] else "gray"
  online_text = "online" if yo_details["LOGGEDIN"] else "offline"
  emotion_colour = "green" if yo_details["EMOTION"] == "5" else "lightgreen" if yo_details["EMOTION"] == "4" else "yellow" if yo_details["EMOTION"] == "3" else "orange" if yo_details == "2" else "red"

  layout = [
    [
      sg.Image(get_emotion_image(yo_details["EMOTION"]), size=(40,40), background_color=emotion_colour),
      #sg.Button(button_color=("gray","gray"), image_filename=get_emotion_image(yo_details["EMOTION"]),image_size=(60,60)),
      sg.Text("",size=(20,1)), sg.Text(yo_details["NAME"], font=('Helvetica', 12, 'bold')),sg.Text(yo_details["SURNAME"],size=(30,1), font=('Helvetica', 12, 'bold')), 
      sg.Button("Online", button_color=("black",online_colour), size=(20,3))
    ],
    [sg.Text("", size=(20,3)), sg.Button(messages_text, button_color=(urgent,"black"), font=('Helvetica', 12, 'bold'), key=yo_details["ID"], size=(42,3))],
    [
      sg.Text("", size=(20,3)), 
      sg.Button("Notifications", button_color=("black", "yellow"), font=('Helvetica', 12, 'bold'), key=yo_details["ID"], size=(20,3)),
      sg.Button("Tasks", button_color=("black", "orange"), font=('Helvetica', 12, 'bold'), key=yo_details["ID"], size=(20,3))
    ],
    [
      sg.Text("", size=(20,3)),
      sg.Button("Goals", button_color=("black", "orange"), font=('Helvetica', 12, 'bold'), key=yo_details["ID"], size=(20,3)),
      sg.Button(" Audit Logs  ",button_color=("black", "yellow"), font=('Helvetica', 12, 'bold'), key=yo_details["ID"], size=(20,3))
    ],
    [sg.Text("", size=(20,1))],
    [sg.Button('Close', size=(15,2))]
  ]

  window = sg.Window(yo_header, size=(800,400)).Layout(layout)

  # wait for a button to be clicked and handle it
  while True:
    event,values = window.read()
    if event == 'Close':
      break
  window.close()

