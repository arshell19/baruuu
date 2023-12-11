import pandas as pd
import streamlit as st
import numpy as np
import re 
import csv

st.markdown("<h4 style='text-align: center;'>Arshelia Romadhona | 200411100053</h4>", unsafe_allow_html=True)
tab1, tab2, tab3, tab4 = st.tabs(["Hasil Dataset", "Hasil Pre-Processing", 'Hasil TF-IDF', 'Hasil Modelling'])

with tab1 :
    st.subheader('Dataset hasil crawling')
    st.write(
        '- Crawling <br> <p style = "text-align: justify;"> <b>Crawling</b> dilakukan di website https://www.kompas.com/ dengan 3 kategori yaitu Bola, Health dan Teknologi </p>',
        unsafe_allow_html=True)
    csv_path = 'https://raw.githubusercontent.com/arshell19/app-ppw/main/Kompas.csv'
    df = pd.read_csv(csv_path)
    df


with tab2 :
    st.subheader('Data Pre-Processing')
    st.write(
        '- Cleaning <br> <p style = "text-align: justify;"> <b>Cleaning</b>adalah langkah dalam preprocessing yang fokus pada identifikasi dan penanganan elemen yang tidak diinginkan atau mengganggu dalam dataset. Ini melibatkan deteksi dan penanganan nilai-nilai yang hilang, noise, atau outlier. Proses pembersihan juga dapat mencakup penghapusan atau penggantian nilai-nilai yang tidak valid, penanganan duplikat, dan penanganan masalah lain yang dapat mempengaruhi kualitas data.</p>',
        unsafe_allow_html=True)
    st.write(
        '- Tokenizing <br> <p style = "text-align: justify;"> <b>Tokenizing</b>proses memecah teks atau data teks menjadi unit-unit yang lebih kecil, yang disebut token. Token bisa berupa kata, frasa, atau simbol. Tokenisasi mempermudah analisis teks dan pengolahan bahasa alami, karena memungkinkan sistem untuk memahami dan memanipulasi unit-unit kata atau frasa secara terpisah. Misalnya, dalam kalimat "Saya suka belajar pemrograman," tokenisasi dapat menghasilkan token seperti ["Saya", "suka", "belajar", "pemrograman"].</p>',
        unsafe_allow_html=True)
    st.write(
        '- Stopword <br> <p style = "text-align: justify;"> <b>Stopword</b> kata-kata umum yang sering muncul dalam suatu bahasa dan dianggap kurang informatif atau tidak signifikan dalam konteks analisis teks atau pemodelan bahasa. Contoh stopwords dalam bahasa Inggris adalah "the", "is", "and", "of". Pada langkah preprocessing yang melibatkan teks, biasanya dilakukan penghapusan stopwords untuk mengurangi dimensi dan meningkatkan akurasi analisis. Namun, perlu dicatat bahwa tidak selalu diperlukan di semua kasus, tergantung pada tujuan analisis atau pemodelan tertentu.</p>',
        unsafe_allow_html=True)
    csv_path = 'https://raw.githubusercontent.com/arshell19/app-ppw/main/HasilTokenizeSummary.csv'
    df = pd.read_csv(csv_path)
    df

with tab3 :
    st.subheader('Hasil TF-IDF')
    st.write(
        '- TF-IDF <br> <p style = "text-align: justify;"> <b>TF-IDF</b> adalah suatu metode pengukuran statistik yang digunakan untuk mengevaluasi seberapa penting sebuah kata (term) dalam suatu dokumen dalam koleksi dokumen atau korpus. TF-IDF umumnya digunakan dalam pemrosesan bahasa alami dan pengambilan informasi untuk memberikan bobot pada kata-kata dalam suatu teks.</p>',
        unsafe_allow_html=True)
    csv_path = 'https://raw.githubusercontent.com/arshell19/app-ppw/main/HAsil-TFIDF.csv'
    df = pd.read_csv(csv_path)
    df

with tab4 :
    st.subheader('Hasil Akurasi dari  Metode KNN, Naive Bayes dan Random Forest')
    st.write(
        '- K-NN <br> <p style = "text-align: justify;"> <b>K-NN</b>adalah suatu algoritma pembelajaran mesin yang digunakan untuk klasifikasi dan regresi. Pada dasarnya, KNN bekerja dengan cara mencari k tetangga terdekat dari suatu titik data berdasarkan ukuran jarak (biasanya menggunakan jarak Euclidean). Untuk klasifikasi, suatu titik akan diatributkan ke kelas mayoritas dari tetangga-tetangganya, sementara untuk regresi, nilai rata-rata atau nilai tertimbang dari tetangga-tetangganya dapat digunakan sebagai prediksi nilai.</p>',
        unsafe_allow_html=True)
    st.write(
        '- Naive Bayes <br> <p style = "text-align: justify;"> <b>Naive Bayes</b>adalah algoritma klasifikasi probabilistik berdasarkan Teorema Bayes. Meskipun disebut "naive" karena asumsi dasar yang sederhana (yaitu, independensi antar-fitur), Naive Bayes sering kali memberikan hasil yang baik terutama pada data yang cukup besar. Algoritma ini umumnya digunakan dalam klasifikasi teks dan kategorisasi dokumen.</p>',
        unsafe_allow_html=True)
    st.write(
        '- Random Forest <br> <p style = "text-align: justify;"> <b>Random Forest</b>adalah suatu jenis ensemble learning yang terdiri dari beberapa pohon keputusan. Setiap pohon keputusan dibangun secara acak dengan menggunakan subset acak dari data training dan subset acak dari fitur. Prediksi dari Random Forest dihasilkan dengan mengumpulkan prediksi dari setiap pohon dan memilih hasil mayoritas.</p>',
        unsafe_allow_html=True)
    csv_path = 'https://raw.githubusercontent.com/arshell19/app-ppw/main/hasilakhir.csv'
    df = pd.read_csv(csv_path)
    df