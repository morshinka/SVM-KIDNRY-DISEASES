import streamlit as st
from web_function import predict

def app(df, x, y):
    st.title("Klasifikasi Kanker Ginjal")
    
    col1,col2,col3,col4 = st.columns(4)
    
    with col1:
        bp = st.text_input("Blood Pressure")
        sg = st.text_input("Specific Gravity")
        al = st.text_input("Albumin")
        su = st.text_input("Sugar")
        rbc = st.text_input("Red Blood Cells")
        pc = st.text_input("Pus Cells")
    with col2:
        pcc = st.text_input("Pus Cell Clumps")
        ba = st.text_input("Bacteria")
        bgr = st.text_input("Blood Glucose Random")
        bu = st.text_input("Blood Urea")
        sc = st.text_input("Serum Creatinine")
        sod = st.text_input("Sodium")
    with col3:
        pot = st.text_input("Potassium")
        hemo = st.text_input("Hemoglobin")
        pcv = st.text_input("Packed Cell Volume")
        wc = st.text_input("White Blood Cell Count")
        rc = st.text_input("Red Blood Cell Count")
        htn = st.text_input("Hypertension")
    with col4:
        dm = st.text_input("Diabetes Mellitus")
        cad = st.text_input("Coronary Artery Disease")
        appet = st.text_input("Appetite")
        pe = st.text_input("Pedal Edema")
        ane = st.text_input("Anemia")
    features = [bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc,sod,pot,hemo,pcv,wc,rc,htn,dm,cad,appet,pe,ane]
    
    if st.button("Prediksi"):
        if '' in features:
            st.error("Anda Belum Memasukkan Data Yang Dibutuhkan")
        else:
            prediction, score = predict(x, y, features)
            score = score
            st.info("Prediski Berhasil")
            if (prediction[0] == 1):
                st.warning('Anda Rentan Terkena Batu Ginjal')
            else:
                st.success('Anda Relativ Aman ')
            st.write("Model Yang Digunakan Memiliki Akurasi : ", score*100 ,"%")