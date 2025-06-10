import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np

st.set_page_config(
    page_title="Models Information",
    page_icon="🖥️"
)

def show_model_information_page():

    st.title('🖥️ Models Information')
    st.write("##### 🔍 Goals:")
    st.write('- Modeling from **scratch** without ML Library')
    st.write('- Data Augmentation using GAN')
    st.write('- Feature Selection using ANOVA')
    st.write('- Deploy Best Model into Web App')

    st.write("#### 💻 Models from Scratch:")
    st.write('- Logistic Regression')
    st.write('- Naive Bayes')
    st.write('- Perceptron')
    st.write('- SVM')

    st.write('#### 💻 Model from ML Library:')
    st.write('- CatBoost Classifier (digunakan pada web app ini)')

    st.write('#### 📈 Komparasi Akurasi Model Sebelum & Setelah GAN + Feature Selection')

    nama_model = ['Logistic Regression', 'Naive Bayes', 'Perceptron', 'SVM', 'CatBoost']
    nama_model2 = ['Logistic Regression', 'Naive Bayes', 'Perceptron', 'SVM']
    avg_train_arr = [0.8613636363636363, 0.8424242424242424, 0.8761019283746556, 0.9137741046831955, 0.9387052341597796]
    avg_test_arr = [0.8578512396694216, 0.8415977961432507, 0.8785123966942148, 0.9082644628099172, 0.9173553719008265]
    avg_train_arr_after = [0.8631749460043195, 0.8447084233261339, 0.8669006479481641, 0.9130129589632829]
    avg_test_arr_after = [0.8602591792656588, 0.8401727861771058, 0.8615550755939525, 0.906047516198704]

    fig, ax = plt.subplots(2, figsize=(11, 12))

    # Lebar setiap bar
    bar_width = 0.3

    # Array untuk sumbu X
    x_pos1 = np.arange(len(nama_model))

    # Plot untuk train
    train_bars1 = ax[0].bar(x_pos1, avg_train_arr, width=bar_width, align='center', alpha=0.8, label='Train Accuracy')

    # Plot untuk test
    test_bars1 = ax[0].bar(x_pos1 + bar_width, avg_test_arr, width=bar_width, align='center', alpha=0.8, label='Test Accuracy')

    ax[0].set_xticks(x_pos1 + bar_width / 2)
    ax[0].set_xticklabels(nama_model)

    ax[0].set_ylabel('Accuracy')

    ax[0].set_title('Model Accuracy Comparison Without GAN + Without Feature Selection')

    # Untuk annotation
    for bar1, bar2 in zip(train_bars1, test_bars1):
        height1 = bar1.get_height()
        height2 = bar2.get_height()
        ax[0].annotate(f'{height1:.3f}', xy=(bar1.get_x() + bar1.get_width() / 2, height1),
                    xytext=(0, 3), textcoords='offset points', ha='center', va='bottom')
        ax[0].annotate(f'{height2:.3f}', xy=(bar2.get_x() + bar2.get_width() / 2, height2),
                    xytext=(0, 3), textcoords='offset points', ha='center', va='bottom')

    ax[0].set_ylim(0, 1)  

    ax[0].legend(loc='center left', bbox_to_anchor=(1, 0.5))

    # Untuk plot kedua

    x_pos2 = np.arange(len(nama_model2))

    train_bars2 = ax[1].bar(x_pos2, avg_train_arr_after, width=bar_width, align='center', alpha=0.8, label='Train Accuracy')

    test_bars2 = ax[1].bar(x_pos2 + bar_width, avg_test_arr_after, width=bar_width, align='center', alpha=0.8, label='Test Accuracy')

    ax[1].set_xticks(x_pos2 + bar_width / 2)
    ax[1].set_xticklabels(nama_model2)

    ax[1].set_ylabel('Accuracy')

    ax[1].set_title('Model Accuracy Comparison with GAN + Feature Selection')

    for bar1, bar2 in zip(train_bars2, test_bars2):
        height1 = bar1.get_height()
        height2 = bar2.get_height()
        ax[1].annotate(f'{height1:.3f}', xy=(bar1.get_x() + bar1.get_width() / 2, height1),
                    xytext=(0, 3), textcoords='offset points', ha='center', va='bottom')
        ax[1].annotate(f'{height2:.3f}', xy=(bar2.get_x() + bar2.get_width() / 2, height2),
                    xytext=(0, 3), textcoords='offset points', ha='center', va='bottom')

    ax[1].set_ylim(0, 1) 

    ax[1].legend(loc='center left', bbox_to_anchor=(1, 0.5))

    st.pyplot(fig)

    st.caption('Note: Catboost tidak diikutsertakan ketika memanfaatkan GAN + Feature Selection karena keterbatasan waktu dan sumber daya.')
    st.write('### 🔍 Analisis:')
    st.write('- Tampak tidak ada overfitting dan tidak ada underfitting pada semua model yang dibuat. Hal ini dapat dilihat dari nilai akurasi yang tidak terlalu jauh antara train dan test. Selain itu, nilai akurasi yang didapat juga cukup tinggi, yaitu di atas 84%.')
    st.write('- Tampak tidak ada perubahan mencolok antara sebelum dan sesudah menggunakan GAN + Feature Selection. Hal tersebut karena jumlah data yang sudah mencukupi dan semua feature memiliki peran yang penting. ')
    st.write('- Jika semua feature memiliki peran penting, maka feature selection justru dapat membuat akurasi menurun karena model kehilangan informasi penting dari feature-feature yang dihilangkan tersebut.')
    st.write('- Catboost menghasilkan akurasi tertinggi, yaitu 91.7% pada data test. Hal tersebut karena catboost bisa mengombinasikan berbagai decision tree dan memperbaiki kesalahan prediksi dari pohon sebelumnya. Catboost juga menerapkan ordered boosting untuk menghindari kebocoran data selama pelatihan. Dengan ordered boosting, Catboost dapat menghindari informasi masa depan saat membuat decision tree sehingga hanya data sebelumnya yang digunakan untuk menghitung residual bagi sebuah instance. Hal tersebut juga dapat mengurangi overfitting. Berdasarkan alasan tersebut, saya menggunakan model Catboost pada web app ini.')


show_model_information_page()