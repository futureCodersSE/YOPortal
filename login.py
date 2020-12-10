import PySimpleGUI as sg
from datahandlers import get_data

def login_supporter():
  # retrieve details for user by email, check password and return supporterid
  supporterid = 0
  supportername = ''
  # display login window
  layout = [
    [sg.Text('Enter your log in details')],
    [sg.Text("Email")],
    [sg.Input(key="-ID-")],
    [sg.Text('Password')],
    [sg.Input(password_char="*", key="-PW-")],
    [sg.Button("Login")]
  ]
  window = sg.Window('Login').Layout(layout)

  # wait for click on login button, check credentials and select supporter
  while True:
    event, values = window.read()
    if event == 'Login':   
      # email = values['-ID-']
      # password = values['-PW-']
      # users = get_data("user")
      # validcredentials = False
      # for user in users:
      #   if user['EMAIL'].split('@')[0] == email.split('2')[0] and user['PASSWORD'] == password:
      #     validcredentials = True
      #     supporters = get_data("supporter")
      #     for supporter in supporters:
      #       if supporter['USERID'] == user["ID"]:
      #         supporterid = supporter['ID']
      #         supportername = user['NAME']
      # if validcredentials:
        break
  window.close()
  return supporterid, supportername