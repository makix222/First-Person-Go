# client window to hold the main.py
# not needed yet and utterly broken. All resources I can find online to help
# are all in python 2. :(


import wx
import os

app = wx.App()
frame = wx.Frame(parent=None, title='First Person Go')
frame.Show()
app.MainLoop()
