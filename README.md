# streamlit-practice

## Introduction

### Download streamlit
```
pip install streamlit
```

### Run the app
```
streamlit run app.py
```
### Streamlit 是一个开源的 Python 库，用于快速创建和分享数据应用。它允许你通过简单的 Python 脚本快速构建数据可视化和机器学习模型的可视化界面。Streamlit 的语法非常直观，基于 Python，但也有一些特定的函数和组件用于构建用户界面。下面是一些 Streamlit 最常用的语法和组件：

## 1. 显示文本
```
st.title('我的第一个 Streamlit 应用')  
st.header('这是一个标题')  
st.write('这是一段普通文本。')  
st.markdown('这是 **Markdown** 文本。')
```


## 2. 显示数据
```
data = {'Name': ['Tom', 'Jane', 'Alice'], 'Age': [28, 34, 29]}  
df = pd.DataFrame(data)  
  
st.write(df)  # 显示 DataFrame  
st.table(df)  # 以表格形式显示 DataFrame
```

## 3. 交互

### 滑块
```
age = st.slider('选择年龄', 0, 100, 25)  
st.write(f'你选择的年龄是: {age}')
```

### 复选框
```
checked = st.checkbox('你同意条款吗？')  
st.write(f'你同意条款: {checked}')
```

### 单选按钮
```
gender = st.radio('选择性别', ['男', '女'])  
st.write(f'你选择的性别: {gender}')
```

### 下拉菜单
```
options = st.multiselect('选择你喜欢的颜色', ['红', '绿', '蓝', '黄'])  
st.write(f'你喜欢的颜色是: {options}')
```

### 文本输入框
```
name = st.text_input('请输入你的名字')  
st.write(f'你输入的名字是: {name}')
```

### 上传文件
```
file_uploaded = st.file_uploader("上传一个文件", type=['csv', 'txt'])  
if file_uploaded is not None:  
    st.write(f'文件内容: {file_uploaded.getvalue().decode()}')
```

## 4. 图表
```
import matplotlib.pyplot as plt  
  
fig, ax = plt.subplots()  
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  
st.pyplot(fig)
```

## 5. 按钮和事件
```
if st.button('点击我'):  
    st.write('按钮被点击了！')
```

## 6. 布局

### 列
```
col1, col2 = st.columns(2)  
col1.write('这是第一列')  
col2.write('这是第二列')
```


