# Pandas: Create Scatter plot from multiple DataFrame columns 

import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame(
    [[1.038988,    1.15915721, -2.28067047,  2.15586249],
     [1.67701311, -0.29835294,  1.85995237,  0.09892021],
     [-1.27494246, -1.10266464, -0.53293884,  0.65932129],
     [1.57701142, -0.75032143,  1.06973893,  0.82543657],
     [-0.99777099, -0.46051326,  1.43704249,  1.24864683],
     [-0.73344725,  1.63418558,  0.7973022, -1.9192436]
     ],
    columns=['A', 'B', 'C', 'D']
)


ax1 = df.plot(kind='scatter', x='A', y='B', color='g')
ax2 = df.plot(kind='scatter', x='C', y='D', color='r', ax=ax1)

plt.show()
