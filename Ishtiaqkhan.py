#!/usr/bin/python2

#coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize

from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError

from mechanize import Browser

reload(sys)

sys.setdefaultencoding('utf8')

br = mechanize.Browser()

br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)

br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():

	print "\033[1;96m[!] \x1b[1;91mExit"	os.sys.exit()

def acak(b):

    w = 'ahtdzjc'

    d = ''

    for i in x:

        d += '!'+w[random.randint(0,len(w)-1)]+i

    return cetak(d)

def cetak(b):

    w = 'ahtdzjc'

    for i in w:

        j = w.index(i)

        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))

    x += '\033[0m'

    x = x.replace('!0','\033[0m')

    sys.stdout.write(x+'\n')

def jalan(z):

	for e in z + '\n':

		sys.stdout.write(e)

		sys.stdout.flush()

		time.sleep(00000.1)

#### LOGO ####

logo = """

\033[1;98m   _____   __     ______     ______     ______    

\033[1;97m /\__  _\ /\ \   /\  ___\   /\  ___\   /\  == \   

\033[1;95m \/_/\ \/ \ \ \  \ \ \__ \  \ \  __\   \ \  __<   

\033[1;94m    \ \_\  \ \_\  \ \_____\  \ \_____\  \ \_\ \_\ 

\033[1;93m     \/_/   \/_/   \/_____/   \/_____/   \/_/ /_/ 

\033[1;91m    ║══▒═💀═▒═💀═▒═══¤═¤═¤════════════¤═══¤═══¤═══║

\033[1;96m    ║✯ 𝕮𝖗𝖊𝖆𝖙𝖔𝖗  𝕸𝖗.𝕽𝖆𝖓𝖆 𝕬𝖆𝖍
