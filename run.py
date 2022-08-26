# Run.py
import pandas, numpy
import datetime

# 取得現在時間
now = datetime.datetime.now()
txt = '上次更新時間為：' + str(now)

# 轉成df
df = pandas.DataFrame([txt], index=['UpdateTime'])

# 存出檔案
df.to_csv('log.csv', header=False)