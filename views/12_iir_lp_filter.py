import numpy as np
import streamlit as st
from scipy import signal
import matplotlib.pyplot as plt
st.markdown('### Design IIR Low pass filter using Butterworth filter')
fp=st.text_input('Enter the pass band freq ',placeholder="1500")
fs=st.text_input('Enter the stop band freq ',placeholder="3000")
F=st.text_input('Enter the sampling freq',placeholder="8000")
kp=st.text_input('Enter the passband gain Kp',placeholder="3")
ks=st.text_input('Enter the stop band gain Ks',placeholder="10")
if fp and fs and F and kp and ks:
    fp=float(fp)
    fs=float(fs)
    F=int(F)
    wp=2*fp/F
    ws=2*fs/F
    kp=float(kp)
    ks=float(ks)
    N, Wn = signal.buttord([wp], [ws], kp, ks)
    b, a = signal.butter(N, Wn)
    st.write(f"Filter coeff b={b} and a={a}")
    w, h = signal.freqz(b, a,F)
    w1=[i for i in np.arange(0,F/2,0.5)]
    fig=plt.figure()
    plt.plot(w1, 20 * np.log10(abs(h)))
    plt.xlabel('Frequency(Hz)-->')
    plt.ylabel('Amplitude in dB-->')
    st.pyplot(fig)
