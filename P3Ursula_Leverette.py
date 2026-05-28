Athlete Evants
import pandas as pd
mySports = pd.read_csv("/anvil/projects/tdm/data/olympics/athlete_events.csv")
mySports.head()
mySports.shape 
mySports.tail
mySports['Year'].value_counts()
yearCount = mySports['Year'].nunique()
print(yearCount)
yearCount = mySports['Year'].value_counts()
print(yearCount)
import matplotlib.pyplot as plt
plt.figure(figsize=(18, 8))
plt.bar(yearCount.index, yearCount, color='darkorange')  
plt.xlabel("Year")
plt.ylabel("Number of Records")
plt.title("The Frequency a Year appears in the Dataset")
plt.show()
#######Project 3 Questions 4 & 5
pd.set_option('display.max_rows',None) 
mySports.groupby('NOC')['Height'].mean().reset_index(name='Athlete_Avg_Height')
pd.set_option('display.max_rows',None)
mySports.groupby('Sport')['Height'].mean().reset_index(name='SportsAthlete_Avg_Height')

## Question 2 & 3: Grocery Store Transaction by Year & STORE_R
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
myGroceries = pd.read_csv("/anvil/projects/tdm/data/8451/The_Complete_Journey_2_Master/5000_transactions.csv")3myGroceries.columns = ["BASKET_NUM", "HSHD_NUM", "PURCHASE", "PRODUCT_NUM", "SPEND", "UNITS", "STORE_R", "WEEK_NUM", "YEAR"]
myGroceries.head()
pd.set_option('display.max_columns',None)
myGroceries
pd.set_option('display.max_rows',None)
myGroceries.groupby('YEAR')['SPEND'].sum().reset_index(name='Total_Spend')
myGroceries.groupby('STORE_R')['SPEND'].sum().reset_index(name='Total_Spend')

##Question 1: Average Flights (myAirplane_Avg)
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
myAirplane_Avg = pd.read_csv("/anvil/projects/tdm/data/flights/subset/1990.csv")
myAirplane_Avg.head()
pd.set_option('display.max_columns',None)
myAirplane_Avg
