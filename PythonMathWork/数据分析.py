import pandas as pd
import numpy as np
from Data import *


Time_Data = Get_Data('Time_Data')

#print(Time_Data)
Time_Data_L = pd.DataFrame(Time_Data['L'])
Time_Data_K = pd.DataFrame(Time_Data['K'])
Time_Data_U = pd.DataFrame(Time_Data['U'])
'''
print(Time_Data_L)
#print((1/Time_Data_U[1])/(1/Time_Data_L[1]))
#print(((1/Time_Data_U)/(1/Time_Data_L)).values)
A = np.std((1/Time_Data_K[0])/(1/Time_Data_L[0]))
B = np.std((1/Time_Data_K[1])/(1/Time_Data_L[1]))
C = np.std((1/Time_Data_K[2])/(1/Time_Data_L[2]))
print((A+B+C)/3)
#print(np.std(((1/Time_Data_K)/(1/Time_Data_L)).values))
'''
print(Time_Data_U.iloc[0,])
A = np.std((1/Time_Data_U.iloc[0,])/(1/Time_Data_L.iloc[0,]))
B = np.std((1/Time_Data_U.iloc[1,])/(1/Time_Data_L.iloc[0,]))
C = np.std((1/Time_Data_U.iloc[2,])/(1/Time_Data_L.iloc[0,]))
D = np.std((1/Time_Data_U.iloc[3,])/(1/Time_Data_L.iloc[0,]))
E = np.std((1/Time_Data_U.iloc[4,])/(1/Time_Data_L.iloc[0,]))
print((A+B+C+D+E)/5)


#print(np.mean(Time_Data_L/Time_Data_U))