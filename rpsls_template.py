#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：段云辉
日期：2020.4.6
"""

import random



#0 - rock石头
#1 - Spock史波克
#2 - paper纸
#3 - lizard蜥蜴
#4 - scissors剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    if name=='石头':
		   return 0
    elif name=='史波克':
		   return 1
    elif name=='布':
		   return 2
    elif name=="蜥蜴":
		   return 3
    elif name=="剪刀":
		   return 4    
    else:
		   print("Error: No Correct Name") 


   


def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==0:
		    return "石头"
    elif number==1:
		    return "史波克"
    elif number==2:
		    return "布"
    elif number==3:
		    return "蜥蜴"
    elif number==4:
	        return "剪刀"
    else:
		    print('Error')
    



def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """


    print("-----------------")
    print("您的选择为：",player_choice)
    player_choice_number=name_to_number(player_choice)
    comp_number=random.randrange(0,5)
    computer_choice=number_to_name(comp_number)
    print("计算机的选择为：",computer_choice)
    x=(player_choice_number-comp_number)%5   #根据两个结果所代表的数的差值，几种玩家胜利的情况差值都是1或者2，电脑胜利的几种情况差值都是3或者4，除以5取余数是为了控制在5以下
    
    if x==3 or x==4:
		    print("计算机赢了！")
    elif x==1 or x==2:
		    print("您赢了！")
    elif x==0:
		    print("您和电脑出的一样呢！")
    else:
		    print("Error")
	
     

   


# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)


