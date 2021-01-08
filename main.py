# Portal app to work with goals database
from datahandlers import get_data,update_data
from login import login_supporter
from yolist import list_yos
import PySimpleGUI as sg


# main program
# print(get_data("yos"))
# print(get_data("message"))
# print(get_data("task"))
# print(get_data("user"))
# print(get_data("goal"))
#print(get_data("notification"))
# print(get_data("supporter"))

# supporterid, supportername = login_supporter()
"""
supportername = "Boris"
supporterid = 1
list_yos(supporterid, supportername)

# ADD CHALLENGE CODE HERE
# Get notifications data
# Select notifications for YO
# return notifications list
# Expected test results
# [{'1','3','1','Interview tomorrow','14/12/2020'},
# {'5','3','1','Appointment for house viewing this Friday','16/12/2020'}]

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
      sg.Text("NOTIFICATIONS", size=(22,1), font=("Helvetica",18,"bold")),
      sg.Button('Log-out', size=(20,2))
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
    if event == 'Close':
      break
  window.close()
  """
# Portal app to work with goals database
from datahandlers import get_data
from login import login_supporter
from yolist import list_yos
import PySimpleGUI as sg

# main program
# print(get_data("yos"))
# print(get_data("message"))
# print(get_data("task"))
# print(get_data("user"))
# print(get_data("goal"))
#print(get_data("notification"))
# print(get_data("supporter"))

# supporterid, supportername = login_supporter()

supportername = "Boris"
supporterid = 1
list_yos(supporterid, supportername)
"""
# ADD CHALLENGE CODE HERE
# Get notifications data
# Select notifications for YO
# return notifications list
# Expected test results
# [{'1','3','1','Interview tomorrow','14/12/2020'},
# {'5','3','1','Appointment for house viewing this Friday','16/12/2020'}]

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
      sg.Text("NOTIFICATIONS", size=(22,1), font=("Helvetica",18,"bold")),
      sg.Button('Log-out', size=(20,2))
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
    if event == 'Close':
      break
  window.close()
  """
def edit_goal(yoid):
  goal_list = get_data('goal')
  for g in goal_list:
    if g["YOID"] == str(yoid):
      goal = g
  layout = [
    [
      sg.Text("EDIT GOALS", size= (22,1), font= ("Helvetica",18,"bold")),
      sg.Button('Logout',size=(20,2))
    ],
    [sg.Text('_'*92)],
    [sg.Text("GOAL NAME")],
    [sg.Input(goal["GOALNAME"],size=(80,1))],
    [sg.Text("DESCRIPTION")],
    [sg.Multiline(goal["DESCRIPTION"],size=(80,2))],
    [sg.Text("TARGET DATE")],
    [sg.Input(goal["TARGETDATE"],size=(80,1))],
    [sg.Text('_'*92)],
    [sg.Button('Save',size=(20,2)),sg.Button('Cancel',size=(20,2))]
  ]
  window = sg.Window('EDIT Goals',size= (600,350)).Layout(layout)
  while True:
    event,values = window.read()
    if event == 'Save':
      for g in goal_list:
        if g["YOID"] == str(yoid):
          g["GOALNAME"] = values[goal["GOALNAME"]]
          g["DESCRIPTION"] = values[goal["DESCRIPTION"]]
          g["TARGETDATE"] = values[goal["TARGETDATE"]]
        break
      goal_list = update_data("goal",goal_list)
  
    if event == 'Cancel':
      break
  window.close()

#main program
#display_notifications(3)
edit_goal(1)

""