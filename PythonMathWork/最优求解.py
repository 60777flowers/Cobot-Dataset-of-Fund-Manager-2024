import pandas as pd
from Data import *
from Functions import *
import time



if __name__ == "__main__":
    time_start = time.time()  # 记录开始时间
    Time_Data = Get_Data('Time_Data')
    Percent_Data = Get_Data('Percent_Data')

    for Yield in [1e6,5e6,1e7,3e7,6e7,1e8,2e8,3e8,4e8,5e8,6e8,7e8,8e8,9e8,1e9]:#产生多少收益时
        Efficiency_of_K = pd.DataFrame(Time_Data['L'])/pd.DataFrame(Time_Data['K'])
        Efficiency_of_U = pd.DataFrame(Time_Data['L']) / pd.DataFrame(Time_Data['U'])

        #Work_Load = pd.DataFrame(Percent_Data)*Get_Data('Profit')['Workload']*Get_Data('Profit')['Unit_Time']
        Work_Load = pd.DataFrame(Percent_Data) * (Yield/10000) * 735.8612451

        Time_Consume_of_Human = Work_Load
        Time_Consume_of_AI = Work_Load/Efficiency_of_K
        Time_Consume_of_Union = Work_Load/Efficiency_of_U

        #print(Time_Consume_of_AI)
        #print(Time_Consume_of_Union)
        Minimized_Cost = Get_Minimized_Cost(Time_Consume_of_Human,Time_Consume_of_AI,Time_Consume_of_Union,Yield)
        #Minimized_Cost = {'A':1,'B':2}
        print(Minimized_Cost)
        with open('Minimized_Cost3.txt','a') as file:
            file.write('Yield:'+str(Yield)+'\n'+'Minimized Cost:'+str(Minimized_Cost)+'\n')
    time_end = time.time()
    time_sum = time_end - time_start
    print(time_sum)

