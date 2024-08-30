import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import copy
st.markdown('### Linear and circular convolution using DFT and IDFT')
x=st.text_input('Enter the i/p sequence x(n)',placeholder="1 2 3 4")
x1=[int(i) for i in x.split()]
h=st.text_input('Enter the i/p sequence h(n)',placeholder="1 1 1 1")
h1=[int(i) for i in h.split()]
if x1 and h1:
    N=len(h1)+len(x1)-1
    x2=copy.copy(x1)
    h2=copy.copy(h1)
    st.write(f"{len(x2)} point FFT of x={np.fft.fft(x2)}")
    st.write(f"{len(h2)} point FFT of h={np.fft.fft(h2)}")
    x2=x2+[0]*(N-len(x2))
    h2=h2+[0]*(N-len(h2))
    X2=np.fft.fft(x2)
    H2=np.fft.fft(h2)
    Y=np.array(X2)*np.array(H2)
    y=np.fft.ifft(Y)
    y=np.real(y)
    y1=np.real(np.fft.ifft(np.fft.fft(x1)*np.fft.fft(h1)))
    st.write(f"{N} point FFT of x={X2}")
    st.write(f"{N} point FFT of h={H2}")
    st.write(f"Linear convolution using DFT and IDFT y={y}")
    st.write(f"Circular convolution using DFT and IDFT y={y1}")
    fig=plt.figure()
    plt.subplot(2,1,1)
    plt.stem(range(len(y)),y)
    plt.xlabel('n-->')
    plt.ylabel('y(n)-->')
    plt.title('Linear convolution y(n) using DFT and IDFT')
    plt.subplot(2,1,2)
    plt.stem(range(len(y1)),y1)
    plt.xlabel('n-->')
    plt.ylabel('h(n)-->')
    plt.title('circular convolution y(n) using DFT and IDFT')
    plt.tight_layout()
    st.pyplot(fig) 