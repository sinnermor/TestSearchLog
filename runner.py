from ServerPart import ServerOperations
from LodParser import LogParse

print('Type ip-adress ')
ip_adress = input()
# Get authorized by login an password
# get_auth(auth_data(ip_adress))
login = ServerOperations(ip_adress)
print('Type log-mask ')
log_mask = input()
print('Type query for search ')
identify = input()
parser = LogParse()
parser.find_text(identify, log_mask)
parser.print_scope(identify, log_mask, 100)
