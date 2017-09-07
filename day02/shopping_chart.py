# Author:Byron Li
#-*-coding:utf-8-*-

'''----------------------------------------------使用文件说明----------------------------------------------------------
使用文件说明
userlist.txt         存放用户账户信息文件，包括用户名、密码、登陆次数和余额
xxx_cost_record.txt  存放某用户xxx消费记录的文件，用户首次购买商品后创建，没有购买过商品的用户不会产生该文件
---------------------------------------------------------------------------------------------------------------------'''
import os

def login(name,password):   #查询用户名是否在注册用户名单中
    with open('userlist.txt', 'r+') as f:
        line = f.readline()
        while(line):
            pos=f.tell()
            line=f.readline()
            if [name,password] == line.split()[0:2]:
                times=int(line.split()[2])
                line=line.replace(str(times).center(3,' '),str(times+1).center(3,' '))
                f.seek(pos)
                f.write(line)
                return times+1
    return None

def get_balance(name):
    with open('userlist.txt', 'r') as f:
        for line in f:
            if name == line.split()[0]:
                return line.split()[3]
    print("用户%s不存在，无法获取其余额信息！"%name)
    return False

def update_balance(name,balance):
    with open('userlist.txt', 'r+') as f:
        line = f.readline()
        while(line):
            pos=f.tell()
            line=f.readline()
            if name == line.split()[0]:
                line=line.replace(''.join([' ',line.split()[3],'\n']),''.join([' ',str(balance),'\n']))
                f.seek(pos)
                f.write(line)
                return True
    print("用户%s不存在，无法更新其余额信息！" % name)
    return False

def inquire_cost_record(name):
    if os.path.isfile(''.join([name,'_cost_record'])):
        with open(''.join([name,'_cost_record']), 'r') as f:
            print(f.read())
    return False

def show_product_list():
    for index,item in enumerate(product_list):
        print(index,item)

product_list=[
    ('Iphone 6',5000),
    ('自行车',600),
    ('联想电脑',7800),
    ('衬衫',350),
    ('矿泉水',3),
    ('手表',12000)
]

while(True):
    username = input("请输入用户名：")
    password = input("请输入密码：")
    login_times=login(username,password)   #查询输入用户名和密码是否正确,正确则返回登陆次数
    if login_times:
        print('欢迎%s第%d次登陆!'%(username,login_times))
        if login_times==1:
            balance = input("请输入工资：")
            while(True):
                if balance.isdigit():
                    balance=int(balance)
                    break
                else:
                    balance = input("输入工资有误，请重新输入！")
        else:
            balance=get_balance(username)
        while(True):
            print("请选择您要查询消费记录还是购买商品：")
            print("[0] 查询消费记录")
            print("[1] 购买商品")
            choice=input(">>>")
            if str(choice)==0:
                inquire_cost_record(username)

            elif str(choice)==1:
                show_product_list()
            elif choice=='q':
                exit()
            else:
                print("选项输入错误，请重新输入！")

        break
    else:
        print('用户名或密码错误,请重新输入!')

'''
if login():  #执行登陆函数
    print('登陆成功！'.center(47,'*'))
else:
    print('登陆失败！'.center(47,'*'))
'''