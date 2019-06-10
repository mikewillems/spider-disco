import PySimpleGUI as sg
import sys
import cv2 as cv
from PIL import Image
import io
from sys import exit as exit
import time


# sub-layout components
makeButton = lambda text, key=None, w=6, bgColor='dark red', textColor='white': (
    sg.Button(text, key=key, size=(w, None), button_color=(textColor, bgColor)) )

mainButtons = [
    [sg.FileBrowse('LOAD', key='loadProfileButton', size=(6,None))],
    [sg.Save('SAVE', key='saveProfileButton', size=(6,None))],
    [sg.Button('CALIB', key='openCalibrateButton', size=(6,None))],
    [makeButton('SEND', key='downloadTrialButton')],
    [makeButton('START', key='startTestButton')],
]

buttonsDuringRun = [
    [makeButton('END', key='endTestButton'),]
]

profileSettings = {
        "PROFILE": "Profile0001",
        "DURATION (s)": 90,
        "MAX POWER": None,
        "TAR 1 TSET": 23.5,
        "TAR 2 TSET": None,
        "CAL STD LEN": 5,
        "AMB TSET": None,}

settingsDisplay = [[
        sg.Column([[sg.Text(setting, justification='right')] for setting in profileSettings.keys()]),
        sg.Column([[sg.Text(str(profileSettings[setting]), justification='left')] for setting in profileSettings.keys()])
    ]]

makeIndicator = lambda key, color=None : sg.Canvas(size=(10, 10), background_color=color, key=key)

hwStatusIndicators = [
        makeIndicator('armIndicator', 'red'), sg.Text('ARM  '),
        makeIndicator('enremIndicator', 'blue'), sg.Text('ENREM  '),
        makeIndicator('flirIndicator', 'yellow'), sg.Text('FLIR  '),
        ]


settingsDisplayColumn = [
            [   sg.Column(settingsDisplay),
                sg.Column(mainButtons, key='buttonShelf'),
            ],
            hwStatusIndicators
        ]


logoImg = 'disco_spider.png'

# layout
layout = [

    # panels row
    [
        # control panel column
        sg.Column(settingsDisplayColumn),

        # display panel column
        sg.Column([
            [sg.Image(filename=logoImg, size=(20,20), key='visualPreview')],
            [sg.Text('scale: '), sg.Image(filename=logoImg, size=(1,10))],
            [sg.Image(filename=logoImg, size=(20,20), key='flirPreview')],
            [sg.Text('scale: '), sg.Image(filename=logoImg, size=(1,10))],
        ])
    ]

]


# read window


# create the window and show it without the plot
window = sg.Window('Spider Disco 0.2',
                   location=(200,220),
                   icon='fav1.ico')
window.Layout(layout)


# ---===--- Event LOOP Read and display frames, operate the GUI --- #
cap = cv.VideoCapture(0)

while True:
    button, values = window.Read(timeout=250)
    if button is None:
        break

    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # let img be the PIL image
    img = Image.fromarray(gray)  # create PIL image from frame
    img = img.resize((200,150))
    bio = io.BytesIO()  # a binary memory resident stream
    img.save(bio, format= 'PNG')  # save image as png to it
    imgbytes = bio.getvalue()  # this can be used by OpenCV hopefully
    window.FindElement('visualPreview').Update(data=imgbytes)


    # let img be the PIL image
    img2 = Image.fromarray(hsv)  # create PIL image from frame
    img2 = img2.resize((200,150))
    bio2 = io.BytesIO()  # a binary memory resident stream
    img2.save(bio2, format= 'PNG')  # save image as png to it
    imgbytes2 = bio2.getvalue()  # this can be used by OpenCV hopefully
    window.FindElement('flirPreview').Update(data=imgbytes2)

    # process button presses:
    if button != sg.TIMEOUT_KEY:
        #sg.Popup(values['loadProfileButton'])
        sg.Popup(values)
