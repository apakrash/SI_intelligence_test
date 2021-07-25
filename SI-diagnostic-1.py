__author__ = "Raghunath Kulnarni(raghukul), Abhishek Pakrashi(apakrash)"
__email__ = "raghukul@cisco.com, apakrash@cisco.com"
__status__ = "alpha"

import os, logging, random, requests
from random import randint
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
    try:
        #Create and configure logger
        logging.basicConfig(filename=os.path.join(path,'SI-diagnostic-1.log'),
                            format='%(asctime)s %(message)s',
                            filemode='a')
        #Creating an object
        logger=logging.getLogger()
        
        #Setting the threshold of logger to DEBUG
        logger.setLevel(logging.INFO)

        logger.info("--------------------Initiate testing---------------------")
        urlFilePath = os.path.join(path,'urls.txt')
        ipAddressFilePath = os.path.join(path,'ipAddress.txt')
        urlFileList = returnFileContentInList(urlFilePath)
        ipAddressList = returnFileContentInList(ipAddressFilePath)
        logger.info("Loaded url and ip address file")

        for url in range(0,5):
            url = urlFileList[randint(0, 100)]
            print('Sending Get Request for URL=', url)
            logger.info('Sending Get Request for URL= %s', str(url))
            try:
                r = requests.get(url)
            except:
                print('Get request timed out for URL=', url)
                logger.info('Get request timed out for URL= %s', str(url))
            #print(r.json())
            print('-----------------------------------------')
            logger.info('-----------------------------------------')
        
        
        for ip in range(0,5):
            ip = ipAddressList[randint(0, 100)]
            print('Sending icmp request for ip=', ip)
            logger.info('Sending icmp request for ip= %s', str(ip))
            pingResponse = ping(ip)
            if pingResponse == False:
                print('Got no answer for ip= ', ip)
                logger.info('Got no answer for ip= %s', str(ip))
            else:
                print('response time of icmp access for ip= ', pingResponse)
                logger.info('response time of icmp access for ip= %s', str(pingResponse))
            print('-----------------------------------------')
    except KeyboardInterrupt:
        print('-----------------------------------------')
        print('Code Kill initiated')
        print('-----------------------------------------')
    logger.info("--------------------End of testing---------------------")