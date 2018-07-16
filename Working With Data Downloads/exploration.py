if __name__ == "__main__":
    
    import pandas as pd
    import numpy as np
    
    data = pd.read_csv('data/CRDC2013_14.csv', encoding="Latin-1")
    #counts the number of schools that fall within each category
    #print( data['JJ'].value_counts())
    #print( data['SCH_STATUS_MAGNET'].value_counts())
    
    #two pivot tables that aggregate total Male and total Female based on JJ and SCH_STATUS_MAGNET
    tables= pd.pivot_table(data, index=['JJ', 'SCH_STATUS_MAGNET'], values=["TOT_ENR_M", "TOT_ENR_F"],aggfunc=np.sum)
    
    print(tables)