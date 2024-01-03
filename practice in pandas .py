# EXPLAIN HOW TO CREATE A SERIES FROM DICTIONARY 
import pandas as pd 
dic1={
    "Name":["nafees","ahmad","haider"],
    "Country":["Pakistan","Germany","Pakistan"]
}

dic2=pd.Series(dic1)
print(dic2)

# CREATE EMPTY DATAFRAME 

D1=()

D2=pd.DataFrame(D1)

print(D2)

# HOW WILL YOU ADD A COLUMN FROM EXISTING DATA FRAME

dic1={
    "Name":["nafees","ahmad","haider"],
    "Country":["Pakistan","Germany","Pakistan"]
}

dic2=pd.DataFrame(dic1)


dic2["age"]=[15,27,17]
print(dic2)


import pandas as pd

# Create an example DataFrame
df = pd.DataFrame({
    "Name": ["nafees", "ahmad", "haider"],
    "Country": ["Pakistan", "Germany", "Pakistan"],
    "Age": [25, 30, 22]
})

# Retrieve a single column, for example, the "Country" column
country_column = df["Country"]


# Display the retrieved column
print(country_column)

#EXPLAIN ABOUT CATEGORICAL DATA IN PYTHON

#ABOUT IT 

#  Categoricals are a pandas data type corresponding to categorical 
# variables in statistics. A categorical variable takes on a limited
# , and usually fixed, number of possible values 


# Examples are gender, social class, blood type, country affiliation
# , observation time or rating via Likert scales.
# FOR SERIES

S1=pd.Series(
    ["ahmad","nafees","syed kabir"] , dtype="category"
)

print(S1)

# FOR DATA FRAME


S1=pd.DataFrame(
    ["ahmad","nafees","syed kabir"] , dtype="category"
)

print(S1)

