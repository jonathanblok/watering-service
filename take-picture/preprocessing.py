from PIL import Image 

class preprocessing:

    def process(path):
        image_file = Image.open(path) # open colour image
        image_file = image_file.convert('1') # convert image to black and white
        image_file.save('/home/pi/Workspace/watering-service/take-picture/result.png')
