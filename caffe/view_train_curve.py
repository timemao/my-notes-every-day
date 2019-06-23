#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 17:33:08 2018

@author: myj
"""
import re
import matplotlib.pyplot as plt
regex_iteration = re.compile('Iteration (\d+)')
regex_loss = re.compile('loss = ([-+]?[0-9]*\.?[0-9]+([eE]?[-+]?[0-9]+)?)')

filename='train.log'
fr=open(filename)
lines=fr.readlines()
iters=[]
loss=[]
for i in range(527,1539):
    print(i)
    line=lines[i]
    iteration_match = regex_iteration.search(line)
    loss_match=regex_loss.search(line)
    if iteration_match:
        iters.append(float(iteration_match.group(1)))
        loss.append(float(loss_match.group(1)))
    
plt.plot(iters,loss,'m')
plt.legend()
