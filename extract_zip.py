
#!/usr/bin/python3.7

import os
from zipfile import ZipFile

# User inputs zip file directory and we navigate there
input_zip_directory = str(input("Name zip file directory: "))
os.system("cd $input_zip_directory")
print(input_zip_directory)

# User inputs zip file name
input_zip_name = str(input("Name zip file: "))
print(input_zip_name)

# Opening zip file in read mode
#with ZipFile($input_zip_name, 'r') as zip:
#    zip.printdir()
    # Extract all the files
#    print('Extracting all the files now...')
#    zip.extractall()
#    print('Done!')

