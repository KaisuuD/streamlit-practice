import streamlit as st

number = st.radio("Select a number", [1, 2, 3, 4, 5],
         index=None)
# 按钮组
if number:
    st.write("You selected:", number)

st.divider()

color = st.selectbox("Select a color", 
             ["Red", "Green", "Blue"], index=1)
# 单选框
if color:
    st.write("You selected:", color)

st.divider()

fruits = st.multiselect("Select a fruit", 
             ["Apple", "Banana", "Orange", "Pineapple", "Watermelon"],
             default=["Apple", "Banana"])
# 多选框
for fruit in fruits:
    st.write(f"You selected {fruit}")

st.divider()

level = st.slider("How much do you like this app?",
           min_value=0, max_value=100, value=50, step=1)
# 滑动条
st.write(f"You selected: {level}")

st.divider()

uploaded_file = st.file_uploader("Upload a picture", type=["png", "jpg", "jpeg"])
# 文件上传，实例化一个文件对象

if uploaded_file:
    st.write(f'Uploaded file name: {uploaded_file.name}')
    # st.write(f'file content: {uploaded_file.read()}') 
    # 读取文件内容，读图片没有意义

