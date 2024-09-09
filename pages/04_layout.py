import streamlit as st

with st.sidebar:
# 侧边栏
    name = st.text_input("Enter your name:")
    # 输入框的类型为text_input，可以输入单行文字
    if name:
        st.write(f"Hello, {name}")

column1, column2, column3 = st.columns([1,3,1]) 
# 分栏，参数为每栏的宽度比例，比例之和为100%
# column1, column2, column3 = st.columns(3) 等分表示三列

with column1:
    password = st.text_input("Enter your password", type="password")
    # 输入框的类型为text_input，可以输入单行文字，且输入内容会被隐藏

with column2:
    paragraph = st.text_area("Enter your message:")
    # 输入框的类型为text_area，可以输入多行文字

with column3:
    age = st.number_input("Enter your age:", min_value=0, max_value=120, value=25, step=1)
    # 输入框的类型为number_input，可以输入数字。默认精度为2位小数
    st.write(f"Your age is {age}")

st.divider()

tab1, tab2, tab3 = st.tabs(['专栏1', '专栏2', '专栏3'])
# 选项卡，参数为选项卡名称列表

with tab1:
    checked = st.checkbox("I agree to the terms and conditions")
    # 输入框的类型为checkbox，可以勾选或不勾选
    if checked:
        st.write("Thank you for agreeing to the terms and conditions.")

with tab2:
    submitted = st.button("Submit")
    if submitted:
        st.write("Form submitted successfully!")

with tab3:
    level = st.slider("How much do you like this app?",
           min_value=0, max_value=100, value=50, step=1)

st.divider()

with st.expander("About"):
# 展开器，可以折叠或展开内容
    st.write("This is an example of a Streamlit app.")