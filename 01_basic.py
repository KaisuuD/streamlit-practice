import streamlit as st

st.write("Hello, Streamlit!")
# streamlit run 01_basic.py 启动本地项目

st.write('# Markdown supportted!')
# 支持markdown语法

'字符串/变量/列表/字典等python数据类型，可以直接显示'

a = 89 * 98
a
# 显示变量

[1,9,9,4,8,6]
# 显示列表

{'name': 'Alice', 'age': 25, 'city': 'Beijing'}
# 显示字典

st.title('Title🤔')
# 显示标题

st.image('./img/愚人.jpg', width =200)
# 显示图片

import pandas as pd
#pandas 常见的数据分析库

df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]})
# 常用方法 用于表示表格

st.dataframe(df)
# 交互式表格展示数据 可以下载，搜索，全屏现实表格

st.divider()
# 分割线

st.table(df)
# 静态表格展示数据



