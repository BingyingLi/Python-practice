# Author:Byron Li

import os
import getpass
BASE_DIR = os.path.dirname(__file__)   #获取文件目录路径
userlist='userlist.txt'     #存取已注册用户名单文件，包括用户名和密码
blacklist='blacklist.txt'   #存取锁定用户的黑名单文件
userlist_path = os.path.join(BASE_DIR,userlist)    #注册用户名单文件路径
blacklist_path = os.path.join(BASE_DIR,blacklist)  #黑名单文件路径

#----------------------------------------------登陆函数（主函数）-------------------------------------------------------
def login():  #登陆函数
    username = input("请输入用户名：")
    while(True):
        if inquire_blacklist(username):     #查询输入用户名是否在黑名单中
            print("不好意思,此用户名\"%s\"已被锁定,禁止登陆!"%username)
            return False
        else:
            user_password = inquire_userlist(username) #查询输入用户名是否存在注册用户名单中，若存在则返回该用户密码
            if user_password:
                for i in range(3):
                    password = input("请输入密码：") if i==0 else input("密码输入错误，请重新输入密码：")
                    #password = getpass.getpass("请输入密码：") if i == 0 else getpass.getpass("密码输入错误，请重新输入密码：")
                    if password==user_password:
                        print('欢迎%s登陆!'%username)
                        return True
                else:
                    print("您已经连续输错密码3次,用户名将被锁定，禁止再登陆!")
                    add_blacklist(username)             #添加用户名到黑名单文件
                    return False
            else:
                username = input('无效的用户名,请重新输入：')
# ----------------------------------------------------------------------------------------------------------------------


#----------------------------------------------查询黑名单函数-----------------------------------------------------------
def inquire_blacklist(name):   #查询用户名是否在黑名单中
    with open(blacklist_path, 'r') as f:
        for line in f:
            if name==line.strip():
                return True
    return False
# ----------------------------------------------------------------------------------------------------------------------


#----------------------------------------------查询用户名函数-----------------------------------------------------------
def inquire_userlist(name):   #查询用户名是否在注册用户名单中
    with open(userlist_path, 'r') as f:
        for line in f:
            [username,password] = line.split()
            if name==username:
                return password
    return None
# ----------------------------------------------------------------------------------------------------------------------


#----------------------------------------------添加黑名单函数-----------------------------------------------------------
def add_blacklist(name): #添加用户名到黑名单文件
    with open(blacklist_path, 'a') as f:
        f.write(str(name)+'\n')
    return True
# ----------------------------------------------------------------------------------------------------------------------

if login():  #执行登陆函数
    print('登陆成功！'.center(47,'*'))
else:
    print('登陆失败！'.center(47,'*'))