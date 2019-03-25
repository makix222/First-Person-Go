# client window to hold the main.py
import wx

app = wx.App()
frame = wx.Frame(parent=None, title='First Person Go')
frame.Show()
app.MainLoop()
