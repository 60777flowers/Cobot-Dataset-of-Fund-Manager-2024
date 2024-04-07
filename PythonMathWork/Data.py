#import pandas as pd

def Get_Data(Type):
    if Type == 'Time_Data':
        Labor_Time = [[15.02,25.14,31],
                      [22.77,107.45,130.45],
                      [6.23,18.65,271.83],
                      [8,25.6,504.96],
                      [21.79,36.2,67.3]]
        AI_Work_Time = [[5.41,17.33,12.47],
                        [18.6,95.4,131.67],
                        [25,15.5,277.75],
                        [4.43,3.83,336.72],
                        [4.1,23.52,52.58]]
        Union_Time = [[5.41,14.64,9.33],
                        [18.6,68.5,85.33],
                        [7.05,10.51,226.33],
                        [4.43,3.83,294.23],
                        [4.1,22.13,45.28]]
        return {'L':Labor_Time,'K':AI_Work_Time,'U':Union_Time}
    if Type == 'Percent_Data':
        Extend = [[0.021982098,0.036792938,0.087811309],
                  [0.013857016,0.065390268,0.079387254],
                  [0.004483286,0.013421073,0.195616641],
                  [0.002863504,0.009163213,0.180744368],
                  [0.050172653,0.083352457,0.154961889]]
        return Extend
    if Type == 'Yield':
        Yield = 1e9
        Unit_Yield = 10000
        Workload = Yield/Unit_Yield
        Unit_Time = 735.8612451
        return {'Yield':Yield,'Unit':Unit_Yield,"Workload":Workload,'Unit_Time':Unit_Time}


#print((pd.DataFrame(Get_Data('Time_Data')['K'])/pd.DataFrame(Get_Data('Time_Data')['L'])).stack().mean())