# Author:Byron Li

with open('3_menu.txt', 'r') as f:
    menu_data =eval(f.read())  #读取菜单文件内容并转化成嵌套字典

current_menu_dict=menu_data   #存放当前级及后续各级菜单的嵌套字典，在最低级时为一个列表
upper_menu_list=[]            #存放比当前级更高级别的所有菜单字典的列表，最后一个元素比current_menu_dict多一层父菜单
temp_menu=[]                  #存放当前级菜单的一个临时列表

while(True):
    for i,subject in enumerate(current_menu_dict):                 #循环显示出当前菜单的索引和菜单项
        if type(current_menu_dict) == dict:                        #如果当前菜单不是最低一级菜单，则显示索引和菜单项
           print(''.join(['\t'*len(upper_menu_list),'[',str(i),']',subject]))

        else:                                                      #如果当前菜单是最低一级菜单则只显示菜单项，不显示索引
            print(''.join(['\t'*len(upper_menu_list),subject]))
        temp_menu.append(subject)

    choice=input(''.join(['\t'*len(upper_menu_list),'>>>']))      #输入选项
    if choice.isdigit():                                            #如果输入选项是菜单项对应的数字索引，则进入该菜单项下一级菜单
        if type(current_menu_dict) == dict:                         #如果当前菜单不是最低一级菜单，则通过输入数字索引进入对应菜单项的下一级菜单
            index = int(choice)
            if index >= 0 and index < len(temp_menu):
                key = temp_menu[index]
                upper_menu_list.append(current_menu_dict)           #如果输入数字包含在菜单项索引中，则高级别菜单列表添加当前菜单为其最后一个元素，而当前菜单进入索引对应的下一级菜单
                current_menu_dict = current_menu_dict[key]
            else:
                print('输入错误数字，请重新输入！')
        else:
            print('已是最低级菜单，按b键退回上级菜单，按q键退出!')
    elif choice=='b':                                            #如果输入选项是"b"，则退回到上一级菜单
        if len(upper_menu_list) > 0:                              #如果当前菜单不是最高级菜单，取高级别菜单列表中的最后一个元素为当前菜单字典
            current_menu_dict=upper_menu_list.pop()
        else:                                                    #如果当前菜单已是最高级菜单，不能回退
            print('已是最高级菜单，不能回退，按数字键选择菜单项进入子菜单，按q键退出')
    elif choice=='q':                                            #如果输入选项是"q"，则退出菜单
        print('退出菜单！'.center(50,'*'))
        exit()
    else:
        print('输入错误，请重新输入')
    temp_menu=[]