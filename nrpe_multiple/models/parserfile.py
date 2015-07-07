#!/usr/bin/python
#encoding:utf-8

import os
import ConfigParser
import pexpect
import sys
import time
###设置系统默认编码，以便能够识别中文###
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Parser_config:
    def readoptions(self):
        cf = ConfigParser.ConfigParser()
        cf.read('config/host.conf')
        return cf.sections()

    
def Interaction(user,passwd,host,cmd,timeout):
    foo = pexpect.spawn(cmd,timeout=timeout)
    index = foo.expect(["yes/no","(?i)password:",pexpect.EOF,pexpect.TIMEOUT])
    if index == 0:
        foo.sendline("yes")
        foo.expect("(?i)password:")
        foo.sendline(passwd)
    elif index == 1:
        foo.sendline(passwd)
    elif index == 2:
        print "子程序的退出"
    elif index == 3:
        print "等待目标正则表达式超时"
    foo.expect(pexpect.EOF)
    foo.close()


    
