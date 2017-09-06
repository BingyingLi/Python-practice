# Author:Byron Li

import os
import getpass
BASE_DIR = os.path.dirname(__file__)   #获取文件目录路径
userlist='userlist.txt'     #存取已注册用户名单文件，包括用户名和密码
userlist_path = os.path.join(BASE_DIR,userlist)    #注册用户名单文件路径

def inquire_userlist(name,password):   #查询用户名是否在注册用户名单中
    with open(userlist_path, 'r+') as f:
        line = f.readline()
        while(line):
            pos=f.tell()
            line=f.readline()
            if [name,password] == line.split()[0:2]:
                times=int(line.split()[2])
                line=line.replace(str(times),str(times+1))
                f.seek(pos)
                f.write(line)
                return times+1
    return None


while(True):
    username = input("请输入用户名：")
    password = input("请输入密码：")
    login_times=inquire_userlist(username,password)   #查询输入用户名和密码是否正确,正确则返回登陆次数
    if login_times:
        print('欢迎%s第%d次登陆!'%(username,login_times))
        if login_times==1:
            salary = input("请输入工资：")
        break
    else:
        print('用户名或密码错误,请重新输入：')

'''
if login():  #执行登陆函数
    print('登陆成功！'.center(47,'*'))
else:
    print('登陆失败！'.center(47,'*'))
'''