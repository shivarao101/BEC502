import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from operator import mod
st.markdown('### Perform various signal operations')
x=st.text_input('Enter the first i/p sequence x(n)',placeholder="1 2 3 4")
x1=[int(i) for i in x.split()]
h=st.text_input('Enter the second i/p sequence h(n)',placeholder="4 3 2 1")
h1=[int(i) for i in h.split()]
sf=st.text_input('Enter the shift factor',placeholder="2")
sc=st.text_input('Enter the scale factor',placeholder="2")

if x1 and h1 and sc and sf:
    sf1=int(sf)
    sc1=int(sc)
    y1=np.array(x1) + np.array(h1)
    y2=np.array(x1) * np.array(h1)
    y3=np.zeros(int(0.5*len(x1)))
    y4=np.zeros(2*len(x1))
    for n in range(len(y4)):
        if n%sc1==0:
            y4[n]=x1[n//sc1]
    for n in range(len(y3)):
        y3[n]=x1[sc1*n]
    neg=[-i for i in range(len(x1))]
    y5=np.zeros(len(x1)+sf1)
    for n in range(len(x1)):
        y5[n+sf1]=x1[n]
   
    st.write(f"addition of x(n) & h(n)={y1}")
    st.write(f"multiplication of x(n) & h(n)={y2}")
    st.write(f"Compressed x(n)={y3}")
    st.write(f"Expanded x(n)={y4}")
    st.write(f"Shifted seq x(n-2)={y5}")
    fig=plt.figure()
    plt.subplot(3,2,1)
    plt.stem(range(len(y1)),y1)
    plt.xlabel('n-->')
    plt.ylabel('x(n)-->')
    plt.title('x(n)+h(n)')
    plt.subplot(3,2,2)
    plt.stem(range(len(y2)),y2)
    plt.xlabel('n-->')
    plt.ylabel('h(n)-->')
    plt.title('x(n)*h(n)')
    plt.subplot(3,2,3)
    plt.stem(range(len(y3)),y3)
    plt.xlabel('n-->')
    plt.ylabel('y(n)-->')
    plt.title('x(kn) compressed')
    plt.subplot(3,2,4)
    plt.stem(range(len(y4)),y4)
    plt.xlabel('n-->')
    plt.ylabel('y(n)-->')
    plt.title('x(n/k) expanded')
    plt.subplot(3,2,5)
    plt.stem(neg,x1)
    plt.xlabel('n-->')
    plt.ylabel('y(n)-->')
    plt.title('x(-n) folded')
    plt.subplot(3,2,6)
    plt.stem(range(len(y5)),y5)
    plt.xlabel('n-->')
    plt.ylabel('y(n)-->')
    plt.title('x(n-2) shift')
    plt.tight_layout()
    st.pyplot(fig) 
    
