# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 11:00:00 2021

Bank account using class

@author: a.bugami
"""
from datetime import datetime

class Bank_Account():
    def __init__(self, name, credit=0):
        self.name   = name
        self.credit = credit
    
    def take_date(self):
        date  = datetime.now()
        day   = date.strftime("%A")
        date2 = date.strftime("%d %B, %Y")
        time  = date.strftime('%H:%M%p')        
        return [day, date2, time]
    
    def debt(self, amount):
        self.credit += amount
        datetime1 = self.take_date()
        print("تم إيداع " + str(amount) +" ريال لرصيدك البنكي في يوم "+ datetime1[0]+" التاريخ "+datetime1[1]+" الساعة "+datetime1[2])
    
    def withdraw(self, amount):
        self.credit -= amount
        datetime1 = self.take_date()
        print("تم خصم " + str(amount) +" ريال من رصيدك البنكي في يوم "+ datetime1[0]+" التاريخ "+datetime1[1]+" الساعة "+datetime1[2])
    
    def get_credit(self):
        print("رصيدك البنكي هو "+ str(self.credit) + " ريال")


account1 = Bank_Account("Ahmad")
account1.get_credit()
account1.debt(2000)
account1.get_credit()
account1.withdraw(50)
account1.get_credit()
