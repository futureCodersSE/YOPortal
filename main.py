import PySimpleGUI as sg
# Portal app to work with goals database
from datahandlers import get_data
from login import login_supporter
from yolist import list_yos

# main program
# print(get_data("yos"))
#print(get_data("message"))
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

def create_messages_window(yoid):

  layout= [
   [sg.Text('Messages from', size= (15,1)), sg.Text('YOID', size=(70,1)), sg.Button('Log Out')]]
   
  message_list = get_data("message")

  for message in message_list:
     if message['YOID']== str(yoid):
       layout.append([sg.Text('_'*140)])

       layout.append([sg.Text(' ', size=(70,1))+ sg.Text('Urgent', size=(70,1))])
       layout.append([sg.Text(' ', size=(70,1))])
       layout.append([sg.Text('Opened', size=(70,1))])
       layout.append([sg.Text('Date', font=('bold')), sg.Text(message['MESSAGEDATE'])])
       layout.append([sg.Text('Subject', font=('bold')), sg.Text(message['SUBJECT'])])
       layout.append([sg.Text('Text'), sg.Text(message['MESSAGETEXT'])])
   
  layout.append([sg.Text('_'*140)])
  layout.append([sg.Button('Close')])



  
  window = sg.Window('Messages', size=(800,400)).Layout(layout)


  while True:
    event, values = window.read()
    if event == 'Close':
      break
  window.close()


#main_program
print (create_messages_window(2))








