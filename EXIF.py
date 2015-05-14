import exifread
import optparse
import sys



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
    """get EXIF info from images according to the key value"""
    optparser = optparse.OptionParser()
    optparser.add_option("-f", "--filename", dest="filename", default="", help="the location of input image")
    optparser.add_option("-k", "--key", dest="key", default="GPS", help="the EXIF key")
    (opts, _) = optparser.parse_args()
    
    #open image
    image = openImage(opts.filename)
    #get image tags
    tags = exifread.process_file(image)
    #print EXIF info according to the key
    getData(tags, opts.key)



if __name__ == '__main__':
	main()