import PySimpleGUI as sg
from datahandlers import get_data

# Dee
def display_tasks(yo_details):
  # get list of all tasks for this yo
  task_list = get_data('task')
  layout = [
    [sg.Text('List of tasks for '), sg.Text(yo_details["NAME"]), sg.Text(yo_details["SURNAME"])],
    [sg.Text('ID',size=(3,2)),sg.Text('TASK NAME',size = (15,2)), sg.Text('DESCRIPTION',size = (38,2)),sg.Text('TARGETDATE',size=(13,2)), sg.Text('ACHIEVED', size=(10,2)), sg.Text('VERIFIED', size=(10,2))],
    ]

  for task in task_list:
    if task['YOID'] == yo_details["ID"]:
      row = [sg.Text(task['ID'],size=(3,2)),sg.Text(task['TASKNAME'],size = (15,2)),sg.Text(task['DESCRIPTION'],size=(38,2)), sg.Text(task['TARGETDATE'], size=(13,2)), sg.Text(task['ACHIEVED'], size=(10,2)), sg.Text(task['VERIFIED'], size=(10,2)) ]
      layout.append(row)
  layout.append([sg.Button('Close', size=(15,2))])

  window = sg.Window('Tasks', size = (800,400)).Layout(layout)
  while True:
    event, values = window.read()
    if event == 'Close':   
      break
  window.close()

  #playing code
  #Get list of notifications for yo & supporter
"""
def display_notifications(supporterid, yoid):
  notification_list = get_data('notification')
  notification_list2 = []  
  for n in notification_list:     
    if n['SUPPORTERID'] == supporterid and n['YOID'] == yoid:
      notification_list2.append(n)
    print(notification_list2)
  return notification_list2

#print(display_notifications('1','2'))

def display_tasks(yoid):
  # get list of all tasks for this yo
  task_list = get_data('task')
  task_list2 = []
  
  for task in task_list:
    if task['YOID'] == yoid:
        task_list2.append(task)
  return task_list2
yo_list = display_tasks('3')
print(yo_list)

#VERIFY A TASK - LOGIC
# 1. find tasks for YO where achieved is equal to "Y”
# 2. Find the ID for the task / the individual task
# 2. change the "N" value to "Y" to confirm task is verified
# 3. save the changes back to the record on the data file.

def display_tasks(yoid):
  # get list of all tasks for this yo
  task_list = get_data('task')
  to_be_verified = []
  #find tasks that are achieved for yo & change verified to Y
  for task in task_list:
    if task['YOID'] == yoid and task['ACHIEVED'] == 'Y':      
      to_be_verified.append(task)      
      task['VERIFIED'] = 'Y'      
      #print (to_be_verified)
   
    return to_be_verified
print(display_tasks('1'))
"""
#IDENTIFY OVERDUE TASKS - LOGIC
# 1. identify tasks that have passed target dates
# 2. create a variable to hold the current date and time
# 3. Compare targetdate record to the variable
# 4. if the target date is before the current date, then change the colour of the whole record
# consider moving the red tasks to the top of the list

# from datetime import date
# def overdue_task(yoid, taskid):
#   # get list of all tasks for this yo
#   task_list = get_data('task')
#   overdue_task_list = []
#   #compare dates
#   today = date.today()
#   for task in task_list:
#     if task['TARGETDATE'] < today:
#       overdue_task_list.append(task['TARGETDATE'])
#   return overdue_task_list

# print(overdue_task('1','1'))

    
#     # message_colour = "red"
#     # task['TARGETDATE'] == message_colour





