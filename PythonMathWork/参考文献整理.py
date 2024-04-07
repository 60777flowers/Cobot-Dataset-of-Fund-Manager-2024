import re

with open('REF.txt','r',encoding='UTF-8') as REF:
    Dict={}
    for line in REF.readlines():
        #print(line)
        #print(re.search('}',line).span())
        Index = re.search('}',line).span()[0]
        Key = line[9:Index]
        Dict[Key]=line
    Dict = sorted(Dict.items(),key=lambda x:x[0])
    #print(Dict)
    with open("Sorted_REF.txt",'w',encoding='UTF-8') as SR:
        for key, value in Dict:
            SR.writelines(value)