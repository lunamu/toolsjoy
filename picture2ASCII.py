import os,sys
from PIL import Image

WIDTH = 100

def get_ajust_size(image):
	origin_width = image.size[0]
	origin_height = image.size[1]
	target_width = WIDTH	
	target_height = origin_height * (target_width / float(origin_width))	
	target_size = (target_width, int(target_height))
	return target_size


def picture2ascii(fname):
	chars = "   ...',;:clodxkO0KXNWMMMM"
	image = Image.open(fname)
	output = ''
	size = get_ajust_size(image)
	print size
	image = image.resize(size)
	image = image.convert('L')
	pix = image.load()
	for i in range(0, size[1]):
		for j in range(0, size[0]):
			output += chars[pix[j,i]/10]			
		output += '\n'
	print output


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Useage: pic2ascii.py filename"
        sys.exit(1)
    filename = sys.argv[1]
    picture2ascii(filename)