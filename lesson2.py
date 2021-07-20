# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 11:32:28 2021

@author: nitac
"""

score = input('成績?')
score= int(score)
if score  >= 60:
    print('及格')
else:
    print('不及格')
    
    
    
score=int(input('成績?'))

if score>=90:
    print('A')
elif score>=75:
    print('B')
elif score>=60:
    print('C')
else:
    print('D')
    
    
    
    
math=input('數學成績?')
math=int(math)
eng=input('英文成績?')
eng=int(eng)

if math>=90 and eng >=90:
    print('有獎學金')
elif math==100 or eng ==100:
    print('有獎學金')
else:
    print('沒獎學金')
    
    
    
math=input('數學成績?')  
math=int(math) 
eng=input('英文成績?')
eng=int(eng)

if math>=90 and eng>=90:
    print('有獎品')
elif math<60 and eng<60:
    print('要處罰')
else:
    print('OK')
    
    

