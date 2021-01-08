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

# get goals data, then find goal allocated to yoid. for loop
# # ID,YOID,GOALNAME,DESCRIPTION,TARGETDATE,ACHIEVED
# 1,1,Job,Get a job,1/2/2020,N
# 2,2,Housing,Secure a home,2/1/2020,N
# 3,3,Job,Get a job,30/1/2020,N
# 4,4,Apprenticeship,Start an apprenticeship,16/2/2020,N


def show_goals(yoid):
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

  window.Close()

show_goals(3)








# def edit_task(task):
#   #task_list = get_data("task")
#   layout = [
#     [sg.Text("EDIT / ADD TASK", size=(28,2), font = ("Helvetica", 18, "bold")), sg.Button("LOG OUT")],
#     [sg.Text("Task Name", size=(25,2)), sg.Input(task["TASKNAME"])],
#     [sg.Text("Description", size=(25,2)), sg.Multiline(task["DESCRIPTION"], size=(None,6))],
#     [sg.Text("Target date", size=(25,2)), sg.Input(task["TARGETDATE"])],
#     [sg.Text("Achieved", size=(25,2)), sg.Checkbox("", size=(100,10), disabled = True, default = task["ACHIEVED"] == "Y")],
#     [sg.Text("Verified", size=(25,2)), sg.Checkbox("", size=(100,10), default = task["VERIFIED"] == "Y")],
    


#     [sg.Button("SAVE"), sg.Button("CANCEL")],


#   ]

#   window = sg.Window("EDIT TASK", size=(600,400)).Layout(layout)
#   while True: 
#     event, values = window.read()

#   window.Close()


# task = {"ID":"1", "YOID":"1", "GOALID": "1", "TASKNAME": "Write CV", "DESCRIPTION":"Complete a CV to be used for a job application. Be thorough in your CV", "TARGETDATE":"12/12/2020", "ACHIEVED":"Y", "VERIFIED":"N"}

# edit_task(task)


