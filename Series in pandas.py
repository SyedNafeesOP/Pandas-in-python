#series data structure
#series:
#IT IS DEFINES AS ONE DIMENTIAL ARRAY THAT IS CAPABLE OF STORING VARIOUS DATA TYPE 
#import pandas as pd 
#a=pd.series()
#print(a)

# now we discuss about series
import pandas as pd

x=[3,5,7,8,4]
var=pd.Series(x,index=['FIRST','SECOND','THIRD','FOURTH','FIFTH'])#,dtype="float")
print(var)
print(type(var))
print(var[2])
# we can also change the data type by using dtype function

dic={
    "name":["Python","C","C++","Rust","Java"],
    "rank":[1,5,3,4,2],
}
dic1=pd.Series(dic)
print(dic1)

var=pd.Series(5,index=[1,2,3,4,5,6])
print(var)

var1=pd.Series(5,index=[1,2,3,4,5,6])
var2=pd.Series(6,index=[1,2,3,4,])
print(var1*var2)


dic1={
    "Goats":["RONALDO", "MESSI","NEYMAR"],
    "RANK":[1,2,3]
}

dic2=pd.DataFrame(dic1,index=["FIRST","SECOND","THIRD"])

print(dic2)

