


# Python金融图表绘制——折线图 https://mp.weixin.qq.com/s/cTD0VBKoZvzfKK4xG3ErQg


# 准备工作
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates

# 导入数据
stock_return = pd.read_excel('t.xlsx', names=['日付け', 'TOPIX先物', '日経225先物'])

# 设置图形样式和中文字体
plt.style.use('ggplot')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建图形和子图
fig, axes = plt.subplots(figsize=(10, 5), dpi=120)

# 绘制折线图
axes.plot(stock_return['日付け'], stock_return['TOPIX先物'], color='#155ca8', ls='-', lw=1.0, label='TOPIX先物')
axes.plot(stock_return['日付け'], stock_return['日経225先物'], color='#5a5a5a', ls='--', lw=1.0, label='日経225先物')

# 调整X轴刻度
axes.xaxis.set_major_locator(ticker.IndexLocator(base=50, offset=0))
axes.xaxis.set_minor_locator(ticker.NullLocator())
axes.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# 区域填充
y1 = stock_return['TOPIX先物']
y2 = stock_return['日経225先物']
axes.fill_between(stock_return['日付け'], y1, y2, where=y1 > y2, color='#f5f5f5')
axes.fill_between(stock_return['日付け'], y1, y2, where=y1 < y2, color='#ca4f4f')

# 添加数据来源和日期范围标签
plt.text(0.5, -0.1, '数据来源：Investing.com', horizontalalignment='center', verticalalignment='center', transform=axes.transAxes, fontsize=12)
start_date = stock_return['日付け'].min().strftime('%Y-%m-%d')
end_date = stock_return['日付け'].max().strftime('%Y-%m-%d')
plt.text(0.5, -0.15, f'日期范围：{start_date} - {end_date}', horizontalalignment='center', verticalalignment='center', transform=axes.transAxes, fontsize=12)

# 添加标题和图例
plt.text(0.5, 1.1, 'TOPIX先物-日経225先物 Spread', horizontalalignment='center', verticalalignment='center', transform=axes.transAxes, fontsize=16)
plt.legend(loc='upper left', fontsize=12)

# 保存图像
plt.savefig('financial_chart.png', dpi=300, bbox_inches='tight')

# 显示图形
plt.show()
