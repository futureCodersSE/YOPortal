import PySimpleGUI as sg
from datahandlers import get_data

def display_goal(yoid):
  goal_list = get_data("goal")
  for goal in goal_list: 
    if goal["YOID"] == str(yoid):
      YOgoal = goal
      break

  layout = [
    [sg.Text("GOAL DETAILS", size=(28,1), font = ("Helvetica", 18, "bold")), sg.Button("LOG OUT")],
    [sg.Text("_"*92)],
    [sg.Text("GOAL NAME", size=(20,2), font = ("Helvetica", 14)), sg.Text(YOgoal["GOALNAME"], size=(25,2), font = ("Helvetica", 14, "bold"))],
    [sg.Text("DESCRIPTION", size=(20,4), font = ("Helvetica", 14)), sg.Text(YOgoal["DESCRIPTION"], size=(25,4), font = ("Helvetica", 14, "bold"))],
    [sg.Text("TARGET DATE", size=(20,2), font = ("Helvetica", 14)), sg.Text(YOgoal["TARGETDATE"], size=(25,2), font = ("Helvetica", 14, "bold"))],
    [sg.Text("ACHIEVED", size=(20,2), font = ("Helvetica", 14)), sg.Text(YOgoal["ACHIEVED"], size=(25,2), font = ("Helvetica", 14, "bold"))],
    [sg.Button("EDIT"), sg.Button("CLOSE")],
  ]

  window = sg.Window("Young Offenders Goals", size=(600,400)).Layout(layout)
  while True: 
    event, values = window.read()
    if event == 'CLOSE':
      break
  window.close()