__author__ = "Raghunath Kulnarni(raghukul), Abhishek Pakrashi(apakrash)"
__email__ = "raghukul@cisco.com, apakrash@cisco.com"
__status__ = "alpha"

import os
from random import randint
import random
from ping3 import ping, verbose_ping

def returnFileContentInList(filename):
    my_file = open(filename, "r")
    content = my_file.read().split('\n')
    return content

#this is a linux specific command
def checkIpConnect(ipaddress): 
    print('\n')
    status = subprocess.call(['ping', '-q', '-c', '3', ipaddress])
    if status == 0:
        print('\n\n\t{} is UP\t'.format(ipaddress))
        return

path = os.path.dirname(os.path.abspath(__file__))
if __name__ == '__main__':
    urlFilePath = os.path.join(path,'urls.txt')
    ipAddressFilePath = os.path.join(path,'ipAddress.txt')
    urlFileList = returnFileContentInList(urlFilePath)
    ipAddressList = returnFileContentInList(ipAddressFilePath)

    for url in range(0,5):
        url = urlFileList[randint(0, 100)]
        print('Sending Get Request for URL=', url)
        try:
            r = requests.get(url)
        except:
            print('Get request timed out for URL=', url)
        #print(r.json())
        print('-----------------------------------------')
    
    
    for ip in range(0,5):
        ip = ipAddressList[randint(0, 100)]
        print('Sending icmp request for ip=', ip)
        pingResponse = ping(ip)
        if pingResponse == False:
            print('Got no answer for ip= ', ip)
        else:
            print('response time of icmp access for ip= ', pingResponse)
        print('-----------------------------------------')