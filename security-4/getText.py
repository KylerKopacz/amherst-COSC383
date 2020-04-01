import numpy as np
import imageio
import sys

def chunk(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

if __name__ == "__main__":
    # make sure that there is the correct amount of arguments
    if len(sys.argv) != 2:
        print("Error: invalid number of arugments")
        print("Usage: python readText.py <path to image>")
        sys.exit(1)
    
    # first we want to read the image
    img = imageio.imread(sys.argv[1])

    # get the width and the height, and print those out
    height, width, _ = img.shape
    print("Height: ", height, "Width: ", width)

    # now we want to get some information from these files
    # this file is for text, and so the first 32 bits of the message are for that
    # so lets try to get the message size for the test image
    numCharBits = 0
    messageSizeBits = []
    messageBits = []
    messageSize = 0

    # for every row and column in the image (ie every pixel)
    for row in range(height):
        for col in range(width):
            for chan in range(3):
                if numCharBits < 32:
                    # append the least significant bit in each channel of a pixel
                    # to the messageSizeBits list, so we can read the whole 
                    # thing later
                    messageSizeBits.append(str(img[row,col,chan] & 1))
                    numCharBits += 1

                    if numCharBits == 32:
                        messageSize = int("".join(messageSizeBits), 2)
                else:
                    if len(messageBits) != messageSize * 8:
                        # now just get all the rest of the bits and throw them in a list
                        messageBits.append(str(img[row,col,chan] & 1))


    # print("There are ", len(messageSizeBits), " bits in the sizeBits list.")
    # print("".join(messageSizeBits))
    print("Number of characters: ", messageSize)
    
    # now that we have the message, we can just take 8 bits at a time from the list and interpret
    # those bits as a character, and only do that as long as the message is.
    message = list(chunk(messageBits, 8))
    realMessage = []
    for i in message:
        realMessage.append(chr(int("".join(i), 2)))

    print("Length of the message: ", len(realMessage))
    print("".join(realMessage))
    
