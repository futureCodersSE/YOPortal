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

def edit_task(task):
  #task_list = get_data("task")
  layout = [
    [sg.Text("EDIT / ADD TASK", size=(28,2), font = ("Helvetica", 18, "bold")), sg.Button("LOG OUT")],
    [sg.Text("Task Name", size=(25,2)), sg.Input(task["TASKNAME"])],
    [sg.Text("Description", size=(25,2)), sg.Multiline(task["DESCRIPTION"], size=(None,6))],
    [sg.Text("Target date", size=(25,2)), sg.Input(task["TARGETDATE"])],
    [sg.Text("Achieved", size=(25,2)), sg.Checkbox("", size=(100,10), disabled = True, default = task["ACHIEVED"] == "Y")],
    [sg.Text("Verified", size=(25,2)), sg.Checkbox("", size=(100,10), default = task["VERIFIED"] == "Y")],
    


    [sg.Button("SAVE"), sg.Button("CANCEL")],


  ]

  window = sg.Window("EDIT TASK", size=(600,400)).Layout(layout)
  while True: 
    event, values = window.read()

  window.Close()


task = {"ID":"1", "YOID":"1", "GOALID": "1", "TASKNAME": "Write CV", "DESCRIPTION":"Complete a CV to be used for a job application. Be thorough in your CV", "TARGETDATE":"12/12/2020", "ACHIEVED":"Y", "VERIFIED":"N"}

edit_task(task)


