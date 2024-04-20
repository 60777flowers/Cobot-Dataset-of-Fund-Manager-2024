import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from scipy.stats import norm

import warnings

#中文绘图支持
matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 指定默认字体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题
#matplotlib.reParams['font.sans-serif']= ['Microsoft YaHei']


#屏蔽警告
warnings.filterwarnings("ignore")

# Load the uploaded Excel file
file_path = 'P2_Related_Data.xlsx'
data = pd.read_excel(file_path)

# Display the first few rows of the dataframe to understand its structure
data.head()

# Group data by industry and count the number of bonds in each industry
industry_counts = data['所属行业分类(YY)'].value_counts()

# Plot a pie chart
plt.figure(figsize=(10, 8))
plt.pie(industry_counts, labels=industry_counts.index, autopct='%1.1f%%', startangle=140, pctdistance=0.85, wedgeprops=dict(width=0.4),textprops={'fontsize': 6})
plt.title('债券持有行业分布环状图')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.

# Show the pie chart
plt.show()
