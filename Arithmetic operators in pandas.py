import pandas as pd
var=pd.DataFrame({
    "a":[1,2,3,4,5],
    "b":[6,7,8,9,10]
}) 
var["c"]=var["a"]+var["b"]
#var["c"]=var["a"]-var["b"]
#var["c"]=var["a"]*var["b"]
print(var)
var["python"]=var["a"]<=20
print(var)
