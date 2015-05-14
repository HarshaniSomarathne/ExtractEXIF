from os import walk
import exifread
import optparse
import sys
import csv


def getFilename(directory):
    """Get all the file names in the directory. Return a filename list."""
    f = []
    for (dirpath, dirnames, filenames) in walk(directory):
       f.extend(filenames)
       break
    return f


def openImage(path_name):
    """Open image file for reading (binary mode)"""
    image = open(path_name, 'rb')
    return image


def getData(filename, tags, key):
    """Get EXIF info according to the tag key. Return a dataSet: (key, value)"""
    dataSet = [["filename",filename]]
    for tag in tags.keys():
        if key in tag:
            dataSet.append([tag, tags[tag]])
    return dataSet


def outputCSV(dataSet, filename):
    """output dataSet to filename"""
    with open(filename, 'w') as csvfile:
        csvW = csv.writer(csvfile)
        for data in dataSet:
            csvW.writerows(data)
    csvfile.close()


def main():
    """get EXIF info from images according to the key value"""
    optparser = optparse.OptionParser()
    optparser.add_option("-d", "--directory", dest="directory", default="", help="the directory of input images")
    optparser.add_option("-k", "--key", dest="key", default="GPS", help="the EXIF key")
    (opts, _) = optparser.parse_args()
    
    #get file names
    filenames = getFilename(opts.directory)
    
    dataSet = []
    for filename in filenames:
        #open image file
        image = openImage(opts.directory + "/" + filename)
        tags = exifread.process_file(image)
        #get EXIF info according to the key
        data = getData(filename, tags, opts.key)
        #len(data) <= 1 means it has no EXIF info
        if len(data) > 1:
            dataSet.append(data)
    #output dataSet to csv file
    outputCSV(dataSet, "EXIF.csv")


if __name__ == '__main__':
	main()