#!/usr/bin/env python
#author: Havar Novik

import time, os, subprocess

class pymon:

    def iface(self,iface,ud):
        '''This is the function that catches bytes downloaded by the given interface.'''
        self.iface = iface
        if ud == 'dl':
            ud = 1
        elif ud == 'ul':
            ud = 5
        else:
            #error message
            print('Eiter dl for download or ul for uplaod')
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
        self.dlbytes = devinfo[ud]
        return self.dlbytes


    def printinfo(self):
        print('Bytes download trough {0}: {1}'.format(self.iface, self.dlbytes))



    def daily(self):

        dl_prev_day = int(p.iface('wlan0','dl'))
        dl = int(p.iface('wlan0','dl'))
        ul_prev_day = int(p.iface('wlan0','ul'))
        ul = int(p.iface('wlan0','ul'))
        while 1 == True:
            date = time.strftime('%M')
            #print(dl)
            while date == time.strftime('%M'):
                if dl - dl_prev_day > 1000 or ul - ul_prev_day > 1000:
                    print('dl eller ul for mye')
                    p.chgstatus('wlan0','down')
                    break
                time.sleep(5)
                dl = int(p.iface('wlan0'))
                ul = int(p.iface('wlan0'))
                print('dl under grensen')
            if dl - dl_prev_day > 1000 or ul - ul_prev_day > 1000:
                while date == time.strftime('%M'):
                    print('dl/ul for mye, venter pa ny dag')
                    time.sleep(30)
                p.chgstatus('wlan0','up')

            dl_prev_day = dl
            ul_prec_day = ul


    def chgstatus(self, iface, status):
        subprocess.call('ifconfig'', iface, status)



p = pymon()


p.daily()



