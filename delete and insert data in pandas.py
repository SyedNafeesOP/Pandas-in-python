# insert
import pandas as pd

var = pd.DataFrame({
    "A": [1, 2, 3, 4, 5],
    "B": [9, 8, 7, 6, 5]
})

var.insert(1, "python", var["A"])

print(var)


var.insert(1, "python_1",[11,12,13,14,15])

print(var)

print(var)

var["python_12"]=var["A"][:3]
print(var)

