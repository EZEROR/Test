#!/usr/bin/env python
# coding: utf-8

# In[2]:


from pyecharts import options as opts
from pyecharts.charts import Liquid
c = (
    Liquid() # 水球图
    .add("lq", [0.8, 1])  # "lq" 悬浮信息，前者是显示的数值，后者是上浮的面积
    .set_global_opts(title_opts=opts.TitleOpts(title="次元能"))  #标题
    .render("liquid_base.html")
)


# In[ ]:





# In[ ]:





# In[ ]:





# In[3]:





# In[ ]:




