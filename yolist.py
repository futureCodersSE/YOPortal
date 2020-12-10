import PySimpleGUI as sg
from datahandlers import get_data
from helpers import get_YO_user_info, get_emotion_image



def list_yos(supporterid, supportername):
  # get list of all yos with this supporter id
  layout = [
    [
      sg.Text('YOs for supporter: ', font=('Helvetica', 12, 'bold')),
      sg.Text(supportername,font=('Helvetica', 12, 'bold'))],
    [
      sg.Text('Name',size=(14,1),font=('Helvetica', 10, 'bold')),
      sg.Text('Surname',size=(14,1),font=('Helvetica', 10, 'bold')),
      sg.Text('Start date',size=(14,1),font=('Helvetica', 10, 'bold')),
      sg.Text('Emotion',size=(14,1),font=('Helvetica', 10, 'bold')),
      sg.Text('Messages', size=(14,1),font=('Helvetica',10,'bold'))
    ]
  ]
  yos = get_data("yos")
  users = get_data("user")
  for yo in yos:
    for user in users:
      if user['ID'] == yo['USERID']:
        name, surname, email, logged_in = get_YO_user_info(user['ID'])
        start_date = yo['STARTDATE']
        emotion_status = yo['EMOTION']
        layout.append([
          sg.Text(name, size=(16,1)),
          sg.Text(surname, size=(16,1)),
          sg.Text(start_date, size=(18,1)),
          sg.Button(button_color=("gray","gray"), image_filename=get_emotion_image(emotion_status),image_size=(20,20)),
          sg.Text("", size=(24,1)), 
          sg.Button('Select')])
  layout.append([sg.Button('Close')])
  window = sg.Window('YOs', size=(800,400)).Layout(layout)

  # wait for a button to be clicked and handle it
  while True:
    event,values = window.read()
    if event == 'Close':
      break
  window.close()

