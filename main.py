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
supportername = "Boris"
supporterid = 1
list_yos(supporterid, supportername)

# ADD CHALLENGE CODE HERE




