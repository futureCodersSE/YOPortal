import PySimpleGUI as sg
from helpers import get_emotion_image, get_YO_details
from yotasks import display_tasks
from yonotifications import display_notifications


def show_yo_profile(yoid):
  # show profile for selected YO
  yo_details = get_YO_details(yoid)
  yo_header = "YO " + yo_details["NAME"] + " " + yo_details["SURNAME"] + " profile"
  urgent = "red" if yo_details["SOMEURGENT"] else "white"
  messages_text = "Messages: " + str(yo_details["MESSAGECOUNT"])
  online_colour = "green" if yo_details["LOGGEDIN"] else "gray"
  emotion_colour = "green" if yo_details["EMOTION"] == "5" else "lightgreen" if yo_details["EMOTION"] == "4" else "yellow" if yo_details["EMOTION"] == "3" else "orange" if yo_details == "2" else "red"

  layout = [
    [
      sg.Image(get_emotion_image(yo_details["EMOTION"]), size=(40,40), background_color=emotion_colour),
      sg.Text("",size=(20,1)), sg.Text(yo_details["NAME"], font=('Helvetica', 12, 'bold')),sg.Text(yo_details["SURNAME"],size=(30,1), font=('Helvetica', 12, 'bold')), 
      sg.Button("Online", button_color=("black",online_colour), size=(20,3))
    ],
    [sg.Text("", size=(20,3)), sg.Button(messages_text, button_color=(urgent,"black"), font=('Helvetica', 12, 'bold'), size=(42,3))],
    [
      sg.Text("", size=(20,3)), 
      sg.Button("Notifications", button_color=("black", "yellow"), font=('Helvetica', 12, 'bold'), size=(20,3)),
      sg.Button("Tasks", button_color=("black", "orange"), font=('Helvetica', 12, 'bold'), size=(20,3))
    ],
    [
      sg.Text("", size=(20,3)),
      sg.Button("Goal", button_color=("black", "orange"), font=('Helvetica', 12, 'bold'), size=(20,3)),
      sg.Button(" Audit Logs  ",button_color=("black", "yellow"), font=('Helvetica', 12, 'bold'), size=(20,3))
    ],
    [sg.Text("", size=(20,1))],
    [sg.Button('Close', size=(15,2))]
  ]

  window = sg.Window(yo_header, size=(800,400)).Layout(layout)

  # wait for a button to be clicked and handle it
  while True:
    event,values = window.read()
    print(event)
    if event == 'Tasks':
      display_tasks(yo_details)
    elif event == 'Notifications':
      display_notifications(yoid)
    if event == 'Close':
      break
  window.close()


