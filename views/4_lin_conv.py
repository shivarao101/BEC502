import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.markdown('### Determines the Linear convolution b/w x(n) & h(n) ')
x=st.text_input('Enter the i/p sequence x(n)',placeholder="1 2 3 4")
x1=[int(i) for i in x.split()]
h=st.text_input('Enter the i/p sequence h(n)',placeholder="1 1 1 1")
h1=[int(i) for i in h.split()]
if x1 and h1:
    y=np.convolve(x1,h1)
    st.write(f"Linear convolution of x(n) and h(n)={y}")
    fig=plt.figure()
    plt.subplot(3,1,1)
    plt.stem(range(len(x1)),x1)
    plt.xlabel('n-->')
    plt.ylabel('x(n)-->')
    plt.title('x(n)')
    plt.subplot(3,1,2)
    plt.stem(range(len(h1)),h1)
    plt.xlabel('n-->')
    plt.ylabel('h(n)-->')
    plt.title('h(n)')
    plt.subplot(3,1,3)
    plt.stem(range(len(y)),y)
    plt.xlabel('n-->')
    plt.ylabel('y(n)-->')
    plt.title('Linear convolution y(n) using DFT and IDFT')
    plt.tight_layout()
    st.pyplot(fig) 