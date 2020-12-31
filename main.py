# Portal app to work with goals database
from datahandlers import get_data, update_data
from login import login_supporter
from yolist import list_yos
from display_yo import receive_messages
from yotasks import display_tasks

# main program
# print(get_data("yos"))
# print(get_data("message"))
# print(get_data("task"))
# print(get_data("user"))
# print(get_data("goal"))
# print(get_data("notification"))
# print(get_data("supporter"))

# # supporterid, supportername = login_supporter()
# supportername = "Boris"
# supporterid = 1
# list_yos(supporterid, supportername)

# ADD CHALLENGE CODE HERE
def add_task(yoid, goalid, taskname, description, targetdate):  
  #get the next available id
  task_list = get_data('task')
  last_task_in_list = task_list[-1]
  next_id_for_task = int(last_task_in_list['ID']) + 1
  
  #new dict for task and add data
  new_task = {
    'ID':str(next_id_for_task),
    'YOID': yoid,
    'GOALID':goalid,
    'TASKNAME':taskname,
    'DESCRIPTION':description,
    'TARGETDATE':targetdate,
    'ACHIEVED':'N',
    'VERIFIED':'N',
  }
  
  #add task to end of task_list & data
  task_list.append(new_task)
  
  #overwrite yop-task.csv
  task_list = update_data('task',task_list) 
  
add_task('1','1', 'Complete course', 'BMD Full course','19/01/2021')