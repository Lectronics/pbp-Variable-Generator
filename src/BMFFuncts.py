import struct
import numpy as np

def scaleFont(font, num_of_sizes=1, scale_factor=2) -> list:

    # Defining iteration variables for the while loops that run through the letters, rows of each letter, and bits of each row
    bit = 0
    row = 0
    letter = 1

    new_font = []


    for i, letter in enumerate(font[1:]):

        new_font.append([])

        for y, row in enumerate(letter):

            new_font[i].append([])

            for x, bit in enumerate(row):

                for j in range(scale_factor):
                    new_font[i][y].append(bit)


    extra_new_font = []


    for y, letter in enumerate(new_font):

        extra_new_font.append([])

        for row in letter:

            for j in range(scale_factor):
                extra_new_font[y].append(row)


    return extra_new_font


def fontToHex(font, write_direction='v', size='byte') -> list:

    # font is a list type formatted like this:
    #
    #           ---------------------------------------------------------------------------------------------------------------------------------------
    #           |   Metadata: [Current Character index,             |    Letter 1:  [row 1: {bit 1, bit 2...bit N},   |    Letter 2    |   Letter n   |
    #           |              Total number of Characters,          |                row 2,                           |                |              |
    #           |              Number of Rows,                      |                row 3...row N]                   |                |              |
    #           |              Number of Columns]                   |                                                 |                |              |
    #           ---------------------------------------------------------------------------------------------------------------------------------------
    #
    # write_direction is 'h' for horizontal, 'v' for vertical:
    #
    #           horizontal mode writes each of the rows all the way across as bits and then goes to the next row
    #
    #           vertical mode writes each column all the way down and then advances to the next column
    #
    #
    # size is 'byte" for 8 bits of data stored at a time. This really doesn't matter because it should be universal in the generator. The option to change it is nice though
    #
    #
    # RETURNS a list of byte-strings formatted like this:
    #
    #       ----------------------------------------------------------------------------------------
    #       |  letter 1: [ byte_string_1,  letter 2: [ byte_string_1,  letter 3: [ byte_string_1,  |
    #       |              byte_string_2,              byte_string_2,              byte_string_2,  |
    #       |              byte_string_3],             byte_string_3],             byte_string_3]  |
    #       ----------------------------------------------------------------------------------------


    # Defining a Dictionary that associates the size parameter with a number that is used in the 
    size_lookup = {
        'byte': 8,
        'word': 16,
        'long': 32,
        'double': 64,
    }

    letters = [] # This is the array that will be returned

    metadata = [4, 4, 8, 5, 'Font'] # font[0] # Storing the metadata before "forgetting it" when re-assigning the font as an nparray

    font = np.array(font[1:]) # Reassigning the font as a nparray without the metadata. This makes it easier to iterate over.

    if write_direction == 'h': 

        for letter in font[1:]:
            pack_string = f'>{len(letter)}s'
            string = ''
            for i in range(metadata[2]):
                for bit in letter[i]:
                    string += str(bit)

                letters.append(struct.pack(pack_string, struct.pack('>q', int(string, 2))))

    # for i, letter in enumerate(letters):
    #     letters[i] = struct.pack('>h', letter)

    if write_direction == 'v':

        for index, letter in enumerate(font):
            letters.append([]) # Adding a letter in the letters array corresponding with a letter in the font array
            pack_string = f'>{len(letter)}s'
            # letters[index].append(pack_string) # Assigning a variable to use in the struct.pack function. <PASSED AS METADATA> because the 's' requires a byte

            for i in range(metadata[3]): # Iterating over the number of columns in the letter so that each 
                string = ''
                for bit in letter[:, i]: # using numpy indexing magic to iterate over a COLUMN of data from a 2-Dimensional Array
                    string += str(bit)   # Adding a bit from what ever column is being iterated over

                # letters[index].append(struct.pack('>B', int(string, 2)))
                letters[index].append(struct.pack('>B', int(string, 2)))


        for i, letter in enumerate(letters[1:]):
            letters[i] = b''  
            for byte in letter:
                letters[i] += byte

    return letters


if __name__ == "__main__":

    testFont = [[4, 4, 8, 5, 'Font'], [[0, 1, 0, 0, 0], [1, 0, 1, 0, 0], [1, 1, 1, 0, 0], [1, 0, 1, 0, 1], [1, 0, 0, 0, 0], [1, 1, 1, 0, 1], [1, 0, 1, 0, 1], [1, 1, 1, 0, 1]], [[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]], [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]], [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 1, 1, 1, 1], [0, 1, 0, 0, 1], [0, 1, 0, 0, 1], [0, 1, 1, 1, 1]]]
    lowLevelFont = fontToHex(testFont) #[b'*]]]*', b'\x04u^u\x04', b'~\x81\x81\x81B', b'\x00\x0f\t\x89\xff']
    print(lowLevelFont)

    # more_font_variables = []
    
    
    # for i in lowLevelFont:
    #     tuple1 = struct.unpack('>sssss', i)
    #     print(tuple1)

    #     stringFont = ''

    #     for j in tuple1:
    #         stringFont += str(format(struct.unpack('>B', j)[0], 'X')) if len(str(format(struct.unpack('>B', j)[0], 'X'))) > 1 else "0" + str(format(struct.unpack('>B', j)[0], 'X'))

    #     more_font_variables.append(stringFont)

    # print(more_font_variables)

    print(fontToHex(scaleFont(testFont)))