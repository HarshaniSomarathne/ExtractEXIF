import exifread
from sys import argv



def openImage(path_name):
    """Open image file for reading (binary mode)"""
    image = open(path_name, 'rb')
    return image


def getData(tags, key):
    """get EXIF info according to the tag key"""
    for tag in tags.keys():
        if key in tag:
            print "Key: %s, value: %s" % (tag, tags[tag])


def main():
    """main function"""
    #get the image path
    script, image_path = argv
    #open image
    image = openImage(image_path)
    #get image tags
    tags = exifread.process_file(image)
    print getData(tags, "GPS")



if __name__ == '__main__':
	main()