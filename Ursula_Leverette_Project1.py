Airports
import pandas as pd
myData = pd.read_csv("/anvil/projects/tdm/data/flights/subset/airports.csv")
myData.head()
myData.shape 
myData.tail
myData[(myData['city'] == 'New York') & (myData['state'] == 'NY')]
myData[(myData['city'] == 'Indianapolis') & (myData['state'] == 'IN')]
myData[(myData['city'] == 'Houston') & (myData['state'] == 'TX')]
myData['state'].value_counts()
myTopAPData = myData['state'].value_counts().head()
import matplotlib.pyplot as plt
plt.bar(myTopAPData.index, myTopAPData)

Icecream Products
import pandas as pd
myIData = pd.read_csv("/anvil/projects/tdm/data/icecream/combined/products.csv")
myIData.head()
Number_of_Unique_Brands = myIData["brand"].nunique()
print(Number_of_Unique_Brands)
Count_of_Brand_Rows = myIData['brand'].value_counts()
print(Count_of_Brand_Rows)
import matplotlib.pyplot as plt
plt.bar(Count_of_Brand_Rows.index, Count_of_Brand_Rows)

Icecream Reviewprint(CTN_Row_IRData)

import pandas as pd
myRIData = pd.read_csv("/anvil/projects/tdm/data/icecream/combined/reviews.csv")
myRIData.head()
CTN_Row_IRData = myRIData["brand"].value_counts()
print(CTN_Row_IRData)
import matplotlib.pyplot as plt
plt.bar(CTN_Row_IRData.index,CTN_Row_IRData)
