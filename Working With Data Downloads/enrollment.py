
import pandas as pd

data = pd.read_csv('data/CRDC2013_14.csv', encoding="Latin-1")

#moves the two columns together
data['total_enrollment'] = data['TOT_ENR_M'] + data['TOT_ENR_F']

all_enrollment = data['total_enrollment'].sum()

columns=['SCH_ENR_HI_M', 
         'SCH_ENR_HI_F', 
         'SCH_ENR_AM_M',
         'SCH_ENR_AM_F',
         'SCH_ENR_AS_M',
         'SCH_ENR_AS_F',
         'SCH_ENR_HP_M',
         'SCH_ENR_HP_F',
         'SCH_ENR_BL_M',
         'SCH_ENR_BL_F',
         'SCH_ENR_WH_M',
         'SCH_ENR_WH_F',
         'SCH_ENR_TR_M', 
         'SCH_ENR_TR_F',
         'TOT_ENR_M',
         'TOT_ENR_F'
        ]
percentage = (data[columns].sum()/all_enrollment)*100
print(percentage)