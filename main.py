import PySimpleGUI as sg
sg.SetOptions(element_padding=(0, 0))
"""
    Restrict the characters allowed in an input element to digits and . or -
    Accomplished by removing last character input if not a valid character
"""

layout = [  [sg.Text('Input value for you would like to convert, please input only numbers')],
            [sg.Input(key='-IN-', enable_events=True, size=(10,1))],

            [sg.Text('Convert From',pad=(30,10)), sg.Text('Convert to')],

            [sg.InputOptionMenu(["Binary","Base 10", "hexadecimal"],pad=(10,5), key='-from-',size=(15,5)), sg.InputOptionMenu(["Binary","Base 10", "hexadecimal"],key='-to-',size=(15,30))],
            
            [sg.Button('Submit'),sg.Button('Exit')]  
            
            ]

window = sg.Window('Bucky', layout)
def bin_check():

   pass

    
def bintobase10():

     user_input = values["-IN-"]

     user_input_string = str(user_input)

     for contents in user_input_string:

        if contents != '0' and contents != '1':

            return sg.popup('Number not binary! Binary numbers are made up of only 1s and 0s ',title='error')
     base = 2

     running_total = 0

     user_input_str = str(user_input)

     num_of_digits = len(user_input_str) - 1

     for i in user_input_str:

        x = int(i)

        y = x * (base ** num_of_digits)

        running_total += y 

        num_of_digits-=1

     user_message = str(running_total) + ' is the equivalent of ' + user_input_string + ' in base 10 decimal'

     return sg.popup(user_message,title='Info') 

def base10tobin():

    pass

def binarytohex():

    pass

def hextobinary():

    pass

def hextobase10():

    pass

def base10tohex():

    pass

def same():
  
  """ this function just returns input value back,if it detects the to and from fields are the same"""

  return sg.popup('No need for conversion!', title='error')
while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    # if last character in input element is invalid, remove it
    if event == '-IN-' and values['-IN-'] and values['-IN-'][-1] not in ('0123456789.-'):
        window['-IN-'].update(values['-IN-'][:-1])

    if event in ('Submit'):

        if not values['-IN-']:

            sg.popup("No value supplied",title='error')

        elif values['-from-'] == values['-to-'] :

            same()

        elif values['-from-'] == 'Binary' and values['-to-'] == 'Base 10':

            bintobase10()

        else:

            print(values)

window.close()

