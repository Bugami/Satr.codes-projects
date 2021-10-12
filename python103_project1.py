# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 20:25:23 2021

Subject: convert to Object Oriented Programming


    def update_sale_price(bike, sale_price):
        if bike['sold'] == True:
            print('Action not allowed, Bike has already been sold')
        else:
            bike['sale_price'] = sale_price
    
    
    def sell(bike):
        bike['sold'] = True
    
    
    def create_bike(description, cost, sale_price, condition):
        return {
            'description': description,
            'cost': cost,
            'sale_price': sale_price,
            'condition': condition,
            'sold': False
        }
    
    
    bike1 = create_bike('Univega Alpina, orange', cost=100, sale_price=500, condition=0.5)
    update_sale_price(bike1, 350)
    sell(bike1)

@author: Abdullah Albugami
"""


class bike:
    
    def __init__(self, description, cost, sale_price, condition, sold=False):
        self.description = description
        self.cost        = cost
        self.sale_price  = sale_price
        self.condition   = condition
        self.sold        = sold
    
    def update_sale_price(self, sale_price):
        if self.sold == True:
            print('Action not allowed. Bike has already been sold')
        else:
            self.sale_price = sale_price
    
    def sell(self):
        self.sold = True
        

bike1 = bike('Univega Alpina. orange', 100, 500, 0.5)
bike1.update_sale_price(350)
print(bike1.sale_price)
bike1.sell()
bike1.update_sale_price(350)
