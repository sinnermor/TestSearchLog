
import re, os
import glob
from pip._vendor import requests

dirrect = ""

# allowedIps = ['129.0.0.1', '127.0.0.1']
# def allow_by_ip(view_func, ip_my):
#     def authorize(request, *args, **kwargs):
#         user_ip = request.META['REMOTE_ADDR']
#         for ip in allowedIps:
#             if ip==user_ip:
#                 return view_func(request, *args, **kwargs)
#         return HttpResponse('Invalid Ip Access!')
#     return authorize

def auth_data(ip):
    pass
    # do somthing
    # return login, password

def get_auth(login, password):
    session = requests.session()
    data = {"username": login, "pass": password}
    url = "test.server.111"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)  Safari/537.36'}
    r = session.post(url, data=data, headers=headers)
#     Написать если авторизация не прошла



def getsubs(dir):

    # get all
    dirs = []
    files = []
    for dirname, dirnames, filenames in os.walk(dir):
        dirs.append(dirname)
        for subdirname in dirnames:
            dirs.append(os.path.join(dirname, subdirname))
        for filename in filenames:
            files.append(os.path.join(dirname, filename))
    print(dirs, files)

def find_files_array(mask):
    filename_mask = mask + '*.log'
    filelist = []
    # dir = os.path.join()
    for filename in glob.glob(os.path.join((os.path.dirname((__file__))) + filename_mask)):
        filelist.append(filename)
    return filelist


def find_text(text, mask):
    files = find_files_array(mask)
    i = 0
    for log_file in files:
        with open(log_file, 'r') as file:
            for line in file:
                if line.find(text) != -1:
                    # Тут должен быть красивый вывод строки
                    print (line)
                    i+=i
        file.close()


def print_scope(identify, mask):
    files = find_files_array(mask)
    for log_file in files:
        with open(log_file, 'r') as file:
         lines = file.readlines()

        r = re.compile(identify)
        for i in range(len(lines)):
            if r.search(lines[i]):
                print(lines[i-10:i+10], end='\n')


def print_info(ip, mask, identify):
    # Get authorized in system
    get_auth(auth_data(ip))
    files = find_files_array(mask)
    for file in files:
        find_text(identify)
        print_scope(identify, 100)

#
#
# print('Type ip-adress ')
# ip_adress = input()
# # Get authorized by login an password
# get_auth(auth_data(ip_adress))
#
# print('Type log-mask ')
# log_mask = input()
# print('Type query for search ')
# identify = input()
#
# print_scope(log_mask, identify)
#
#
# print_scope()
getsubs("C:\Autotesting\WebDriver")