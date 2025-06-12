import streamlit as st
import pickle
import numpy as np
from catboost import CatBoostClassifier

st.set_page_config(
    page_title="Student Dropout Prediction",
    page_icon="👨‍🎓"
)

def load_model():
    with open('models/catboost_best_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model


model = load_model()

def show_predict():
    st.title('👨‍🎓 Student Dropout Prediction')

    # with st.form("user_input"):
    with st.container(border=True):
        st.info('📢 Untuk keperluan demo, nilai inputan digenerate secara random jika tidak diisi. Tujuannya supaya memudahkan jika ingin mencoba-coba sistem prediksi ini.')

        # st.session_state

        if "rand_init" not in st.session_state:
            st.session_state.rand_marital_status = np.random.randint(0, 6)
            st.session_state.rand_age = np.random.randint(18, 40)
            st.session_state.rand_gender = np.random.randint(0, 2)
            st.session_state.rand_scholarship = np.random.randint(0, 2)
            st.session_state.rand_tuition = np.random.randint(0, 2)
            st.session_state.rand_course = np.random.randint(0, 17)
            st.session_state.rand_approved1 = np.random.randint(0, 26)
            st.session_state.rand_grade1 = np.random.uniform(0, 18)
            st.session_state.rand_approved2 = np.random.randint(0, 26)
            st.session_state.rand_grade2 = np.random.uniform(5, 18)
            st.session_state.rand_init = True

        # st.session_state

        # generate = st.button('🔄 Try Another Random Data')

        # if generate:
        #     random_marital_status = np.random.randint(0, 6)
        #     st.session_state.rand_marital_status = random_marital_status
        #     random_age = np.random.randint(18, 40)
        #     st.session_state.rand_age = random_age
        #     random_gender = np.random.randint(0, 2)
        #     st.session_state.rand_gender = random_gender
        #     random_scholarship = np.random.randint(0, 2)
        #     st.session_state.rand_scholarship = random_scholarship
        #     random_tuition = np.random.randint(0, 2)
        #     st.session_state.rand_tuition = random_tuition
        #     random_course = np.random.randint(0, 17)
        #     st.session_state.rand_course = random_course
        #     random_approved1 = np.random.randint(0, 26)
        #     st.session_state.rand_approved1 = random_approved1
        #     random_grade1 = np.random.uniform(0, 18)
        #     st.session_state.rand_grade1 = random_grade1
        #     random_approved2 = np.random.randint(0, 26)
        #     st.session_state.rand_approved2 = random_approved2
        #     random_grade2 = np.random.uniform(5, 18)
        #     st.session_state.rand_grade2 = random_grade2

        # rand_marital_status = np.random.randint(0, 6)
        marital_status = st.selectbox('Apa status pernikahan Anda?', ('Single', 'Married', 'Widower', 'Divorced', 'Facto Union', 'Legally Separated'), index=st.session_state.rand_marital_status, help='Pilih status pernikahan Anda')
        if marital_status == 'Single':
            marital_status = 1
        elif marital_status == 'Married':
            marital_status = 2
        elif marital_status == 'Widower':
            marital_status = 3
        elif marital_status == 'Divorced':
            marital_status = 4
        elif marital_status == 'Facto Union':
            marital_status = 5
        elif marital_status == 'Legally Separated':
            marital_status = 6

        # rand_age = np.random.randint(18, 40)
        age = st.select_slider('Berapa umur Anda?', options=[i for i in range(14, 70)], value=st.session_state.rand_age, help='Pilih usia Anda')

        # rand_gender = np.random.randint(0, 2)
        gender = st.selectbox('Apa jenis kelamin Anda?', ('Laki-laki', 'Perempuan'), index=st.session_state.rand_gender, help='Pilih jenis kelamin Anda')
        if gender == 'Perempuan':
            gender = 0
        elif gender == 'Laki-laki':
            gender = 1

        # rand_scholarship = np.random.randint(0, 2)
        scholarship = st.selectbox('Apakah Anda pemegang beasiswa?', ('Tidak', 'Iya'), index=st.session_state.rand_scholarship, help='Apakah Anda penerima beasiswa?')
        if scholarship == 'Tidak':
            scholarship = 0
        elif scholarship == 'Iya':
            scholarship = 1

        # rand_tuition = np.random.randint(0, 1)
        tuition = st.selectbox('Apakah Anda terlambat atau menunggak membayar uang kuliah?', ('Tidak', 'Iya'), index=st.session_state.rand_tuition, help='Apakah Anda terlambat atau menunggak membayar uang kuliah?')
        if tuition == 'Iya':
            tuition = 0
        elif tuition == 'Tidak':
            tuition = 1

        # rand_course = np.random.randint(0, 17)
        course = st.selectbox('Apa kode program studi Anda?', (33, 171, 8014, 9003, 9070, 9085, 9119, 9130, 9147, 9238, 9254, 9500, 9556, 9670, 9773, 9853, 9991), index=st.session_state.rand_course, help='Pilih kode program studi Anda')

        # rand_approved1 = np.random.randint(0, 26)
        approved1 = st.number_input('Jumlah SKS pada semester 1', value=st.session_state.rand_approved1, help='Rentang SKS dari 0 sampai 26.')

        # rand_grade1 = np.random.uniform(0, 18)
        grade1 = st.number_input('Rata-rata nilai pada semester 1', value=st.session_state.rand_grade1, help='Nilai memiliki rentang dari 0 sampai 20.')

        # rand_approved2 = np.random.randint(0, 26)
        approved2 = st.number_input('Jumlah SKS pada semester 2', value=st.session_state.rand_approved2, help='Rentang SKS dari 0 sampai 26.')

        # rand_grade2 = np.random.uniform(0, 18)
        # st.session_state.input_data['grade2'] = rand_grade2
        grade2 = st.number_input('Rata-rata nilai pada semester 2', value=st.session_state.rand_grade2, help='Nilai memiliki rentang dari 0 sampai 20.')

        col1, col2 = st.columns([0.135,0.7])

        with col1:
            ok = st.button("🔍 Predict")
        
        with col2:
            if st.button('🔄 Generate Another Random Data'):
                st.session_state.clear()
                st.experimental_rerun()

        if ok:
            X = np.array([[approved1, grade1, approved2, grade2, tuition, course, age, scholarship, gender, marital_status]])
            pred = model.predict(X)
            # st.write(approved2)
            # st.write(grade2)
            if pred == "Dropout":
                font_color = 'red'
                st.markdown(f"<h3>Siswa akan <span style='color: {font_color}'>dropout</span></h3>", unsafe_allow_html=True)
            if pred == "Graduate":
                font_color = 'green'
                st.markdown(f"<h3>Siswa akan <span style='color: {font_color}'>lulus</span></h3>", unsafe_allow_html=True)
            
            st.info('📢 Silakan klik tombol "Generate Another Random Data" untuk mencoba variasi inputan lainnya.')



show_predict()