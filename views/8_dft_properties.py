import streamlit as st
import numpy as np
from operator import mod
from cmath import exp
st.markdown('### DFT properties')
st.markdown('#### To Verify Linearity, Circular time shift and Circular freq shift properties')
st.markdown('#### 1. Linearity property ')
st.markdown('##### a1x1(n)+a2x2(n) <--DFT--> a1X1(k)+a2X2(k)')
x=st.text_input('Enter the i/p sequence x1(n)')
x1=[int(i) for i in x.split()]
h=st.text_input('Enter the i/p sequence x2(n)')
h1=[int(i) for i in h.split()]
a1=st.text_input('Enter a1')
a2=st.text_input('Enter a2')
if x1 and h1 and a1 and a2 :
    a1=int(a1)
    a2=int(a2)
    lhs=np.fft.fft(a1*np.array(x1)+a2*np.array(h1))
    st.write('Lhs=dft(a1*x1(n)+a2*x2(n))',lhs)
    rhs=a1*np.fft.fft(x1) + a2*np.fft.fft(h1)
    st.write('Rhs=a1*dft(x1(n))+a2*dft(x2(n))',rhs)
st.markdown('#### 2. Circular time shift property ')
st.latex(r'''x(n-l)_N<---DFT--->X(k)\omega_N ^{kl}
''')
ip=st.text_input('Enter the i/p sequence x(n)')
ip1=[int(i) for i in ip.split()]
sh=st.text_input('Enter the shift')
if ip1 and sh:
    sh=int(sh)
    N=len(ip1)
    y=[0]*N
    for i in range(N):
        y[i]=ip1[mod((i-sh),N)]
    st.write('shifted seq ',y)
    st.write('DFT of shifted seq ',np.fft.fft(y))
    X=np.fft.fft(ip1)
    Y=[0]*N
    for k in range(len(X)):
        Y[k]=X[k]*exp(-1j*2*np.pi*sh*k/N)
    st.write('DFT of original seq',X)
    st.write('Multiplication of DFT with complex exponential',Y)
st.markdown('#### 3. Circular freq shift property ')
st.latex(r'''x(n)\omega_N^{nl}<---DFT--->X(k-l)_N
''')
res=st.text_input('Enter the i/p sequence X(n)')
res1=[int(i) for i in res.split()]
shift=st.text_input('Enter the freq shift')
if shift and res1:
    shift=int(shift)
    X=np.fft.fft(res1)
    N=len(res1)
    y=np.zeros((N),'complex')
    for i in range(len(res1)):
        y[i]=res1[i]*exp(1j*2*np.pi*shift*i/N)
    st.write('DFT of x(n)Wn',np.fft.fft(y))
    Y=np.zeros((N),'complex')
    for i in range(len(X)):
        Y[i]=X[mod((i-shift),N)]
    st.write('Circular freq shift X(k-shift)N',Y)









