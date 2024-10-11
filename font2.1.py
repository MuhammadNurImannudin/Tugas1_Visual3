import PySimpleGUI as sg
sg.theme ("DarkRed1")
sg.theme_text_color("blue")
window=sg.Window(title="profile",
                 layout=[[sg.Text("FTI UNISKA")],
                         [sg.Text("FAKULTAS TEKNOLOGI INFORMASI")],
                         [sg.Text("UNISKA MAB BANJARMASIN")],],
                 size=(400,200))
window()
window.close()