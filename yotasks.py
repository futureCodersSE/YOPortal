import PySimpleGUI as sg
from datahandlers import get_data

# goal is achieved if all tasks have achieved and verified set to 'Y'
# Isaac/Karen
def calculate_goal_achieved(goalid): 
  goal_list = get_data("goal")
  all_achieved_verified = True 
  task_list = get_data("task")
  for task in task_list:
    if task["GOALID"] == str(goalid):
      if task["ACHIEVED"] == "N" or task["VERIFIED"] == "N":
        all_achieved_verified = False 
  if all_achieved_verified: 
    for goal in goal_list:
      if goal["ID"] == str(goalid):
        goal["ACHIEVED"] = "Y"
        print(update_data("goal", goal_list))

# Isaac
def edit_task(taskid):
  # get task from id
  task_list = get_data("task")
  for t in task_list:
    if t["ID"] == str(taskid):
      task = t
      break

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
    if event == "SAVE": 
      calculate_goal_achieved(task["GOALID"])
    if event == "CANCEL": 
      break 
  window.Close()

# Dee
def display_tasks(yo_details):
  # get list of all tasks for this yo
  task_list = get_data('task')
  # sort task list
  layout = [
    [
      sg.Text('TASK LIST: ', font=('Helvetica',18,'bold'), size=(20,2)),
      sg.Text(yo_details['NAME'] + ' ' + yo_details['SURNAME'], size=(25,2)),
      sg.Button('Logout', size=(20,2))
    ],
    [sg.Text('_'*100)],
    [sg.Text('ID',size=(3,2)),sg.Text('TASK NAME',size = (15,2)), sg.Text('DESCRIPTION',size = (30,2)),sg.Text('TARGETDATE',size=(13,2)), sg.Text('ACHIEVED', size=(10,2)), sg.Text('VERIFIED', size=(10,2))],
    ]

  for task in task_list:
    if task['YOID'] == yo_details["ID"]:
      row = [sg.Text(task['ID'],size=(3,3)),sg.Text(task['TASKNAME'],size = (15,3)),sg.Text(task['DESCRIPTION'],size=(30,3)), sg.Text(task['TARGETDATE'], size=(13,3)), sg.Text(task['ACHIEVED'], size=(10,3)), sg.Text(task['VERIFIED'], size=(10,3)),
      sg.Button('Edit', key='task-' + task['ID']) ]
      layout.append(row)
  layout.append([sg.Button('Close', size=(20,3))])

  window = sg.Window('Tasks', size = (800,600)).Layout(layout)
  while True:
    event, values = window.read()
    if event.find('task-') != -1:
      taskid = event.split('-')[1]
      edit_task(taskid)
    if event == 'Close':   
      break
  window.close()