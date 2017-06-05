import re, os
import glob
import pprint
from ServerPart import ServerOperations


class LogParse(object):

    def __init__(self):
        self.dir = ServerOperations.dir

    # Find all subdir anf subfiles from dir
    def getsubs(self, mask):
        files = []
        filename_mask = mask + '*'
        for dirname, dirnames, filenames in os.walk(self.dir):
            for filename in glob.glob(os.path.join(filenames + filename_mask)):
                files.append(os.path.join(dirname, filename))
        return files


    # Find files matched with mask in some dirrectory
    def find_files_array(self, mask):
        filename_mask = mask + '*'
        filelist = []
        # Here we find files array which mached with mask from current dir for win
        # for filename in glob.glob((dir + '/' + filename_mask)): - WIN dir = (os.path.dirname((__file__)))
        for filename in glob.glob((self.dir + filename_mask)):
            filelist.append(filename)
        return filelist


    # Find text in files by identify
    def find_text(self, identify, mask):
        files = self.find_files_array(mask)
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
                self.print_from_file("file.txt")
        except:
            print("Somthing went wrong!")


    # Print lines scope matched string and value strings before and after it
    def print_scope(self, identify, mask, value):
        files = self.find_files_array(mask)
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
            self.print_from_file("file_scope.txt")


    # Function for printing data from file
    def print_from_file(self, file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            if lines:
                pprint.pprint(lines)
            else:
                print("There is no matched strings in file")


