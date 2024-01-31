#!/usr/bin/env python
# coding: utf-8

# In[4]:


from pyecharts import options as opts

from pyecharts.charts import Liquid
c = (
    Liquid() # 水球图
    .add("Honkai", [0.6, 0.4],shape="arrow",color =["pink","lightblue"],background_color="black")  # "lq" 悬浮信息，前者是显示的数值，后者是上浮的面积
    .set_global_opts(title_opts=opts.TitleOpts
                     (
                         title="Honkai",
                         pos_left="center",
                         pos_top="20%",
                         title_textstyle_opts=opts.TextStyleOpts(color="violet")
                        
                     
                     )
                     )  #标题
    .render("liquid_base.html")
)




# import openai_secret_manager
# import openai
# from pyecharts.charts import Line
# from pyecharts import options as opts
# from pyecharts_javascripthon import online
# import json

# # 设置 Notion API 密钥
# secrets = openai_secret_manager.get_secret("notion")
# notion_api_key = secrets["api_key"]

# # 设置 Notion 数据库 ID 和要更新的数据行的 ID
# database_id = "your_database_id"
# row_id = "your_row_id"

# # 初始化 Notion 客户端
# notion = Client(auth=notion_api_key)

# # 获取数据行
# row = notion.pages.retrieve(page_id=row_id)

# # 获取数据列
# data_column = row.properties["Data"].number

# # 创建折线图
# line = Line()

# # 添加数据
# line.add_xaxis(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
# line.add_yaxis('Data', data_column)

# # 设置全局选项
# line.set_global_opts(title_opts=opts.TitleOpts(title='Data Visualization'))

# # 在线更新数据
# online_update = online.OnlineUpdater(line)

# # 定义点击事件回调函数
# @online.on(online_update, 'click')
# def on_click(params):
#     # 获取当前点击的数据点的索引
#     index = params['dataIndex']

#     # 更新 Notion 数据
#     new_data = [120, 100, 180, 200, 90, 150, 170]
#     data_column[index] = new_data[index]
#     row.set(properties={"Data": {"number": data_column}})

#     # 更新图表数据
#     online_update.add_data(0, new_data[index])

# # 生成HTML文件
# line.render('line_chart.html')


# In[ ]:




