import PySimpleGUI as sg
sg.SetOptions(element_padding=(0, 0))


"""
    Restrict the characters allowed in an input element to digits and . or -
    Accomplished by removing last character input if not a valid character
"""

layout = [  [sg.Text('Input value for you would like to convert, please input only numbers')],
            [sg.Input(key='-IN-', enable_events=True, size=(10,1))],

            [sg.Text('Convert From',pad=(30,10)), sg.Text('Convert to')],

            [sg.InputOptionMenu(["Binary","Base 10", "hexadecimal","Octal"],pad=(10,5), key='-from-',size=(15,5)), sg.InputOptionMenu(["Binary","Base 10", "hexadecimal","Octal"],key='-to-',size=(15,30))],
            
            [sg.Button('Submit'),sg.Button('Exit')]  
            
            ]

window = sg.Window('Bucky', layout)


    
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

    """ this function accepts any number and converts to binary integer"""
    user_input = int(values["-IN-"])

    base = 2 

    binary_list = []

    while True:

        if user_input == 0:

            break

        else:

            divide_result = user_input // base

            remainder = user_input % base

            binary_list.append(remainder)

            user_input = divide_result

    reversed_binary_list = binary_list[::-1]

    reversed_binary_list_str = list(map(str,reversed_binary_list))

    return_string = ''.join(reversed_binary_list_str)

    user_message = return_string + ' is the equivalent of ' + values['-IN-'] + ' in base 2.'

    return sg.popup(user_message,title='info')


def binarytohex():

    user_input = values["-IN-"]

    user_input_string = str(user_input)

    for contents in user_input_string:

        if contents != '0' and contents != '1':

            return sg.popup('Number not binary! Binary numbers are made up of only 1s and 0s ',title='error')

    

def hextobinary():

    """accepts hexadecimal digits and converts to binary. It will first check if the number is hexadecimal"""

    pass

def hextobase10():

    """converts hexadecimal digits to base 10. will check for hexadecimal"""
    

    if values["-IN-"] == 'A':

        [sg.Input(key='-IN-', enable_events=False, size=(10,1))],

    else:

        [sg.Input(key='-IN-', enable_events=True, size=(10,1))],

def base10tohex():

    """ converts base 10 digits to hexadecimal values"""

    user_input = int(values['-IN-'])

    base = 16

    running_list = []

    while True:

        if user_input == 0:

            break

        else:

            quotient = user_input // base

            remainder = user_input % base

            running_list.append(remainder)

            user_input = quotient

    reversed_list = running_list[::-1]

# dict is necessary inorder to display output in letter format.
  
    some_dict = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}

    for contents in reversed_list:

        if contents >= 10:

            for contents2 in some_dict.keys():

                converted_contents = int(contents2)

                # converted_contents comes from the dictionary keys 

                if converted_contents == contents:

                    where = reversed_list.index(contents)

                    reversed_list[where] = some_dict[contents]

                    
    a = list(map(str,reversed_list))

    a_string = ''.join(a)

    user_output = a_string + ' is the equivalent of ' + values['-IN-'] + ' in base 16.'

    return sg.popup(user_output,title='info')

def Octaltobase10():

    """ converts base 8 digits to base 10"""

    pass

def base10toOctal():

    """converts base 10 digits to base 8 digits"""

def Octaltobinary():

    """converts base 8 digits to base 2 digits"""

    pass

def binarytoOctal():

    """converts base 2 digits to base 8 digits"""

    pass

def Octaltohex():

    """converts base 8 digits to base 16 digits"""

    pass

def hextoOctal():

    """converts base 16 digits to base 8 digits"""

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

        elif values['-from-'] == 'Base 10' and values['-to-'] == 'Binary':

            base10tobin()

        elif values['-from-'] == 'Binary' and values['-to-'] == 'hexadecimal':

            binarytohex()

        elif values['-from-'] == "Base 10" and values["-to-"] == 'hexadecimal':

            base10tohex()

        elif values['-from-'] == "hexadecimal" and values["-to-"] == 'Base 10':

            hextobase10()

            



        else:

            print(values)

window.close()