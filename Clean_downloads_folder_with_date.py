##hg
#check modified date and create the path if not exist

from genericpath import isdir
import os
import datetime as dt
import glob
import shutil
import argparse

parser = argparse.ArgumentParser(description="Just an example",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-e", "--extensions", default=[],nargs='+',help="type in extensions to filter in format py Default filters everything")
parser.add_argument("-l", "--directory", default="current",help="directory to run in")
args = parser.parse_args()
config = vars(args)
#print(config)

print(config["extensions"])

if config["directory"] =="current":
    download = os.getcwd() 
else:
    download = config["directory"]
    print(download)

files_to_move= [] 
os.chdir(download)
#list_of_files  = os.listdir(os.curdir) #glob.glob("*") 

if config["extensions"] =="all":
    split_types = list(set(os.path.splitext(file)[-1] for file in os.listdir(os.curdir)))
else:
    split_types = list(set(config["extensions"]))
    if '.' not in split_types:
        split_types = ['.'+item for item in split_types]


for file in os.listdir(os.curdir):
    if file.endswith(split_types):
        if os.path.isfile(file):
            file_time = dt.datetime.fromtimestamp(os.path.getmtime(file))
            print(file)
            print(file_time.strftime("%Y-%m-%d"))
            filename, file_ext = os.path.splitext(file)
            file_ext_name = file_ext.replace(".","")
            print(filename,file_ext,file_ext_name)
            if not os.path.exists(str(file_time.strftime("%Y-%m-%d"))):
                os.mkdir(str(file_time.strftime("%Y-%m-%d")))
                if not os.path.exists(str(file_time.strftime("%Y-%m-%d"))+'/'+file_ext_name):
                    os.mkdir(str(file_time.strftime("%Y-%m-%d"))+'/'+file_ext_name)
            shutil.move(file, str(file_time.strftime("%Y-%m-%d"))+'/'+file_ext_name)





