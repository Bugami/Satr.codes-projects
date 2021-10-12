# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 20:25:23 2021

Birthdate day calculation 

@author: Abdullah Albugami
"""

import datetime

def func(**args):
    current = datetime.date.today()
    name_list = []
    age_list  = []
    for name, birthdate in args.items():
        birthdate = datetime.datetime.strptime(birthdate, '%d-%m-%Y')
        age = current.year - birthdate.year - ((current.month, current.day) < (birthdate.month, birthdate.day))
        print(name+' is '+str(age)+' years old and she/he was born on '+ birthdate.date().strftime('%A'))
        name_list.append(name)
        age_list.append(age)
    oldest = name_list[age_list.index(max(age_list))]
    youngest = name_list[age_list.index(min(age_list))]
    print('The oldest one is ' + oldest)
    print('The youngest one is ' + youngest)
    print('Total People: '+str(len(args)))
        

a = {'khalid': '1-2-1989',
     'Nouf': '2-9-2004',
     'Ali': '9-12-2009'}

func(**a)
