#!/usr/bin/python2.7
# Usage - amend size variable for desired dimensions
# Run: python2.7 resize_picture_script.py <picture_name.jpeg>

import os, sys
try:
    from PIL import Image
except ImportError:
    import Image

size = 128, 128

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(outfile, "JPEG")
        except IOError:
            print("cannot create thumbnail for '%s'" % infile)
