"""
Docstrinng:
This script will rename files with numbers in them so that they do not have numbers in the filename
"""

import os
import re

def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir(r"C:\Users\gopir\Documents\Gopi\Education\Github\Udacity\Programming_Foundations_with_Python\Prank_Project\alphabet")
    print(file_list)


    # (2) for each file, rename filename
    saved_path = os.getcwd()
    print("Current directory is:", saved_path)
    os.chdir(r"C:\Users\gopir\Documents\Gopi\Education\Github\Udacity\Programming_Foundations_with_Python\Prank_Project\alphabet")
    destination = os.getcwd()
    print("stripping filenames of numbers in directory:",destination)
    for file_name in file_list:
        print("Old file name", file_name)
        new_name = re.sub(r"[0-9]*", "", file_name)
        os.rename(file_name, new_name)
        print("changed to",new_name)
    print("New filenames: ",os.listdir(destination))
    os.chdir(saved_path)
    print("Restored current working directory back to", os.getcwd())

rename_files()
