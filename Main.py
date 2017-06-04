import re, os
import glob
from pip._vendor import requests
import pprint

import paramiko

# Method found in Internet and does not tested, but seem it should be works
def coonect_ssh(ip):
    auth_data(ip)
    try:
        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect("< сервер>", username=auth_data['login'], password=auth_data['pasword'])
        ftp = ssh.open_sftp()
        currentDir = ftp.getcwd()
        return currentDir
    except : print ('Somthing went wrong')



# Some function to get auth on server, return login and pasword
def auth_data(ip):
    pass
    # do somthing
    # return login, password


# Second auth try
# Abstract function for auth
def get_auth(login, password):
    session = requests.session()
    data = {"username": login, "pass": password}
    url = "test.server.111"
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    r = session.post(url, data=data, headers=headers)
    if r.status != 200:
        print("Auth is not finished")


# Find all subdir anf subfiles from dir
def getsubs(dir, mask):
    files = []
    filename_mask = mask + '*'
    for dirname, dirnames, filenames in os.walk(dir):
        for filename in glob.glob(os.path.join(filenames + filename_mask)):
            files.append(os.path.join(dirname, filename))
    return files

# Find files matched with mask in some dirrectory
def find_files_array(mask, dir):
    filename_mask = mask + '*'
    filelist = []
    # Here we find files array which mached with mask from current dir for win
    # for filename in glob.glob((dir + '/' + filename_mask)): - WIN dir = (os.path.dirname((__file__)))
    for filename in glob.glob((dir + filename_mask)):
        filelist.append(filename)
    return filelist


# Find text in files by identify
def find_text(identify, mask, dir):
    files = find_files_array(mask, dir)
    try:
        if not files:
            print('Files with mask =' + mask + ' not found')
        else:
            file_result = open("file.txt", "w")
            i = 0
            for log_file in files:
                with open(log_file, 'r') as file:
                    for line in file:
                        if line.find(identify) != -1:
                            file_result.write(line)
                            i += i
            file_result.close()
            print_from_file("file.txt")
    except: print("Somthing went wrong!")


# Print lines scope matched string and value strings before and after it
def print_scope(identify, mask, dir, value):
    files = find_files_array(mask, dir)
    if not files:
        print('Files with mask =' + mask + ' not found')
    else:
        line_list = []
        for log_file in files:
            with open(log_file, 'r') as file:
                lines = file.readlines()
            r = re.compile(identify)

            for i in range(len(lines)):
                if r.search(lines[i]):
                    line_list.append(lines[i - value: i + value])

        with open("file_scope.txt", "w") as file_result:
            for line in line_list:
                file_result.write(str(line))
        file_result.close()
        print_from_file("file_scope.txt")


# Function for printing data from file
def print_from_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        if lines:
            pprint.pprint(lines)
        else : print("There is no matched strings in file")




print('Type ip-adress ')
ip_adress = input()
# Get authorized by login an password
# get_auth(auth_data(ip_adress))
dir = coonect_ssh(ip_adress)
print('Type log-mask ')
log_mask = input()
print('Type query for search ')
identify = input()
find_text(identify, log_mask, dir)
print_scope (identify, log_mask, dir, 100)
