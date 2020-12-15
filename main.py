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
# print(get_data("notification"))
# print(get_data("supporter"))

# supporterid, supportername = login_supporter()
#supportername = "Boris"
#supporterid = 1
#list_yos(supporterid, supportername)

# ADD CHALLENGE CODE HERE
def display_notifications(supporterid,yoid):
  layout = [
    [sg.Text("List of notifications")],
    [sg.Text("ID",size = (3,2)),sg.Text("YOID",size = (4,2)),sg.Text("SUPPORTER ID",size = (12,2)),sg.Text("TEXT",size = (30,2)),sg.Text("RECEIVED DATA",size = (13,2))], 
    [sg.Button("Close")]


  ]
  window = sg.Window("Notifications",size = (800,400)).Layout(layout)
  while True:
    event,values = window.read()
    if event == 'Close':
      break
  window.close()




display_notifications("2","1")




