import paramiko
from pip._vendor import requests


class ServerOperations(object):

    def __init__(self, ip):
        self.dir = self.coonect_ssh(ip)

    # Method found in Internet and does not tested, but seem it should be works
    def coonect_ssh(self, ip):
        self.auth_data(ip)
        try:
            ssh=paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect("< сервер>", username=auth_data['login'], password=auth_data['pasword'])
            ftp = ssh.open_sftp()
            currentDir = ftp.getcwd()
            return currentDir
        except: print('Somthing went wrong')

    # Some function to get auth on server, return login and pasword
    def auth_data(self, ip):
        pass
        # do somthing
        # return login, password

    # Second auth try
    # Abstract function for auth
    def get_auth(self, login, password):
        session = requests.session()
        data = {"username": login, "pass": password}
        url = "test.server.111"
        headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        r = session.post(url, data=data, headers=headers)
        if r.status != 200:
            print("Auth is not finished")
