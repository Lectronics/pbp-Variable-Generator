import re

types = {
    "bit": 1,
    "byte": 2,
    "word": 4,
    "long": 8,
    "double": 8
}

prefixes = {
    "bit": "%",
    "byte": '$',
    "word": "?",
    "long": "?",
    "double": "?"
}

defines = {
    "type": "byte",
    "name": "MyVar1",
    "value": "0x1876fcd9087b06a8d654ffdc87d6b4587a4",
    "isArray": False,
}


def preParse(hex_string, strip_sequence):

    # Setting up the stripped string variable to be able to loop the process multiple times
    stripped_string = hex_string

    # Added functionality for comments in the value field if you ever wanted to do that... 
    # Just put your comment in between double hashtags

    # m = re.search('##(.*)##', hex_string)
    # # get extracted string
    # ext_string = m.group(1)

    # strip_sequence.insert(0, ext_string)


    for i in strip_sequence:
        # Strip the "0x" off the beginning of the hex number
        split_array = stripped_string.split(i)

        # Turn step_1 back into a string
        stripped_string = ''
        for i in split_array: stripped_string += i 

    return stripped_string


def checkEvenLength(string, defines):
    # making sure the value is an even number of digits and zero padding the first if not
    if len(string) % types[defines["type"]] != 0:
        string = '0' + string

    return string


def splitString(string, defines):

    # Parsing the string into x digit numbers (different types are different lengths) seperated by spaces
    arr_str = "" # Creating my "Bucket" string
    for i, val in enumerate(string): # making a zipped list to associate a index with the value that is passed into the for loop
        arr_str += val
        # Depending on the type of the data to be written, the spaces will seperate the data into the appropriate sizes
        if ((i+1) % types[defines["type"]] == 0) and (i+1 < len(string)):
            arr_str += " " #if i != len(string) else None
        
        # Splitting the string that was just parsed into an array and retuning it
    return arr_str.split(" ")


def generateVarFromValue(frameData):


    defines["type"]    = frameData.type_spinbox.get() #PUT SOMWTHING HERE
    defines["name"]    = frameData.name_entry.get()
    defines["value"]   = frameData.value
    defines["isArray"] = True
    
    var_name = defines['name']
    var_type = defines["type"]
    var_value = defines["value"]
    # defines["isArray"] = True

    variable_values = ""
    value_array = []

    # Make a list of characters that should be taken out of the list (There is probably a better way to do this with a nparray)
    unwanted_characters = ["$", '0x', '%', ' ', ',', '\n', '!', '#']

    if defines["isArray"]:

        var_value = preParse(var_value, unwanted_characters)

        # making sure the value is an even number of digits and zero padding the first if not
        var_value = checkEvenLength(var_value, defines)

        # Parsing the string into x digit numbers (different types are different lengths) seperated by spaces
        value_array = splitString(var_value, defines)

        # Making a define of each array index with its specified value in value_array
        for i, val in zip(range(len(value_array)), value_array):
            variable_values += f"{var_name}[{i}] = {prefixes[var_type]}{val}\n"


    else:
        variable_values = f"{var_name} = ${var_value}\n"


    variable_declaration = f"{var_name} var {var_type}{f'[{len(value_array)}]' if len(value_array) > 1 else ''}\n"

    output = variable_declaration + variable_values

    return output


def binToHexa(n):
  
    # convert binary to int
    num = int(n, 2)
    
    # convert int to hexadecimal
    hex_num = format(num, 'x')
    return(hex_num)


def openFont(font):
    pass


# if __name__ == "__main__":
#     print(generateVariable("0x67 0x3346ed64 0x0917a97c0f7 0x98598 0x3f7f8a")) 

