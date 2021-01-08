# Portal app to work with goals database
from datahandlers import get_data
from login import login_supporter
from yolist import list_yos
from datahandlers import update_data

# main program
# print(get_data("yos"))
# print(get_data("message"))
# print(get_data("task"))
# print(get_data("user"))
# print(get_data("goal"))
#print(get_data("notification"))
# print(get_data("supporter"))

# supporterid, supportername = login_supporter()
# supportername = "Boris"
# supporterid = 1
# list_yos(supporterid, supportername)

# ADD CHALLENGE CODE HERE
# Get notifications data
# Select notifications for YO
# return notifications list
# Expected test results
# [{'1','3','1','Interview tomorrow','14/12/2020'},
# {'5','3','1','Appointment for house viewing this Friday','16/12/2020'}]
import PySimpleGUI as sg
from operator import itemgetter

def get_notification_data(yoid):
  selected_yoid = []
  notification_list = get_data("notification")
  for notification in notification_list:
    if notification['YOID'] == str(yoid):
      selected_yoid.append(notification)
  sorted_list = sorted(selected_yoid, key=itemgetter('RECEIVEDDATE'),reverse = True)
  return (sorted_list)

def display_notifications(yoid):
  layout = [
    [
      sg.Text("NOTIFICATIONS", size=(15,1), font=("Helvetica",18,"bold")),
      sg.Button("add notification",size=(20,2)),
      sg.Button('Logout', size=(20,2))
    ]
  ]
  notification_list = get_notification_data(yoid)
  for notification in notification_list:
    layout.append([sg.Text(notification["RECEIVEDDATE"], background_color = "black", size=(80,1))])
    layout.append([sg.Text(notification["TEXT"])])
    layout.append([sg.Text('_'*92)])
  layout.append([sg.Button('Close', size=(20,2))])
  window = sg.Window('Notifications', size=(600,350)).Layout(layout)
  while True:
    event,values = window.read()
    if event == "add notification":
      add_new_notification(yoid)
    if event == 'Close':
      break
  window.close()

def add_new_notification(yoid):
  layout = [
    [
      sg.Text("ADD A NOTIFICATION", size=(23,1), font=("Helvetica",16,"bold")),
      sg.Button('Log-out', size=(17,1))
    ],
    [
      sg.Text("Notification title", size=(14,1), font=("Helvetica",11,"bold")),
      sg.Text('_'*56)
    ],
    [
     sg.Input("", size=(68,1)),
    ],
    [
      sg.Text("Level Of Urgency", size=(14,1), font=("Helvetica",11,"bold")),
      sg.Text('|'*1),
      sg.Text("Action Needed Date", size=(16,1), font=("Helvetica",11,"bold")),
      sg.Text('|'*1),
      sg.Text("Reminder Date", size=(15,1), font=("Helvetica",11,"bold")),
    ],
    [
      sg.Input("", size=(21,1)),
      sg.Input("",key="actiondate", size=(23,1)),
      sg.Input("", size=(21,1)),
    ],
    [
      sg.Text("Difficulty Level", size=(14,1), font=("Helvetica",11,"bold")),
      sg.Text('_'*56)
    ],
    [
      sg.Input("", size=(68,1)),
    ],
    [
      sg.Text("Reminders", size=(14,1), font=("Helvetica",11,"bold")),
      sg.Text('_'*56)
    ],
    [
      sg.Input("", size=(68,1)),
    ],
    [
      sg.Text("information", size=(14,1), font=("Helvetica",11,"bold")),
      sg.Text('_'*56)
    ],
    [
      sg.Input("",key="text", size=(68,1)),
    ]
  ]
  
  layout.append([sg.Button('Close', size=(20,2)), sg.Button('Save', size=(10,2))])
  window = sg.Window('ADD A NOTIFICATION', size=(600,350)).Layout(layout)
  while True:
    event, values = window.read()
    if event == 'Save':
        notification_list = get_data("notification")
        new_id = len(notification_list) + 1
        new_notification ={
          "ID":str(new_id),
          "YOID":str(yoid),
          "SUPPORTERID":"1",
          "TEXT":values["text"],
          "RECEIVEDDATE":values["actiondate"], 
        }
        notification_list = get_data("notification")
        notification_list.append(new_notification)
        notification_list = update_data('notification',notification_list)
        print(new_notification)
    if event == 'Close':   
      break
  window.close()

#main program
display_notifications(3)
add_new_notification(3)