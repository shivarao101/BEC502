import streamlit as st
import control as ct
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
st.markdown('### Determines TF Pole-zero plot and Impulse response of given causal system')
x=st.text_input('Enter the nr coeff',placeholder="1 0")
nr=[float(i) for i in x.split()]
h=st.text_input('Enter the dr coeff',placeholder="1 -0.9")
dr=[float(i) for i in h.split()]
if nr and dr:
    H = ct.tf(nr,dr, dt=True)
    st.write(f" #### Transfer function H(z) {H}")
    fig1=plt.figure()
    plt.plot()
    ct.pzmap(H)
    T=[i for i in np.arange(0,20)]
    n, h = ct.impulse_response(H, T)
    st.write(f"Impulse response is {h}")
    st.pyplot(fig1)
    fig2=plt.figure()
    w,h1=signal.freqz(nr,dr,512)
    plt.subplot(3,1,1)
    plt.plot(w,np.abs(h1))
    plt.title('Magnitude response')
    plt.subplot(3,1,2)
    plt.plot(w,np.angle(h1))
    plt.title('Phase response')
    plt.subplot(3,1,3)
    plt.stem(n,h)
    plt.title('Impulse response')
    plt.tight_layout()
    st.pyplot(fig2) 