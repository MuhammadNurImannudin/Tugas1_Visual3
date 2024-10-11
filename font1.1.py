import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",
                    layout=[[sg.Text("NPM   : 2110010461 ")],
                            [sg.Text("Nama  : MUHAMMAD NUR IMANNUDIN ")],
                            [sg.Text("Kelas : 5N Regular Banjarmasin ")]],
                    size=(400,200),
                    font=("Times", 18))
window()
window.close()