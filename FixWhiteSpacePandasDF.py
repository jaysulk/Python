import pandas as pd

def FixWhiteSpacePandasDF(data):
    # fix trailing and preceding whitspace in column names    
    data = data.rename(columns=lambda x: x.strip())
    
    return data
