# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 21:51:15 2021

@author: jegen
"""

#auto search products and finding reviews 


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import pyautogui,time
from tkinter import *


count = 1

#creating a new window 
def newWindow():
    global count
    driver.execute_script("window.open('about:blank');") 
    driver.switch_to.window(driver.window_handles[count])    
    count = count+1


def printem():
    
    product= ''
    product = E1.get()
    
    
    #first window 
    driver.get('https://www.skroutz.gr/search?keyphrase='+product)
    sleep(1)

    #gsmarena window 
    newWindow()    
    driver.get('https://www.gsmarena.com/res.php3?sSearch='+product)
    sleep(1)

    
    #youtube window
    newWindow()
    driver.get('https://www.youtube.com/results?search_query='+product+' review')
    sleep(1)
    
    #amazon window    
    newWindow()
    driver.get('https://www.amazon.com/s?k='+product)
    sleep(1)
    
    

prod = '' 
driver = webdriver.Firefox(executable_path= "/Users/jegen/Downloads/geckodriver-v0.28.0-win64/geckodriver.exe")

top = Tk()
L1 = Label(top, text="product name")
L1.pack( side = LEFT)

B1 = Button(top, text="search" , command = printem)
B1.pack(side = RIGHT)


E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)




top.mainloop()
