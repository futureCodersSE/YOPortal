import PySimpleGUI as sg
from datahandlers import get_data

def get_emotion_image(emotion):
  image_file = ""
  # return the correct image for the emotion
  return image_file

def list_yos(supporterid, supportername):
  # get list of all yos with this supporter id
  layout = [
    [
      sg.Text('YOs for supporter: ', font=('Helvetica', 12, 'bold')),
      sg.Text(supportername,font=('Helvetica', 12, 'bold'))],
    [
      sg.Text('Name',size=(10,2),font=('Helvetica', 10, 'bold')),
      sg.Text('Surname',size=(10,2),font=('Helvetica', 10, 'bold')),
      sg.Text('Start date',size=(10,2),font=('Helvetica', 10, 'bold')),
      sg.Text('Emotion status',size=(10,2),font=('Helvetica', 10, 'bold'))
    ]
  ]
  yos = get_data("yos")
  users = get_data("user")
  for yo in yos:
    for user in users:
      if user['ID'] == yo['USERID']:
        name = user['NAME']
        surname = user['SURNAME']
        start_date = yo['STARTDATE']
        emotion_status = yo['EMOTION']
        layout.append([
          sg.Text(name, size=(10,2)),
          sg.Text(surname, size=(10,2)),
          sg.Text(start_date, size=(10,2)),
          sg.Button(button_color=("red","red"), image_filename=get_emotion_image(emotion_status),image_size=(20,20)), 
          sg.Button('Select')])
  layout.append([sg.Button('Close')])
  window = sg.Window('YOs').Layout(layout)

  # wait for a button to be clicked and handle it
  while True:
    event,values = window.read()
    if event == 'Close':
      break
  window.close()

