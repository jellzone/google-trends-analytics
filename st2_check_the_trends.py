import pandas as pd
import matplotlib.pyplot as plt

# 从CSV文件中读取数据
data = pd.read_csv('trends_data.csv', parse_dates=['date'])

# 设置筛选关键字的数量，默认为前4个
num_keywords = 4

# 选择要显示的关键字列
selected_columns = data.columns[1:num_keywords+1]

# 绘制样条曲线图
plt.figure(figsize=(12, 6))
for keyword in selected_columns:
    plt.plot(data['date'], data[keyword], label=keyword)

# 设置图表标题和坐标轴标签
plt.title('Google Trends Data')
plt.xlabel('Date')
plt.ylabel('Trends Interest')

# 显示图例
plt.legend()

# 显示图表
plt.show()
