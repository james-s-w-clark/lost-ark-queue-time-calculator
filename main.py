import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('We will calculate your remaining queue time!')],
            [sg.Text('What is the queue count now? (e.g. 5762)'), sg.InputText()],
            [sg.Text('What is the next queue count? (e.g. 5734'), sg.InputText()],
            [sg.Button('Calculate'), sg.Button('Cancel')],
            [sg.Text('Remaining queue time:')],
            [sg.Text('Queue finished ETA:')]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()