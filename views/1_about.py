import streamlit as st
from pathlib import Path
from PIL import Image
current_dir= Path(__file__).parent if "__file__" in locals() else Path.cwd()
college_pic =  "assets/college.png"
college_pic=Image.open(college_pic)
col1, col2 = st.columns((0.3,0.7),gap="large")
with col1:
    st.image(college_pic, width=150)
with col2:
    st.markdown(f"### {'Vivekananda College of Engineering and Technology'}")
    st.write(f"##### {'Department of ECE, VCET Puttur'}")
st.markdown('## DSP lab experiments')
st.write('''1. Program to generate following discrete time sequences 
          a. unit impulse, b unit step,c. exponential seq, d. sinusoidal seq, e. random seq''')
st.write('''2. Program to perform the following operations on signals. 
a) Signal addition, b) Signal multiplication, c)Scaling, d) Shifting, e)Folding''')
st.write('''3. Program to perform convolution of two given sequences (without using built-in function) and display the 
signals''')
st.write('''4. Consider a causal system y(n) = 0.9y(n-1)+x(n). 
a) Determine H(z) and sketch its pole zero plot. 
b) Plot |H(ejω)| and ∠ H(ejω) 
c) Determine the impulse response h(n). ''')
st.write('''5. Computation of N point DFT of a given sequence (without using built-in function) and to plot the 
magnitude and phase spectrum. ''')
st.write('''6. Using the DFT and IDFT, compute the following for any two given sequences a)Circular convolution 
b) Linear convolution ''')
st.write('''7. Verification of Linearity property, circular time shift property & circular frequency shift property
of DFT.''')
st.write('8. Develop decimation in time radix-2 FFT algorithm without using built-in functions')
st.write('9. Design and implementation of digital low pass FIR filter using a window to meet the given specifications')
st.write('10. Design and implementation of digital high pass FIR filter using a window to meet the given specifications')
st.write('11. Design and implementation of digital IIR Butterworth low pass filter to meet the given specifications')
st.write('12. Design and implementation of digital IIR Butterworth high pass filter to meet the given specifications')
