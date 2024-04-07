def Cost_of_AI(AI_WorkTime):
    '''
    The time mark here is minutes

    The floating cost theory changes according to demand,
    but the computing power of the A100 card is too powerful.
    It is assumed that renting one is enough.
    '''
    Const_Cost = 1887457.356427819
    #wage_to_mend =  470639.7391/250/24/60
    #wage_to_mend = 1.3073326086111112
    Float_Cost = 0.3244555
    #Float_Cost = 0.9781218043055556
    return (Const_Cost+Float_Cost*AI_WorkTime)

def Cost_of_Worker(Human_WorkTime,Yield):
    '''
    The time mark is minutes
    '''
    wage = (0.000008041470351036932*Yield+385750.279023107)/120000
    return (wage*Human_WorkTime)


def generate_combinations():
    for i in range(3):
        for ii in range(3):
            for iii in range(3):
                for iv in range(3):
                    for v in range(3):
                        for vi in range(3):
                            for vii in range(3):
                                for viii in range(3):
                                    for ix in range(3):
                                        for x in range(3):
                                            for xi in range(3):
                                                for xii in range(3):
                                                    for xiii in range(3):
                                                        for xiv in range(3):
                                                            for xv in range(3):
                                                                yield [[i, ii, iii], [iv, v, vi], [vii, viii, ix], [x, xi, xii], [xiii, xiv, xv]]




def Get_Minimized_Cost(T_L_Mat,T_K_Mat,T_U_Mat,Yield):
    Profit = -2.1e9
    Time_proportion = []
    Details = []
    cost = 2.1e9
    for Task_Management in generate_combinations():
        T_L = 0
        T_K = 0
        T_U = 0
        for group_index,group in enumerate(Task_Management):
            for i ,value in enumerate(group):
                if value == 0:
                    T_L += T_L_Mat.iloc[group_index,i]
                elif value == 1:
                    T_K += T_K_Mat.iloc[group_index,i]
                elif value == 2:
                    T_U += T_U_Mat.iloc[group_index,i]
        Total_Cost = Cost_of_Worker(T_L+T_U+0.867*T_K,Yield)+Cost_of_AI(T_K+T_U)
        Total_Profit = Yield - Total_Cost
        if Profit < Total_Profit:
            Profit = Total_Profit
            Time_proportion = [T_L,T_K,T_U]
            Details = [Task_Management]
            cost = Total_Cost
    return {'Profit':Profit,'Cost':cost,'Time':Time_proportion,'Details':Details}


