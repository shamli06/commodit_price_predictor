import streamlit as st
import pickle
import numpy as np

# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

reg = pickle.load(open('reg.pkl','rb'))
df_mobile = pickle.load(open('df_mobile.pkl','rb'))

st.title("Commodity Predictor")

commodity = st.selectbox('Commodity',['Laptop','Mobile'])
if commodity == 'Laptop':
    # brand
    company = st.selectbox('Brand',df['Company'].unique())

    # type of laptop
    type = st.selectbox('Type',df['TypeName'].unique())

    # Ram
    ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

    # weight
    weight = st.number_input('Weight of the Laptop')

    # Touchscreen
    touchscreen = st.selectbox('TouchScreen',['No','Yes'])

    # IPS
    ips = st.selectbox('IPS',['No','Yes'])

    # screen size
    screen_size = st.number_input('Screen Size')

    # resolution
    resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

    #cpu
    cpu = st.selectbox('CPU',df['Cpu brand'].unique())

    hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

    ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

    gpu = st.selectbox('GPU',df['Gpu_brand'].unique())

    os = st.selectbox('OS',df['os'].unique())
else:
    #company = st.selectbox('Brand', df['Brand me'].unique())

    # type of laptop
    #ratings = st.number_input("Ratings")

    # Ram
    ram = st.selectbox('RAM(in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])

    # Rom
    rom = st.selectbox('ROM(in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64,128,256])

    # size
    mobile_size = st.number_input('Size of the Mobile')

    # primary_cam
    primary_cam = st.selectbox('Primary Camera', [8, 20, 48, 50,64])

    # selfi_cam
    selfi_cam = st.selectbox('Selfi Camera', [1,2,4,5,8,9,12,13,15,16,20,64])

    # battery power
    battery_power = st.selectbox('Battery Power', [1050,2500,2800,3000,3500,3800,4000,5000,6000])

if st.button('Predict Price'):
    if(commodity == 'Laptop'):
        # query
        ppi = None
        if touchscreen == 'Yes':
            touchscreen = 1
        else:
            touchscreen = 0

        if ips == 'Yes':
            ips = 1
        else:
            ips = 0

        X_res = int(resolution.split('x')[0])
        Y_res = int(resolution.split('x')[1])
        ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
        query = np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])

        query = query.reshape(1,12)
        st.title("The predicted price of this configuration is " + str(int(np.exp(pipe.predict(query)[0]))))
    else:
        query = np.array([[0,ram,rom,mobile_size,primary_cam,selfi_cam,battery_power]])
        st.title("The predicted price of this configuration is " + str(int(np.exp(reg.predict(query)[0]))))