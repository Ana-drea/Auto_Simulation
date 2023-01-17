import time

from pywinauto.application import Application

app  = Application(backend="uia").start(r"C:\Program Files (x86)\SDL\SDL Passolo\SDL Passolo 2018\psl.exe")

# app = Application("uia").connect(process=9492)
# app.kill()
time.sleep(10)
dlg = app["[PASSOLO 2018] Team Edition 18.0.133.0 - [Start Page]"]


# dlg = app["[PASSOLO 2018] Team Edition 18.0.133.0 - [Start Page]"]
# dlg.restore()
menu = dlg.window(auto_id="59398", control_type="ToolBar")
home_tool_bar = menu.child_window(title="Home", control_type="ToolBar")
prj = home_tool_bar.child_window(title="Project", control_type="ToolBar")
print(prj.print_control_identifiers())
# print(dlg.get_show_state())
# dlg.maximize()
# time.sleep(10)
# print(dlg.get_show_state())

# rect = dlg.rectangle()
# print(rect)