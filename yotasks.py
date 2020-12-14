import PySimpleGUI as sg
from datahandlers import get_data

def display_tasks(yoid):
  # get list of all tasks for this yo
  task_list = get_data('task')
  layout = [
    [sg.Text('List of tasks for selected YO')],
    [sg.Text('ID',size=(3,2)),sg.Text('TASK NAME',size = (15,2)), sg.Text('DESCRIPTION',size = (38,2)),sg.Text('TARGETDATE',size=(13,2)), sg.Text('ACHIEVED', size=(10,2)), sg.Text('VERIFIED', size=(10,2))],
    ]

  for task in task_list:
    if task['YOID'] == yoid:
      row = [sg.Text(task['ID'],size=(3,2)),sg.Text(task['TASKNAME'],size = (15,2)),sg.Text(task['DESCRIPTION'],size=(38,2)), sg.Text(task['TARGETDATE'], size=(13,2)), sg.Text(task['ACHIEVED'], size=(10,2)), sg.Text(task['VERIFIED'], size=(10,2)) ]
      layout.append(row)
  layout.append([sg.Button('Close', size=(15,2))])

  window = sg.Window('Tasks', size = (800,400)).Layout(layout)
  while True:
    event, values = window.read()
    if event == 'Close':   
      break
  window.close()