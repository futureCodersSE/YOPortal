import PySimpleGUI as sg
from datahandlers import get_data
from operator import itemgetter

def get_notification_data(yoid):
  selected_yoid = []
  notification_list = get_data("notification")
  for notification in notification_list:
    if notification['YOID'] == str(yoid):
      selected_yoid.append(notification)
  sorted_list = sorted(selected_yoid, key=itemgetter('RECEIVEDDATE'),reverse = True)
  print(yoid)
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