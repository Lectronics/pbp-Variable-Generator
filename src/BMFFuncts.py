import struct

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



def fontToHex(font):

    letters = []

    for letter in font[1:]:
        string = ''
        for row in letter:
            for bit in row:
                string += str(bit)

        pack_string = f'>{len(letter)}s'

        letters.append(struct.pack(pack_string, struct.pack('>q', int(string, 2))))

    # for i, letter in enumerate(letters):
    #     letters[i] = struct.pack('>h', letter)

    return letters


if __name__ == "__main__":

    testFont = [[11, 11, 8, 5], [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0], [1, 0, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0]], [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0]], [[0, 1, 0, 1, 0], [0, 1, 1, 1, 0], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0]], [[0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1], [0, 1, 0, 0, 0], [1, 0, 1, 0, 0], [0, 1, 0, 1, 0]], [[0, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]], [[0, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [0, 1, 1, 1, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [1, 0, 0, 0, 1], [0, 1, 1, 1, 0]], [[0, 0, 0, 0, 0], [0, 1, 1, 1, 1], [1, 0, 0, 0, 1], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 1, 1, 1]], [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 1, 1, 1, 0]], [[0, 1, 1, 1, 1], [1, 0, 1, 0, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1]], [[0, 1, 1, 1, 1], [0, 1, 0, 0, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [0, 1, 1, 1, 0]], [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]]

    print(fontToHex(testFont))