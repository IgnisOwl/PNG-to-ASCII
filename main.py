from PIL import Image

#ascii constants
DARK_CHAR = "█"
LIGHT_CHAR = "░"
NEW_LINE = "\n"

#read the image
image = Image.open("image.png")
imageX, imageY = image.size


#file dest
output = "output.txt"

#used for reversing the whites/blacks
reversePolarity = False

downscaleFactor = 1
threshold = 0

#ask user questions for the conversion
def question():
    while True:
        threshold = input("Brightness Threshold(0-765): ")
        try:
            if(int(threshold)<=765 and int(threshold) > 0):
                break;
            else:
                print("Threshold must be 0-765")
        except:
                print("Threshold must be a valid Int")

    while True:
        downscaleFactor = input("Downscale factor(1-20): ")
        try:
            if(int(downscaleFactor)<=20 and int(threshold) >= 1):
                break;
            else:
                print("Downscale factor must be a valid int")
        except:
                print("Downscale factor must be between 1 - 20")

    reverse = input("Reverse Whites/Blacks? y/N ")

    global imageX, imageY, image, reversePolarity
    if(reverse.lower() == "y"):
        reversePolarity = True
    else:
        reversePolarity = False

    imageX = round(imageX/int(downscaleFactor))
    imageY = round(imageY/int(downscaleFactor))
    image = image.resize((imageX, imageY))


def convert():
    outChars = ""
    for y in range(imageY):
        for x in range(imageX):
            rgb = image.getpixel((x, y))
            brightness = rgb[0] + rgb[1] + rgb[2] #brightness of a pixel is just total r + g + b
            if(brightness > threshold):
                if(not reversePolarity):
                    outChars = outChars + LIGHT_CHAR + LIGHT_CHAR #its twice because for sum reason the characters are narrow and it has problems 
                else:
                    outChars = outChars + DARK_CHAR + DARK_CHAR
            else:
                if(not reversePolarity):
                    outChars = outChars + DARK_CHAR + DARK_CHAR
                else:
                    outChars = outChars + LIGHT_CHAR + LIGHT_CHAR


        outChars = outChars + "\n"

    return(outChars)



if __name__ == "__main__":
    question()
    converted = convert()
    outputFile = open(output, "w")
    outputFile.write(converted)
