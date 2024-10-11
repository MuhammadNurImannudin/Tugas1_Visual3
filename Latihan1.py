import PySimpleGUI as sg
sg.theme("DarkRed1")
sg.theme_text_color("blue")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("NPM : 2110010461 ")],
                           [sg.Text("Nama : Muhammad Nur Imannudin ")],
                           [sg.Text("Kelas : 5N Regular Banjarmasin ")],
                           [sg.Text("Matkul : Pemrograman Visual")]
                           ],
                   size=(400,200),
                   font=("Times", 18))
window()
window.close()
