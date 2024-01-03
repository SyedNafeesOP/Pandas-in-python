#DATA FRAME IS A MULTI DIMENTIAL DATA STRUCTURE IN PYTHON
import pandas as pd
var=[1,2,3,4,5]
var1=pd.DataFrame(var,index=['FIRST','SECOND','THIRD','FOURTH','FIFTH'])
print(var1)
print(type(var1))

Dic={
    "SPORTS":["CRICKET","FOOTBALL","BASKETBALL"],
    "GOAT":["VORAT KHOLI","CRISTIANO RONALDO","LABRON JABES,MICHALJORDAN"]
    }
Dic1=pd.DataFrame(Dic)
print(Dic)    

dic={
    "First":[1,2,3,4,5],"Second":[1,2,3,4,5]
}
var=pd.DataFrame(dic,columns=["First"],index=["a","b","c","d","e"])
print(var)
print(type(var))

lis1=[1,2,3,4,5],[5,6,7,8,9]
var1=pd.DataFrame(lis1)
print(var1)


sr = {
    "s": pd.Series([1, 2, 3, 4, 5]),
    "r": pd.Series([6, 7, 8, 9, 10])  # Adjusted the values for the 'r' Series
}

s1 = pd.DataFrame(sr)
print(s1)





