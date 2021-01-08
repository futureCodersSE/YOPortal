import PySimpleGUI as sg
from datahandlers import get_data
from helpers import get_YO_details, get_emotion_image
from yoprofile import show_yo_profile


def list_yos(supporterid, supportername):
  # display title and headings
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
  # get and display list of all yos with this supporter id
  yos = get_data("yos")
  users = get_data("user")
  for yo in yos:
    for user in users:
      if user['ID'] == yo['USERID']:
        yo_details = get_YO_details(yo["ID"])
        message_colour = "red" if yo_details["SOMEURGENT"] else "black"
        layout.append([
          sg.Text(yo_details["NAME"], size=(16,2)),
          sg.Text(yo_details["SURNAME"], size=(16,2)),
          sg.Text(yo_details["STARTDATE"], size=(18,2)),
          sg.Button(button_color=("gray","gray"), image_filename=get_emotion_image(yo_details["EMOTION"]),image_size=(50,50), size=(20,2)),
          sg.Text(yo_details["MESSAGECOUNT"], justification="center", text_color=message_colour, font=('Helvetica', 12, 'bold'), size=(18,2)), 
          sg.Button('Select', key='yo-' + yo["ID"])])
        break
  layout.append([sg.Button('Close', size=(20,2))])
  window = sg.Window('YOs', size=(800,350)).Layout(layout)

  # wait for a button to be clicked and handle it
  while True:
    event,values = window.read()

    if event.find('yo-') != -1:
      yoid = event.split('-')[1]
      show_yo_profile(yoid)
    if event == 'Close':
      break
  window.close()

