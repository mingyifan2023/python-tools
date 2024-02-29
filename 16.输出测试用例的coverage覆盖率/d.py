#! -- utf-8 --

import datetime

import os



def if_fileExist_rm_it(filename):

for file in os.listdir("."):

if os.path.exists(filename) and file ==filename :

os.remove(filename)




if __name__ =="__main__":

s = datetime.datetime.now()

if_fileExist_rm_it(".coverage")

file_list = []

for (dirname, subdir, subfile) in os.walk(os.getcwd()):

ret_file = [os.path.join(dirname, x) for x in subfile]

for item in ret_file:

file_list.append(item)


os.system("coverage erase")

for item in file_list:

exec_file = item.split("\\")[-1]

if "test_" in exec_file and ".py" in exec_file and ".pyc" not in exec_file:

print(item)

os.system("coverage run -p {0}".format(item))


os.system("coverage combine")


os.system("coverage html -d report/coverage-report.html")

os.system("coverage xml -o report/coverage-report.xml")

e = datetime.datetime.now()

print(e-s)

