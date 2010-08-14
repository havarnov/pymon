#!/usr/bin/env python
#author: Havar Novik

import time, os

class pymon:

    def iface(self,iface):
        '''This is the function that catches bytes downloaded by the given interface.'''
        self.iface = iface
        file = open('/proc/net/dev', 'r')
        found = False
        filelist = []
        while found == False:
            filelist.append(file.readline())
            if filelist[-1] == "":
                found = True
                filelist.pop()
        for i in range(len(filelist)):
            file_line = filelist[i].split()
            device = '{0}:'.format(self.iface)
            device_test = file_line[0]
            if device_test == device: 
                devinfo = file_line
#                print(devinfo)
        self.dlbytes = devinfo[1]
        return self.dlbytes


    def printinfo(self):
        print('Bytes download trough {0}: {1}'.format(self.iface, self.dlbytes))



    def daily(self):

        dl_prev_day = int(p.iface('wlan0'))
        dl = int(p.iface('wlan0'))
        while 1 == True:
            date = time.strftime('%M')
            print(dl)
            while date == time.strftime('%M'):
                if dl - dl_prev_day > 1000:
                    print('dl for mye')
                    p.chgstatus('wlan0','down')
                    break
                time.sleep(5)
                dl = int(p.iface('wlan0'))
                print('dl under grensen')
            if dl - dl_prev_day > 1000:
                while date == time.strftime('%M'):
                    print('dl for mye, venter pa ny dag')
                    time.sleep(30)
                p.chgstatus('wlan0','up')

            dl_prev_day = dl


    def chgstatus(self, iface, status):
        os.popen('ifconfig {0} {1}'.format(iface, status))



p = pymon()


p.daily()



