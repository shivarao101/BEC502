import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random
st.markdown('### Generation of various Discrete time sequences')
N=st.text_input('Enter the no of samples of unit step or unit impulse or exponential or sinusoidal or random sequence',placeholder="100")
a=st.text_input('Enter the amplitude of expoenential seq',placeholder="0.9")
f=st.text_input('Enter the analog freq of sinusoid',placeholder="10")
fs= st.text_input('Enter the sampling freq of sinusoid',placeholder="50")
rn=st.text_input('Enter the range for random number',placeholder="20")
if N and a and f and rn and fs:
    a1=float(a)
    N1=int(N)
    f1=float(f)
    fs1=int(fs)
    rn1=int(rn)
    n=[i for i in np.arange(-N1/2,N1/2)]
    x1= [0]*int(N1/2) + [1] + [0]*(int(N1/2)-1)
    x2= [0]*int(N1/2) + [1]*(int(N1/2))
    n1=[i for i in np.arange(0,N1) ]
    x3=[np.sin(2*np.pi*(f1/fs1*i)) for i in np.arange(0,N1)]
    x4=[(a1)**i for i in np.arange(0,N1) ]
    x5=[random.randint(0,rn1) for i in np.arange(0,N1)]
    fig=plt.figure()
    plt.subplot(2,2,1)
    plt.stem(n,x1)
    plt.xlabel('n-->')
    plt.ylabel('delta(n)-->')
    plt.title('unit impulse')
    plt.subplot(2,2,2)
    plt.stem(n,x2)
    plt.xlabel('n-->')
    plt.ylabel('u(n)-->')
    plt.title('unit step')
    plt.subplot(2,2,3)
    plt.stem(n1,x3)
    plt.xlabel('n-->')
    plt.ylabel('x(n)-->')
    plt.title('sinusoidal seq')
    plt.subplot(2,2,4)
    plt.stem(n1,x4)
    plt.xlabel('n-->')
    plt.ylabel('x(n)-->')
    plt.title('exponential seq')
    plt.tight_layout()
    st.pyplot(fig) 
    fig1=plt.figure()
    plt.stem(n1,x5)
    plt.xlabel('n-->')
    plt.ylabel('x(n)-->')
    plt.title('random seq')
    plt.tight_layout()
    st.pyplot(fig1)
   
