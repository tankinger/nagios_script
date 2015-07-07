#!/usr/bin/python
#encoding=utf-8

import os
import sys
import ConfigParser
import pexpect
import sys
import re
import time

def Interaction(cmd,timeout):
    foo = pexpect.spawn(cmd,timeout=timeout)
    index = foo.expect(["Y/n","(?i)password:","(?i)newest version","(?i)yes/no",pexpect.EOF,pexpect.TIMEOUT])
    if index == 0:
        foo.sendline("Y")
        num=0
    if index == 1:
        foo.sendline("kedaadmin")
        num=0
    if index == 2:
        num=0
    if index == 3:
        foo.sendline("yes")
        foo.expect("(?i)password:")
        foo.sendline("kedaadmin")
        num=0
    if index == 4:
        print "子程序的退出"
        num=1
    if index == 5:
        print "等待目标正则表达式超时"
        num=1
    foo.expect(pexpect.EOF)
    foo.close()
    return num

def nagios_plugins():
	user_mk = os.system("useradd nagios -s /sbin/nologin")
	path=os.chdir('/home/nrpe_install/software_nagios')
	os.system('tar -zxvf nagios-plugins-2.0.tar.gz')
	path=os.chdir('/home/nrpe_install/software_nagios/nagios-plugins-2.0')
	os.system('./configure --prefix=/usr/local/nagios')
	os.system('make')
	os.system('make install')   
	os.system('chown nagios.nagios /usr/local/nagios')
	os.system('chmod  -R  777 /usr/local/nagios')
    
def nrpe():
        path=os.chdir('/home/nrpe_install/software_nagios')
        os.system('tar -zxvf nrpe-2.15.tar.gz')
        path=os.chdir('/home/nrpe_install/software_nagios/nrpe-2.15')
        os.system('./configure --with-ssl-lib=/usr/lib/x86_64-linux-gnu')
	os.system('make all')
	os.system('make install-plugin')
	os.system('make install-daemon')
	os.system('make install-daemon-config')
	os.system('make install-xinetd')
	path=os.chdir('/usr/local/nagios/etc')
	os.system('chmod 777 nrpe.cfg')
	

def nrpe_pid():
    pid1=os.system("pidof nrpe")
    if (pid1!=0):
        print pid1
        print 'nrpe need to start'
        os.system('/usr/local/nagios/bin/nrpe -c /usr/local/nagios/etc/nrpe.cfg -d')
        pid_check=os.system('pidof nrpe')
        if (pid_check==0):
            print 'nrpe start successful'
        if (pid1==0):
            z=os.popen('pidof nrpe')
            old_id=z.read()
            print 'old id is %s' %old_id
            print 'nrpe need to kill'

            p=os.popen('pidof nrpe')
            x=p.read()
            cmd='kill %s' %x
            os.system(cmd)
            print 'kill old id %s' %old_id
            os.system('/usr/local/nagios/bin/nrpe -c /usr/local/nagios/etc/nrpe.cfg -d')
            print 'nrpe start successful'
            y=os.popen('pidof nrpe')
            new_id=y.read()
            print 'new id is %s' %new_id
	
def ip_address():
    ef=[]
    for line in os.popen('ip route show'):
        test=re.findall(r"src\s+(\S+)\s*", line)
        if re.findall(r"src\s+(\S+)\s*", line):
            ef.append(test)
    jjj=len(ef)
    if (jjj==1):
        kkk= ef[0][0]
    if (jjj>1):
        for line in os.popen('ip route show'):
            test=re.findall(r"br-ex\s+proto\s+kernel\s+scope\s+link\s+src\s+(\S+)\s*", line)
            if re.findall(r"br-ex\s+proto\s+kernel\s+scope\s+link\s+src\s+(\S+)\s*", line):
                kkk=test[0]
    return kkk


def xinet():
    os.system("/etc/init.d/xinetd restart")

def time():
    import time
    t=time.strftime('%Y-%m-%d  %H:%M:%S',time.localtime(time.time()))
    return t

def main():
    software_name=['gcc','apache2','nagios-plugins','nagios-nrpe-plugin','nagios-nrpe-server','build-essential','libssl-dev','libgd2-xpm-dev','xinetd','make','gawk']
    #software_name=['gcc','123']
    new_ip='10.9.32.132'
    path=os.chdir('/home/nrpe_install')
    passwd=os.system('debconf-set-selections mysql-passwd')
    update_info=os.system("apt-get update")
    if (update_info==0):
        result=[]
        a=[] 
        for i in software_name:
            cmd="apt-get install %s" %i
            install=Interaction(cmd,1200)
            if (install==0):
                abc='result of %s:!!OK' %i
            if (install==1):
                install=Interaction(cmd,1200)
                if (install==1):
                    abc='result of %s:!!WARNING' %i
                    result.append(abc)
        
        Interaction("ssh "+new_ip+" echo '\\\n' \>\> /home/nrpe_multiple/log/log.conf",60)
        
        ip_add=ip_address()
        
        Interaction("ssh "+new_ip+" echo '[%s]' \>\> /home/nrpe_multiple/log/log.conf" %ip_add,60)
        t=time()
        
        Interaction("ssh "+new_ip+" echo '%s' \>\> /home/nrpe_multiple/log/log.conf" %t,60)
        for i in result:
            if 'WARNING' in i:
                print i
                Interaction("ssh "+new_ip+" echo '%s' \>\> /home/nrpe_multiple/log/log.conf" %i,60)
        Interaction("ssh "+new_ip+" echo 'apt-get install 安装完毕！！' \>\> /home/nrpe_multiple/log/log.conf",60)
                
        
        nagios_plugins()
        nrpe()
        os.system("scp /home/nrpe_install/scripts/check_memory.memory /usr/local/nagios/libexec")
        os.system("chmod 777 /usr/local/nagios/libexec/check_memory.memory")
        os.system("scp /home/nrpe_install/scripts/nrpe.cfg /usr/local/nagios/etc")
        os.system("chmod 777 /usr/local/nagios/etc/nrpe.cfg")
        os.system("scp /home/nrpe_install/scripts/nrpe /etc/xinetd.d")
        os.system("chmod 777 /etc/xinetd.d/nrpe")
        nrpe_pid()
        xinet()

        Interaction("ssh "+new_ip+" echo 'nrpe 安装完毕！！' \>\> /home/nrpe_multiple/log/log.conf",60)

    else:
        Interaction("ssh "+new_ip+" echo '\\\n' \>\> /home/nrpe_multiple/log/log.conf",60)
        ip_add=ip_address()
        Interaction("ssh "+new_ip+" echo '[%s]' \>\> /home/nrpe_multiple/log/log.conf" %ip_add,60)
        t=time()
        Interaction("ssh "+new_ip+" echo '%s' \>\> /home/nrpe_multiple/log/log.conf" %t,60)
        Interaction("ssh "+new_ip+" echo '无法更新下载 请检查网络！！' \>\> /home/nrpe_multiple/log/log.conf",60)
if __name__=='__main__':
    main()
 


