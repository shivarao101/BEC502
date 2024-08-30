import streamlit as st
import numpy as np
st.markdown('### 8 point Radix-2 DIT-FFT algorithm')
val1=st.text_input('Enter the i/p sequence x(n)',placeholder="1 2 3 4 0 0 0 0")
x= [int(i)for i in val1.split()]
if x:
    N=len(x)
    V11=[0,0]
    V12=[0,0]
    V21=[0,0]
    V22=[0,0]
    V11[0]=x[0]+x[4]
    V11[1]=x[0]-x[4]
    V12[0]=x[2]+x[6]
    V12[1]=x[2]-x[6]
    V21[0]=x[1]+x[5]
    V21[1]=x[1]-x[5]
    V22[0]=x[3]+x[7]
    V22[1]=x[3]-x[7]
    stage1=[V11[0],V11[1],V12[0],V12[1],V21[0],V21[1],V22[0],V22[1]]
    st.write(f"stage 1 result= {stage1}")
    F1=[0,0,0,0]
    F2=[0,0,0,0]
    for k in range(0,2):
        F1[k]=V11[k]+(np.cos(4*np.pi*k/N)-np.sin(4*np.pi*k/N)*(1j))*V12[k]
        F1[k+2]=V11[k]-(np.cos(4*np.pi*k/N)-np.sin(4*np.pi*k/N)*(1j))*V12[k]
        F2[k]=V21[k]+(np.cos(4*np.pi*k/N)-np.sin(4*np.pi*k/N)*(1j))*V22[k]
        F2[k+2]=V21[k]-(np.cos(4*np.pi*k/N)-np.sin(4*np.pi*k/N)*(1j))*V22[k]
    stage2=(F1,F2)
    st.write(f"stage 2 result= {stage2}")
    X=[0]*N
    for k in range(0,4):
        X[k]=F1[k]+(np.cos(2*np.pi*k/N)-np.sin(2*np.pi*k/N)*(1j))*F2[k]
        X[k+4]=F1[k]-(np.cos(2*np.pi*k/N)-np.sin(2*np.pi*k/N)*(1j))*F2[k]
    stage3=X
    st.write(f"stage 3 Final result= {stage3}")
