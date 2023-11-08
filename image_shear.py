import sys
from wand.image import Image

#USAGE: 
# python ./Albu_Alexandru_CD_313.py [image location] [shear_x value] [shear_y value] [angle of rotation]
# For the solution to the skull problem simply run the script without parameters


def main():

    #checking if the user provided an image
    if len(sys.argv) >= 2:
        file = str(sys.argv[1])
    else:
        print("Please provide an image")
        return

    #parsing the input, the default values will solve the skull perspective problem
    shear_x = int(sys.argv[2]) if len(sys.argv) >= 3 else -55
    shear_y = int(sys.argv[3]) if len(sys.argv) >= 4 else 0
    angle = int(sys.argv[4]) if len(sys.argv) >= 5 else 45
    output = str(sys.argv[5]) if len(sys.argv) >= 6 else 'transformed_image'

    with Image(filename = file) as image:
        with image.clone() as img:

            #performing shear on the image
            img.shear('Black', shear_x, shear_y)

            #performing rotation on the image
            img.rotate(angle)

            #saving the image, 
            img.save(filename = output + '.jpg')

if __name__ == "__main__":
    main()
