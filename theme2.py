import PySimpleGUI as sg
sg.theme("DarkRed1")
window=sg.Window(title="profile",
                 layout=[[sg.Text("NPM          : 2110010461")],
                         [sg.Text("Nama         : MUHAMMAD NUR IMANNUDIN")],
                         [sg.Text("Kelas        : 5N Reguler Banjarmasin")],
                         [sg.Text("Matkull      : pempograman Visual 3")]],
                 size=(400,200))
window()
window.close()