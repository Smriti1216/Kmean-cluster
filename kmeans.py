import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans 
from sklearn.preprocessing import StandardScaler
data={'class': [10,12,14,18],
      'roll no':[2,4,8,12],
      'marks':[70,75,80,85]}
df=pd.DataFrame(data)
print(df)

op---
   class  roll no  marks
0     10        2     70
1     12        4     75
2     14        8     80
3     18       12     85

print(df.head(3))

​op------

   class  roll no  marks
0     10        2     70
1     12        4     75
2     14        8     80

df=df.dropna()

scaled_df = StandardScaler().fit_transform(df)

print(scaled_df[:4])

op-----
[[-1.18321596 -1.1717002  -1.34164079]
 [-0.50709255 -0.65094455 -0.4472136 ]
 [ 0.16903085  0.39056673  0.4472136 ]
 [ 1.52127766  1.43207802  1.34164079]]

kmeans