import pandas as pd 
import numpy as np

def replace_all(df,column_name):
    df[column_name]=df[column_name].map(lambda x : x.replace(',',''))
    df[column_name]=df[column_name].map(lambda x : x.replace('$',''))
    return(df)