import PySimpleGUI as sg
import time
from datetime import datetime, timedelta


def calculate_queue_seconds(t1, t2):
    update_time_seconds = 15
    queue_delta = t1-t2
    rate_per_second = queue_delta / update_time_seconds
    remaining_seconds = int(t2/rate_per_second)
    return remaining_seconds


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('We will calculate your remaining queue time!')],
            [sg.Text('What is the queue count now? (e.g. 5762)'), sg.InputText()],
            [sg.Text('What is the next queue count? (e.g. 5734'), sg.InputText()],
            [sg.Button('Calculate'), sg.Button('Exit')],
            [sg.Text('Remaining queue time:')],
            [sg.Text('Queue finished ETA:')]]

# Create the Window
window = sg.Window('Lost Ark Queue Time Calculator', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break
    if event == 'Calculate':
        t1 = int(values[0])
        t2 = int(values[1])
        queue_seconds = calculate_queue_seconds(t1, t2)

        formatted_time_remaining = time.strftime('%H:%M:%S', time.gmtime(queue_seconds))
        print(formatted_time_remaining)

        now = datetime.now()
        finish_time = now + timedelta(0, queue_seconds)
        formatted_finish_time = finish_time.strftime('%H:%M:%S')
        print(formatted_finish_time)

window.close()

