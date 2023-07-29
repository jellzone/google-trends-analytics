import pandas as pd
from pytrends.request import TrendReq

# 读取CSV文件并获取关键字列表
keywords_df = pd.read_csv('keywords.csv')
keywords_list = keywords_df['keywords'].tolist()

# 初始化pytrends
pytrends = TrendReq(hl='en-US', tz=360)

# 设置查询参数
timeframe = 'today 5-y'  # 搜索过去5年的数据
geo = ''  # 全球范围，如果需要指定地区，请填写相应的地区代码

# 获取并汇总数据
all_data = pd.DataFrame()

for keyword in keywords_list:
    pytrends.build_payload([keyword], timeframe=timeframe, geo=geo)
    data = pytrends.interest_over_time()
    
    if not data.empty:
        data = data.drop(labels=['isPartial'], axis='columns')
        all_data = pd.concat([all_data, data], axis=1)

# 保存汇总数据到CSV文件
all_data.to_csv('trends_data.csv', index=True)

print("Google Trends数据已保存到 trends_data.csv 文件中。")
