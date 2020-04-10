#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ����ƻ�
���ڣ�2020.4.6
"""

import random



#0 - rockʯͷ
#1 - Spockʷ����
#2 - paperֽ
#3 - lizard����
#4 - scissors����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=='ʯͷ':
		   return 0
    elif name=='ʷ����':
		   return 1
    elif name=='��':
		   return 2
    elif name=="����":
		   return 3
    elif name=="����":
		   return 4    
    else:
		   print("Error: No Correct Name") 


   


def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
		    return "ʯͷ"
    elif number==1:
		    return "ʷ����"
    elif number==2:
		    return "��"
    elif number==3:
		    return "����"
    elif number==4:
	        return "����"
    else:
		    print('Error')
    



def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """


    print("-----------------")
    print("����ѡ��Ϊ��",player_choice)
    player_choice_number=name_to_number(player_choice)
    comp_number=random.randrange(0,5)
    computer_choice=number_to_name(comp_number)
    print("�������ѡ��Ϊ��",computer_choice)
    x=(player_choice_number-comp_number)%5   #���������������������Ĳ�ֵ���������ʤ���������ֵ����1����2������ʤ���ļ��������ֵ����3����4������5ȡ������Ϊ�˿�����5����
    
    if x==3 or x==4:
		    print("�����Ӯ�ˣ�")
    elif x==1 or x==2:
		    print("��Ӯ�ˣ�")
    elif x==0:
		    print("���͵��Գ���һ���أ�")
    else:
		    print("Error")
	
     

   


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)


