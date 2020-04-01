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
    height, width, channels = img.shape
    print("Height: ", height, "Width: ", width, "Number of Channels: ", channels)

    # now we want to get some information from these files
    # this file is for text, and so the first 32 bits of the message are for that
    # so lets try to get the message size for the test image
    numSizeBits = 0
    messageSizeBits = []
    messageBits = []
    messageSize = 0
    messageHeight = 0
    messageWidth = 0

    # for every row and column in the image (ie every pixel)
    for row in range(height):
        for col in range(width):
            for chan in range(3):
                if numSizeBits < 64:
                    # append the least significant bit in each channel of a pixel
                    # to the messageSizeBits list, so we can read the whole 
                    # thing later
                    messageSizeBits.append(str(img[row,col,chan] & 1))
                    numSizeBits += 1

                    # once we have all the data from the header that we need
                    if numSizeBits == 64:
                        # we can calculate the dimensions of the resulting image
                        messageDimensions = list(chunk(messageSizeBits, 32))
                        messageHeight = int("".join(messageDimensions[0]), 2)
                        messageWidth = int("".join(messageDimensions[1]), 2)
                        print("Message Height: ", messageHeight, " Message Width: ", messageWidth)
                        
                        # now that we know the dimensions, and we know that each channel of a pixel is a byte, 
                        # we know how many bytes we need to get from the rest of the image. So update
                        # that value now so we can save some time
                        messageSize = messageHeight * messageWidth
                else:
                    # we have gone through the header, and we know are writing straight to a message buffer
                    if len(messageBits) != messageSize * 8 * 3:
                        # now just get all the rest of the bits and throw them in a list
                        messageBits.append(str(img[row,col,chan] & 1))


    print("Number of pixels: ", messageSize)
    
    # now that we have the message bits, we need to chunk those bits into bytes. 
    # each one of those bytes is the value of a channel of a pixel.
    # we can now overwrite the values that we had in those slots
    message = list(chunk(messageBits, 8))
    print("There are ", len(message), " values in message")
    
    for row in range(messageHeight):
        for col in range(messageWidth):
            for chan in range(3):
                img[row, col, chan] = int("".join(message.pop(0)), 2)

    imageio.imwrite("altered.png", img)
    print("Wrote to file!")
    
