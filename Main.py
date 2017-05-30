
import re, os
import glob

dirrect = ""
def auth_data(ip):
    # return login, password
    pass

def get_auth(login, password):
    pass

def find_files_array(mask):
    filename_mask = mask + '*.log'
    filelist = []
    for filename in glob.glob(os.path.join(dirrect + filename_mask)):
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

print_scope()