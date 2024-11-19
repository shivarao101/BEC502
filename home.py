import streamlit as st
from pathlib import Path
from PIL import Image
@st.cache_data
def Pageviews():
    return []
pageviews=Pageviews()
pageviews.append('dummy')
About_page =st.Page(
    page="views/1_about.py",
    title="About",
)
project_1_page =st.Page(
    page="views/2_dtseq.py",
    title="Generation of various Discrete time sequences",
)
project_2_page =st.Page(
    page="views/3_sgnoper.py",
    title="Perform various signal operations",
)
project_3_page =st.Page(
    page="views/4_lin_conv.py",
    title="Determine the Linear convolution b/w x(n) & h(n) without built-in function",
)
project_4_page =st.Page(
    page="views/5_tf_imp.py",
    title="Determine the TF and impulse response of a given causal system",
)
project_5_page =st.Page(
    page="views/6_dft.py",
    title="Determine N point DFT and plot magnitude and phase response without built-in function",
)
project_6_page =st.Page(
    page="views/7_circ_lin.py",
    title="Determine linear and circular convolution using DFT and IDFT",
)
project_7_page =st.Page(
    page="views/8_dft_properties.py",
    title="Determine Linearity, Circular time shift property & Circular frequency shift property of DFT",
)
project_8_page =st.Page(
    page="views/9_radix2_8pt.py",
    title="Determine 8-point FFT of x(n) using Radix-2 DIT-FFT algorithm",
)
project_9_page =st.Page(
    page="views/10_fir_lp_filter.py",
    title="FIR LPF filter design using Hamming window",
)
project_10_page =st.Page(
    page="views/11_fir_hp_filter.py",
    title="FIR HPF filter design using Hamming window",
)
project_11_page =st.Page(
    page="views/12_iir_lp_filter.py",
    title="IIR LPF filter design using Butterworth filter",
)
project_12_page =st.Page(
    page="views/13_iir_hp_filter.py",
    title="IIR HPF filter design using Butterworth filter",
)
pg = st.navigation(
    {
    "Info":[About_page],
    "Experiments":[project_1_page,project_2_page,project_3_page,project_4_page,project_5_page,project_6_page,project_7_page,project_8_page,project_9_page,project_10_page,project_11_page,project_12_page]
    }
)
current_dir= Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
college_pic = current_dir / "assets" / "college.png"

st.logo("assets/dept.jpeg")
st.markdown("""
     <style>
     .sidebar-text {
        font-size: 16px;
     }
     </style>
 """, unsafe_allow_html=True) 
st.sidebar.markdown("<p class='sidebar-text'>Website Designed by:</p>", unsafe_allow_html=True)
st.sidebar.markdown("<p class='sidebar-text'>Shivaprasad, Dept. of ECE, VCET Puttur</p>", unsafe_allow_html=True)
try:
    st.markdown('Page viewed = {} times.'.format(len(pageviews)))
except ValueError:
    st.markdown('Page viewed = {} times.'.format(1))
pg.run()
