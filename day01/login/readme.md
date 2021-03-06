﻿# python练习--用户登陆验证程序说明

标签（空格分隔）： login 用户登录 密码验证 锁定

---
###**1.功能简介**
此程序模拟用户登录验证的过程，实现用户名输入、黑名单检测、用户有效性判别、密码输入及验证等。用户在3次以内输入正确密码登陆成功，连续输错3次密码登陆失败，且该用户名被记录在黑名单，黑名单中的用户被锁定不能再登陆。
###**2.实现方法**
本程序采用python语言编写，将各项任务进行分解并定义对应的函数来处理，从而使程序结构清晰，易于维护。主要编写了四个函数：
```python
login()  #登陆函数，为主函数，完成用户名检测和密码验证
inquire_blacklist(name) #查询用户名是否在黑名单中
inquire_userlist(name) #查询用户名是否在用户名单中,并返回密码或None
add_blacklist(name) #添加用户名到黑名单文件
```
**函数调用框架**：运行`login()`-->输入用户名-->调用`inquire_blacklist(name)`进行黑名单检测-->调用`inquire_userlist(name)`进行用户名有效性判别，有效则返回用户密码，再与输入密码对比验证-->连续输错3次密码则调用`add_blacklist(name)`添加用户到黑名单。
###**3.流程图**
![用户登录验证程序流程图](http://images2017.cnblogs.com/blog/726802/201708/726802-20170830223631749-422629623.png)
更多信息请前往 [本人博客](http://www.cnblogs.com/byron-li/p/7455729.html) 了解，谢谢！








