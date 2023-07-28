# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 14:10:08 2020

@author: jwang4
"""



from __future__ import division
import pandas as pd
import numpy as np
from numpy import *
import math
import json
import sys
import datetime as dt
from datetime import datetime
import win32com.client
import opendssdirect as dss
import os
import csv
import matplotlib.pyplot as plt
import pylab


FeederDir = r'C:\Users\jwang4\Desktop\AMI\Test_SI\\'

MasterFile = os.path.join(FeederDir,'Test_qsts.dss')


dss.run_command('Compile '+MasterFile)


circuit = dss.Circuit
print(circuit.Name())


dss.run_command('solve')
summary = dss.run_command('summary')
print(summary)

AllNodeNames = circuit.YNodeOrder()
node_number = len(AllNodeNames)   
Vbase_allnode = [0]*node_number
ii = 0

for node in AllNodeNames:
    circuit.SetActiveBus(node)
    Vbase_allnode[ii] = dss.Bus.kVBase()*1000
    ii = ii + 1
    

ii = 0


dss.run_command('set mode=yearly')
dss.run_command('set number=1')
dss.run_command('set stepsize=3600s')
dss.run_command('set hour=0')
present_step=1
Tmax=24

while present_step <= Tmax:
    
    h = dss.Solution.DblHour()

    print('****************** time step= '+ str(present_step) + ' : ' + str(h) +'*****************')
    
    

    dss.run_command('solve')
            

    present_step = present_step + 1   



dss.run_command('export monitor L1_L')

print("File compiled successfully")



