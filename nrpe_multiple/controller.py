#!/usr/bin/python
#encoding:utf-8

##Author:     tancj
##Version:    0.1
##Date:       2014-08-18
#Description  nrpe kill and start


import os
import sys
import ConfigParser
import base64
import getpass
from optparse import OptionParser
from models.parserfile import Parser_config
from models.parserfile import Interaction


#######命令行参数########
def Optimget():
    parser=OptionParser(usage='%prog [-a] [-n] [-s] [-c] [-d] [-e]',version='%prog 0.1')
    parser.add_option('-a','--add',dest='add',action='store_true',default=False,help='追加ip地址等参数')
    parser.add_option('-n','--new',dest='new',action='store_true',default=False,help='清空并添加ip地址等参数')
    parser.add_option('-s','--show',dest='show',action='store_true',default=False,help='显示配置文件里目标机的ip地址')
    parser.add_option('-c','--copy',dest='copy',action='store_true',default=False,help='脚本程序发送到目标机上')
    parser.add_option('-d','--done',dest='done',action='store_true',default=False,help='远程执行nrpe安装脚本')
    parser.add_option('-e','--explain',dest='explain',action='store_true',default=False,help="帮助")
    parser.add_option('-r','--nrpe',dest='nrpe',action='store_true',default=False,help="替换nrpe配置文件中的插件名")
    parser.add_option('-m','--madd',dest='madd',action='store_true',default=False,help="在nrpe配置文件中追加个插件参数")
    parser.add_option('-x','--xinet',dest='xinet',action='store_true',default=False,help="在xinet配置文件中追加个插件参数")
    parser.add_option('-t','--test',dest='test',action='store_true',default=False,help="nrpe 测试")
    parser.add_option('-k','--kill',dest='kill',action='store_true',default=False,help='远程执行nrpe-restart安装脚本')
    (options, args) = parser.parse_args()

#########追加ip地址等参数#######    
    if options.add:
         x = 'y'
         for i in range(100):
             if x =='y':
                 #hostname = raw_input("请输入主机名:")
                 ip = raw_input("请输入IP:")
                 user = raw_input("请输入用户名:")
                 passwd = getpass.getpass('请输入密码: ')
                 passwd = base64.encodestring(passwd)
                 a = raw_input("请输入nrpe被替换的:")
                 b = raw_input("请输入nrpe替换的:")
                 c = raw_input("请输入xinet被替换的:")
                 d = raw_input("请输入xinet替换的:")
                 path = os.getcwd()
                 file = open(path+"/config/host.conf","a")
                 file.write("\n[%s]\n" %ip)
                 #file.write("hostname = %s\n" %hostname)
                 file.write("ip = %s\n" %ip)
                 file.write("user = %s\n" %user)
                 file.write("passwd  = %s" %passwd)
                 file.write("a = %s\n" %a)
                 file.write("b = %s\n" %b)
                 file.write("c = %s\n" %c)
                 file.write("d = %s\n" %d)
                 file.close()
                 print "输入(y)继续添加配置文件，按其他任意键退出："
                 y = raw_input()
                 x =y.strip()
             else:
                 break
    
    #if options.bing:
     #   local_ip = raw_input("请输入本机ip地址:")
      #  ip_port = raw_input("请输入正确的目标机网卡的物理端口(例如:eth0 请使用ip route show命令查询)")
       # string1=


########清空并添加ip地址等参数########
    if options.new:
         
        print '是否清空配置文件信息 请输入(yes or y)继续,按其他任意键退出:'
        judge=raw_input()
        if judge=='yes' or judge=='y':
            path = os.getcwd()

########### 清空文件 然后退出###########
            file = open(path+'/config/host.conf','w')
            file.close()

##########写入配置文件###########            
            x = 'y'
            for i in range(100):
                if x =='y':
                    #hostname = raw_input("请输入主机名:")
                    ip = raw_input("请输入IP:")
                    user = raw_input("请输入用户名:")
                    passwd = getpass.getpass('请输入密码: ')
                    passwd = base64.encodestring(passwd)
                    a = raw_input("请输入nrpe被替换的:")
                    b = raw_input("请输入nrpe替换的:")
                    c = raw_input("请输入xinet被替换的:")
                    d = raw_input("请输入xinet替换的:")
                    
                    path = os.getcwd()
                    file = open(path+"/config/host.conf","a")
                    file.write("\n[%s]\n" %ip)
                    file.write("ip = %s\n" %ip)
                    file.write("user = %s\n" %user)
                    file.write("passwd  = %s" %passwd)
                    file.write("a = %s\n" %a)
                    file.write("b = %s\n" %b)
                    file.write("c = %s\n" %c)
                    file.write("d = %s\n" %d)
                    file.close()
                    print "输入(y)继续添加配置文件，按其他任意键退出："
                    y = raw_input()
                    x =y.strip()
                else:
                    break


    if options.show:
        p = Parser_config()
        hosts = p.readoptions()
        print hosts
        for i in hosts:
            cf = ConfigParser.ConfigParser()
            cf.read("config/host.conf")
            print '   IP   :',cf.get(i,'ip')


#########帮助信息#########
    if options.explain:
        print ' -e: 帮助 \n -a: 追加ip地址等参数 \n -n: 清空并添加ip地址等参数 \n -s: 显示配置文件里目标机的ip地址 \n -c: 脚本程序发送到目标机上 \n -d: 远程执行nrpe安装脚本 \n -m: 在nrpe配置文件中追加个插件参数(未启用) \n -r: 替换nrpe配置文件中的插件名 \n -x: 替换xinet配置文件中的插件名 \n -t: nrpe 测试 \n -k: 远程执行nrpe-restart脚本'

    p = Parser_config()
    hosts = p.readoptions()
    
    if options.copy:
        for i in hosts:
            cf = ConfigParser.ConfigParser()
            cf.read("config/host.conf")
            IP = cf.get(i,'ip')
            passwd1 = cf.get(i,'passwd')
            passwd2 = passwd1.strip()
            PASSWD = base64.decodestring(passwd2)
            USER = cf.get(i,'user')
            path = os.getcwd()
            
            Interaction(USER,PASSWD,IP,"scp -r "+path+"/nrpe_install "+IP+":/home",60)
            Interaction(USER,PASSWD,IP,"ssh "+IP+" chmod -R 777 /home/nrpe_install",30)
            
            Interaction(USER,PASSWD,IP,"scp -r "+path+"/scripts/nrpe-restart.py "+IP+":/home/nrpe_install/scripts",60)
            Interaction(USER,PASSWD,IP,"ssh "+IP+" chmod 777 /home/nrpe-restart.py",30)
            

            Interaction(USER,PASSWD,IP,"scp -r "+path+"/scripts/nrpe-test.py "+IP+":/home/nrpe_install/scripts",60)
            Interaction(USER,PASSWD,IP,"ssh "+IP+" chmod 777 /home/nrpe-test.py",30)
            

            print "IP "+IP+" OK"



    if options.madd:
        x = 'y'
        for i in range(100):
            if x =='y':
                command_filename = raw_input("请输入command 文件名:")
                script_filename = raw_input("请输入script文件名:")
                nrpe_parameter = raw_input("请输入新脚本的参数:")
                new_parameter = nrpe_parameter.replace(' ','\ ')
                new_string = 'command'+'['+command_filename+']'+'='+'/usr/local/nagios/libexec/'+script_filename+'\ '+new_parameter
                print new_string
                for i in hosts:
                    cf = ConfigParser.ConfigParser()
                    cf.read('config/madd.conf')
                    IP = cf.get(i,'ip')
                    passwd1 = cf.get(i,'passwd')
                    passwd2 = passwd1.strip()
                    PASSWD = base64.decodestring(passwd2)
                    USER = cf.get(i,'user')
                    path = os.getcwd()
                    Interaction(USER,PASSWD,IP,"ssh "+IP+" sed -i '\$a\\%s' //usr/local/nagios/etc/nrpe.cfg" %new_string,15)
                    print IP+':追加成功 !'
                print "输入(y)继续添加配置文件，按其他任意键退出："
                y = raw_input()
                x =y.strip()
            else:
                break


    if options.nrpe:

        for i in hosts:
            cf = ConfigParser.ConfigParser()
            cf.read('config/host.conf')
            passwd1 = cf.get(i,'passwd')
            passwd2 = passwd1.strip()
            PASSWD = base64.decodestring(passwd2)
            USER = cf.get(i,'user')
            IP = cf.get(i,'ip')
            a = cf.get(i,'a')
            b = cf.get(i,'b')
            a = a.replace('[','\\\[')
            a = a.replace(']','\\\]')
            a = a.replace('/','\\\/')
            a = a.replace(' ','\ ')


            b = b.replace('[','\\\[')
            b = b.replace(']','\\\]')
            b = b.replace('/','\\\/')
            b = b.replace(' ','\ ')
            
            new_string = 's/'+a+'/'+b+'/g'
            path = os.getcwd()
            Interaction(USER,PASSWD,IP,"ssh "+IP+" sed -i '\\%s' /usr/local/nagios/etc/nrpe.cfg" %new_string,15)
            print IP+':nrpe配置文件替换成功 !'

    if options.xinet:

        for i in hosts:
            cf = ConfigParser.ConfigParser()
            cf.read('config/host.conf')
            passwd1 = cf.get(i,'passwd')
            passwd2 = passwd1.strip()
            PASSWD = base64.decodestring(passwd2)
            USER = cf.get(i,'user')
            IP = cf.get(i,'ip')
            c = cf.get(i,'c')
            d = cf.get(i,'d')
            
            c = c.replace('[','\\\[')
            c = c.replace(']','\\\]')
            c = c.replace('/','\\\/')
            c = c.replace(' ','\ ')


            d = d.replace('[','\\\[')
            d = d.replace(']','\\\]')
            d = d.replace('/','\\\/')
            d = d.replace(' ','\ ')
            
            new_string = 's/'+c+'/'+d+'/g'
            path = os.getcwd()
            Interaction(USER,PASSWD,IP,"ssh "+IP+" sed -i '\\%s' /etc/xinetd.d/nrpe" %new_string,15)
            print IP+':xinet替换成功 !'
    

    if options.done:
        
        for i in hosts:
            cf = ConfigParser.ConfigParser()
            cf.read('config/host.conf')
            IP = cf.get(i,'ip')
            passwd1 = cf.get(i,'passwd')
            passwd2 = passwd1.strip()
            PASSWD = base64.decodestring(passwd2)
            USER = cf.get(i,'user')
            path = os.getcwd()
            Interaction(USER,PASSWD,IP,"ssh "+IP+" python /home/nrpe_install/nrpe-install.py",1800)
            print IP+':nrpe安装完毕！！'

            
    if options.test:

        for i in hosts:
            cf = ConfigParser.ConfigParser()
            cf.read('config/host.conf')
            IP = cf.get(i,'ip')
            passwd1 = cf.get(i,'passwd')
            passwd2 = passwd1.strip()
            PASSWD = base64.decodestring(passwd2)
            USER = cf.get(i,'user')
            path = os.getcwd()
            Interaction(USER,PASSWD,IP,"ssh "+IP+" python /home/nrpe_install/scripts/nrpe-test.py",15)
            print IP+':测试完毕 请查看log.conf文件！！'


    if options.kill:

        for i in hosts:
            cf = ConfigParser.ConfigParser()
            cf.read('config/host.conf')
            IP = cf.get(i,'ip')
            passwd1 = cf.get(i,'passwd')
            passwd2 = passwd1.strip()
            PASSWD = base64.decodestring(passwd2)
            USER = cf.get(i,'user')
            path = os.getcwd()
            Interaction(USER,PASSWD,IP,"ssh "+IP+" python /home/nrpe_install/scripts/nrpe-restart.py",15)
            print IP+':nrpe 服务重启完毕！！'

if __name__ == '__main__':
    Optimget()
