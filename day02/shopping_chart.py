# Author:Byron Li
#-*-coding:utf-8-*-

'''----------------------------------------------使用文件说明----------------------------------------------------------
使用文件说明
userlist.txt         存放用户账户信息文件，包括用户名、密码、登陆次数和余额
***_cost_record.txt  存放某用户***消费记录的文件，用户首次购买商品后创建，没有购买过商品的用户不会产生该文件
---------------------------------------------------------------------------------------------------------------------'''
import os
import datetime

def login(name,password):   #用户登陆,用户名和密码验证，登陆成功则返回登陆次数
    with open('userlist.txt', 'r+',encoding='UTF-8') as f:
        line = f.readline()
        while(line):
            pos=f.tell()
            line=f.readline()
            if [name,password] == line.split()[0:2]:
                times=int(line.split()[2])
                line=line.replace(str(times).center(5,' '),str(times+1).center(5,' '))
                f.seek(pos)
                f.write(line)
                return times+1
    return None

def get_balance(name):   #获取用户余额数据
    with open('userlist.txt', 'r',encoding='UTF-8') as f:
        line = f.readline()
        for line in f:
            if name == line.split()[0]:
                return line.split()[3]
    print("用户%s不存在，无法获取其余额信息！"%name)
    return False

def update_balance(name,balance):    #更新用户余额数据
    with open('userlist.txt', 'r+',encoding='UTF-8') as f:
        line = f.readline()
        while(line):
            pos1=f.tell()
            line=f.readline()
            if name == line.split()[0]:
                pos1=pos1+line.find(line.split()[2].center(5,' '))+5
                pos2=f.tell()
                f.seek(pos1)
                f.write(str(balance).rjust(pos2-pos1-2,' '))
                return True
    print("用户%s不存在，无法更新其余额信息！" % name)
    return False

def inquire_cost_record(name):     #查询用户历史消费记录
    if os.path.isfile(''.join([name,'_cost_record.txt'])):
        with open(''.join([name,'_cost_record.txt']), 'r',encoding='UTF-8') as f:
            print("历史消费记录".center(40, '='))
            print(f.read())
            print("".center(46, '='))
            return True
    else:
        print("您还没有任何历史消费记录！")
        return False

def update_cost_record(name,shopping_list):   #更新用户消费记录
    if len(shopping_list)>0:
        if not os.path.isfile(''.join([name, '_cost_record.txt'])):     #第一次创建时第一行标上“商品  价格”
            with open(''.join([name, '_cost_record.txt']), 'a',encoding='UTF-8') as f:
                f.write("%-5s%+20s\n" % ('商品', '价格'))
                f.write(''.join([datetime.datetime.now().strftime('%c'), ' 消费记录']).center(40,'-'))   #写入消费时间信息方便后续查询
                f.write('\n')
                for product in shopping_list:
                    f.write("%-5s%+20s\n"%(product[0],str(product[1])))
        else:
            with open(''.join([name, '_cost_record.txt']), 'a',encoding='UTF-8') as f:
                f.write(''.join([datetime.datetime.now().strftime('%c'), ' 消费记录']).center(40, '-'))
                f.write('\n')
                for product in shopping_list:
                    f.write("%-5s%+20s\n"%(product[0],str(product[1])))
        return True
    else:
        print("您本次没有购买商品，不更新消费记录！")
        return False

def shopping_chart():    #主函数，用户交互，函数调用，结果输出
    product_list=[
        ('Iphone',5000),
        ('自行车',600),
        ('联想电脑',7800),
        ('衬衫',350),
        ('洗衣机',1000),
        ('矿泉水',3),
        ('手表',12000)
    ]   #商店商品列表
    shopping_list=[]   #用户本次购买商品列表
    while(True):
        username = input("请输入用户名：")
        password = input("请输入密码：")
        login_times=login(username,password)   #查询输入用户名和密码是否正确,正确则返回登陆次数
        if login_times:
            print('欢迎%s第%d次登陆!'.center(50,'*')%(username,login_times))
            if login_times==1:
                balance = input("请输入工资：")   #第一次登陆输入账户资金
                while(True):
                    if balance.isdigit():
                        balance=int(balance)
                        break
                    else:
                        balance = input("输入工资有误，请重新输入：")
            else:
                balance=int(get_balance(username))  #非第一次登陆从文件获取账户余额
            while(True):
                print("请选择您要查询消费记录还是购买商品：")
                print("[0] 查询消费记录")
                print("[1] 购买商品")
                choice=input(">>>")
                if choice.isdigit():
                    if int(choice)==0:                 #查询历史消费记录
                        inquire_cost_record(username)
                    elif int(choice)==1:               #购买商品
                        while (True):
                            for index,item in enumerate(product_list):
                                print(index,item)
                            choice=input("请输入商品编号购买商品:")
                            if choice.isdigit():
                                if int(choice)>=0 and int(choice)<len(product_list):
                                    if int(product_list[int(choice)][1])<balance:   #检查余额是否充足，充足则商品购买成功
                                        shopping_list.append(product_list[int(choice)])
                                        balance = balance - int(product_list[int(choice)][1])
                                        print("\033[31;1m%s\033[0m已加入购物车中，您的当前余额是\033[31;1m%s元\033[0m" %(product_list[int(choice)][0],balance))
                                    else:
                                        print("\033[41;1m您的余额只剩%s元，无法购买%s！\033[0m" %(balance,product_list[int(choice)][0]))
                                else:
                                    print("输入编号错误，请重新输入!")
                            elif choice=='q':      #退出账号登陆，退出前打印本次购买清单和余额信息，并更新到文件
                                if len(shopping_list)>0:
                                    print("本次购买商品清单".center(50,'-'))
                                    for product in shopping_list:
                                        print("%-5s%+20s"%(product[0],str(product[1])))
                                    print("".center(50, '-'))
                                    print("您的余额：\033[31;1m%s元\033[0m"%balance)
                                    update_cost_record(username,shopping_list)
                                    update_balance(username, balance)
                                    print("退出登陆！".center(50, '*'))
                                    exit()
                                else:
                                    print("您本次没有消费记录，欢迎下次购买！")
                                    print("退出登陆！".center(50, '*'))
                                    exit()
                            else:
                                print("选项输入错误，请重新输入！")
                    else:
                        print("选项输入错误，请重新输入！")
                elif choice=='q':   #退出账号登陆
                    print("退出登陆！".center(50, '*'))
                    exit()
                else:
                    print("选项输入错误，请重新输入！")
            break
        else:
            print('用户名或密码错误,请重新输入!')

shopping_chart() #主程序运行