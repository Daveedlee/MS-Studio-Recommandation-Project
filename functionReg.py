# Remove $ and , sign for convert object dtype to int dtype

def replace_all(df,column_name):
    df[column_name]=df[column_name].map(lambda x : x.replace(',','') if type(x) is str else x )
    df[column_name]=df[column_name].map(lambda x : x.replace('$','') if type(x) is str else x )
    return(df)
    
    
    
#fucntion to remove outlier
def remove_outlier(df_in, col_name):
    q1 = df_in[col_name].quantile(0.25)
    q3 = df_in[col_name].quantile(0.75)
    iqr = q3-q1 #Interquartile range
    fence_low  = q1-1.5*iqr
    fence_high = q3+1.5*iqr
    df_out = df_in.loc[(df_in[col_name] > fence_low) & (df_in[col_name] < fence_high)]
    return df_out    