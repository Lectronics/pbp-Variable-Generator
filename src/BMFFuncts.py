import struct
import numpy as np

def scaleFont(font, num_of_sizes=1, scale_factor=2):

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

    return new_font



def fontToHex(font, write_direction='v'):

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


    letters = []

    metadata = font[0]

    font = np.array(font[1:])

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
            letters.append([])
            pack_string = f'>{len(letter)}s'
            for i in range(metadata[3]):
                string = ''
                for bit in letter[:, i]:
                    string += str(bit)

                # letters[index].append(struct.pack('>B', int(string, 2)))
                letters[index].append(struct.pack('>B', int(string, 2)))


        for i, letter in enumerate(letters):
            letters[i] = b''  
            for byte in letter:
                letters[i] += byte

    return letters


if __name__ == "__main__":

    testFont = [[4, 4, 8, 5, 'Font'], [[0, 1, 0, 0, 0], [1, 0, 1, 0, 0], [1, 1, 1, 0, 0], [1, 0, 1, 0, 1], [1, 0, 0, 0, 0], [1, 1, 1, 0, 1], [1, 0, 1, 0, 1], [1, 1, 1, 0, 1]], [[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]], [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]], [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 1, 1, 1, 1], [0, 1, 0, 0, 1], [0, 1, 0, 0, 1], [0, 1, 1, 1, 1]]]
    lowLevelFont = [b'*]]]*', b'\x04u^u\x04', b'~\x81\x81\x81B', b'\x00\x0f\t\x89\xff']
    print(lowLevelFont)

    more_font_variables = []
    
    
    for i in lowLevelFont:
        tuple1 = struct.unpack('>sssss', i)
        print(tuple1)

        stringFont = ''

        for j in tuple1:
            stringFont += str(format(struct.unpack('>B', j)[0], 'X')) if len(str(format(struct.unpack('>B', j)[0], 'X'))) > 1 else "0" + str(format(struct.unpack('>B', j)[0], 'X'))

        more_font_variables.append(stringFont)

    print(more_font_variables)