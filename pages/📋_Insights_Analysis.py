import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(
    page_title="Student Insights Analysis",
    page_icon="📋"
)

@st.cache_data
def load_data():
    # Menampilkan data
    df = pd.read_csv('data.csv', sep=';')
    df.drop(df[df['Target'] == 'Enrolled'].index, inplace = True)

    return df

df = load_data()

def show_insight():
    st.title('📋 Student Insights Analysis')

    st.markdown("### **1. Bagaimana distribusi mahasiswa yang lulus dan dropout?**")

    col1, col2 = st.columns([0.6, 0.4])
    with col1:
        target_counts = df['Target'].value_counts()
        plt.figure(figsize = (5,5))
        colors = ['#CD2E2E', '#4A84B1']
        patches, texts, autotexts = plt.pie(
            target_counts,
            labels=target_counts.index,
            autopct='%1.1f%%',
            colors=colors
        )

        # Set white color for annotation text
        for autotext in autotexts:
            autotext.set_color('black')
        plt.title('Distribusi Mahasiswa Lulus dan Dropout')
        st.pyplot(plt)
    
    with st.expander("📋 Analisis Visualisasi", expanded=True):
        st.info('Tampak bahwa distribusi antara mahasiswa yang lulus dan dropout pada data ini cenderung balance.')
        st.info('Dengan demikian, pola dan hasil analisis selanjutnya dapat lebih representatif.')

    
    st.markdown('### **2. Apakah mahasiswa yang menggunakan beasiswa memiliki proporsi kelulusan yang lebih tinggi?**')
    plt.figure(figsize = (10,6))
    ax = sns.countplot(data = df, x = 'Scholarship holder', hue = 'Target', palette='Set1')
    plt.xlabel('Status Beasiswa')
    plt.ylabel('Jumlah Mahasiswa')
    plt.legend(title='Status Kelulusan')
    scholarship_labels = {
        0: "Tidak",
        1: "Iya",
    }
    plt.xticks(ticks=list(scholarship_labels.keys()), labels=list(scholarship_labels.values()))

    # Untuk menampilkan nilai detail di atas bar
    for i in ax.containers:
        ax.bar_label(i,)

    plt.title('Kelulusan Siswa Berdasarkan Status Beasiswa')
    st.pyplot(plt)

    with st.expander("📋 Analisis Visualisasi", expanded=True):
        st.info('Tampak perbedaan yang cukup mencolok antara mahasiswa yang menggunakan beasiswa dengan yang tidak. Lebih dari 85% mahasiswa penerima beasiswa berhasil lulus dan hanya sangat sedikit yang dropout. Sementara itu, mahasiswa yang tidak menggunakan beasiswa memiliki proporsi lulus dan dropout yang hampir seimbang.')

        st.info('Hal tersebut dapat disebabkan karena mahasiswa penerima beasiswa dapat merasa berutang budi kepada pemberi beasiswa dan ingin membuktikan bahwa mereka layak menerima bantuan tersebut sehingga mereka lebih termotivasi untuk menyelesaikan studi dengan baik. Artinya, mahasiswa penerima beasiswa dapat merasa lebih bertanggung jawab untuk menyelesaikan studi mereka.')


    
    st.markdown("### **3. Bagaimana distribusi kelulusan berdasarkan status perkawinan?**")
    plt.figure(figsize = (10,6))
    ax = sns.countplot(data = df, x = 'Marital status', hue = 'Target', palette='Set1')
    plt.xlabel('Status Perkawinan')
    plt.ylabel('Jumlah Mahasiswa')
    plt.legend(title='Status Kelulusan')
    marital_labels = {
        0: "Single",
        1: "Married",
        2: "Widower",
        3: "Divorced",
        4: "Facto Union",
        5: "Legally Separated",
        6: ""
    }
    plt.xticks(ticks=list(marital_labels.keys()), labels=list(marital_labels.values()))

    # Untuk menampilkan nilai detail di atas bar
    for i in ax.containers:
        ax.bar_label(i,)

    plt.title('Kelulusan Siswa Berdasarkan Status Perkawinan')
    st.pyplot(plt)

    with st.expander("📋 Analisis Visualisasi", expanded=True):
        st.info('Tampak bahwa ada perbedaan proporsi status kelulusan antara mahasiswa yang masih lajang dengan mahasiswa yang sudah pernah menikah. Mahasiswa yang masih lajang memiliki proporsi kelulusan yang lebih tinggi, sedangkan mahasiswa yang sudah menikah justru memiliki proporsi dropout yang lebih tinggi.')
        st.info('Hal tersebut dapat disebabkan karena mahasiswa yang sudah menikah memiliki tanggung jawab tambahan, seperti keluarga dan pekerjaan sehingga dapat memengaruhi fokus dan waktu yang tersedia untuk studi mereka. Mahasiswa yang masih lajang cenderung dapat lebih fokus pada studi mereka tanpa adanya tanggung jawab tambahan tersebut.')


    
    st.markdown("### **4. Bagaimana distribusi nilai mahasiswa di semester 1 dan 2?**")
    plt.figure(figsize=(14, 6))

    # Histogram Semester 1
    plt.subplot(1, 2, 1)
    sns.histplot(df['Curricular units 1st sem (grade)'], bins=30, kde=True, color='blue')
    plt.title("Distribusi Nilai Mahasiswa Semester 1")
    plt.xlabel("Nilai Rata-rata Semester 1")
    plt.ylabel("Jumlah Mahasiswa")

    # Histogram Semester 2
    plt.subplot(1, 2, 2)
    sns.histplot(df['Curricular units 2nd sem (grade)'], bins=30, kde=True, color='orange')
    plt.title("Distribusi Nilai Mahasiswa Semester 2")
    plt.xlabel("Nilai Rata-rata Semester 2")
    plt.ylabel("Jumlah Mahasiswa")

    plt.tight_layout()
    st.pyplot(plt)

    with st.expander("📋 Analisis Visualisasi", expanded=True):
        st.info('Tampak bahwa distribusi nilai mahasiswa di semester 1 dan 2 cenderung mirip. Namun, mahasiswa yang memiliki nilai 0 cenderung lebih banyak di semester 2. Artinya, terdapat peningkatan jumlah mahasiswa yang memiliki nilai 0.')

        st.info('Maka, mahasiswa yang memiliki nilai 0 di semester 1 sudah harus mendapatkan perhatian khusus agar jumlahnya tidak bertambah di semester 2. Salah satu cara yang dapat dilakukan adalah dengan memberikan bimbingan akademik atau konseling kepada mahasiswa tersebut untuk membantu mereka mengatasi kesulitan yang mungkin mereka hadapi.')

    st.markdown("### **5. Bagaimana distribusi kelulusan mahasiswa berdasarkan nilai mahasiswa?**")
    plt.figure(figsize = (14,6))
    plt.subplot(1, 2, 1)
    ax = sns.boxplot(data = df, x = 'Target', y = 'Curricular units 1st sem (grade)', palette='Set1')
    plt.xlabel('Status Kelulusan')
    plt.ylabel('Nilai Rata-rata Semester 1')
    plt.title('Nilai Rata-rata Semester 1 Berdasarkan Status Kelulusan')
    plt.xticks(ticks=[0, 1], labels=['Dropout', 'Graduate'])

    plt.subplot(1, 2, 2)
    ax = sns.boxplot(data = df, x = 'Target', y = 'Curricular units 2nd sem (grade)', palette='Set1')
    plt.xlabel('Status Kelulusan')
    plt.ylabel('Nilai Rata-rata Semester 2')
    plt.title('Nilai Rata-rata Semester 2 Berdasarkan Status Kelulusan')
    plt.xticks(ticks=[0, 1], labels=['Dropout', 'Graduate'])

    # plt.grid(axis='y')
    st.pyplot(plt)

    with st.expander("📋 Analisis Visualisasi", expanded=True):
        st.info('Tampak terdapat perbedaan yang sangat mencolok antara distribusi nilai mahasiswa yang lulus dan dropout. Distribusi nilai mahasiswa yang lulus berkisar antara 12 hingga 15, sementara distribusi nilai mahasiswa yang dropout sangat lebar di bawah 12. Hal tersebut menunjukkan bahwa performa akademik mahasiswa sangat berpengaruh terhadap status kelulusan mereka.')

        st.info('Namun, terdapat outlier pada mahasiswa yang dropout dengan nilai di atas 17. Hal ini menunjukkan bahwa dropout tidak selalu disebabkan karena nilai yang rendah, tetapi bisa juga disebabkan oleh faktor eksternal lainnya.')

    st.markdown("### **6. Bagaimana distribusi kelulusan mahasiswa berdasarkan umur mahasiswa?**")
    bins = [10, 20, 30, 40, 50, 60, 70]
    labels = ['11-20', '21-30', '31-40', '41-50', '51-60', '61-70']
    df['Age'] = pd.cut(df['Age at enrollment'], bins=bins, labels=labels, right=False)
    plt.figure(figsize = (10,6))
    ax = sns.countplot(data = df, x = 'Age', hue = 'Target', palette='Set1')
    plt.xlabel('Usia Mahasiswa')
    plt.ylabel('Jumlah Mahasiswa')
    plt.legend(title='Status Kelulusan')

    # Untuk menampilkan nilai detail di atas bar
    for i in ax.containers:
        ax.bar_label(i,)

    plt.title('Kelulusan Siswa Berdasarkan Usia')
    st.pyplot(plt)

    with st.expander("📋 Analisis Visualisasi", expanded=True):
        st.info('Tampak pola yang menarik pada distribusi usia mahasiswa. Mahasiswa yang berusia di bawah 30 tahun memiliki proporsi kelulusan yang lebih tinggi dibandingkan mahasiswa yang dropout. Sementara itu, mahasiswa yang berusia di atas 30 tahun justru memiliki proporsi dropout yang lebih tinggi dibandingkan yang berhasil lulus.')
        
        st.info('Hal tersebut dapat disebabkan karena mahasiswa yang berusia di atas 30 tahun kemungkinan sudah memiliki banyak kesibukan dan tanggung jawab sehingga dapat mengganggu fokus mereka terhadap studi. Kemampuan bersaing kognitif juga dapat menurun seiring bertambahnya usia sehingga mahasiswa yang lebih tua mungkin mengalami kesulitan dalam mengikuti materi kuliah yang semakin kompleks.')


    st.markdown("### **7. Bagaimana distribusi kelulusan mahasiswa berdasarkan status pembayaran uang kuliah?**")
    plt.figure(figsize = (10,6))
    palette_inverse = sns.color_palette("Set1", n_colors=2)[::-1]  # Membalikkan palet warna
    ax = sns.countplot(data = df, x = 'Tuition fees up to date', hue = 'Target', palette=palette_inverse)
    plt.xlabel('Status Pembayaran Uang Kuliah')
    plt.ylabel('Jumlah Mahasiswa')
    plt.legend(title='Status Kelulusan')
    tuition_labels = {
        0: "Terlambat",
        1: "Tepat Waktu",
    }
    plt.xticks(ticks=list(tuition_labels.keys()), labels=list(tuition_labels.values()))

    # Untuk menampilkan nilai detail di atas bar
    for i in ax.containers:
        ax.bar_label(i,)

    plt.title('Kelulusan Siswa Berdasarkan Status Pembayaran Uang Kuliah')
    st.pyplot(plt)

    with st.expander("📋 Analisis Visualisasi", expanded=True):
        st.info('Tampak perbedaan yang sangat mencolok antara mahasiswa yang membayar uang kuliah terlambat dengan yang tepat waktu. Lebih dari 90% mahasiswa yang terlambat membayar uang kuliah mengalami dropout, sementara mahasiswa yang membayar tepat waktu memiliki proporsi kelulusan yang lebih tinggi.')

        st.info('Hal tersebut menunjukkan bahwa dropout bisa terjadi karena masalah keuangan. Mahasiswa yang terlambat membayar uang kuliah mungkin mengalami kesulitan keuangan yang dapat memengaruhi fokus mereka dalam menyelesaikan studi. Namun, hal ini juga menunjukkan bahwa terlambat membayar uang kuliah menjadi penyebab mahasiswa tersebut mendapatkan hukuman dropout.')


    st.markdown("### **8. Bagaimana distribusi kelulusan mahasiswa berdasarkan jumlah SKS yang diambil?**")
    plt.figure(figsize = (14,6))
    plt.subplot(1, 2, 1)
    ax = sns.boxplot(data = df, x = 'Target', y = 'Curricular units 1st sem (enrolled)', palette='Set1')
    plt.xlabel('Status Kelulusan')
    plt.ylabel('Jumlah SKS Semester 1')
    plt.title('Jumlah SKS Semester 1 Berdasarkan Status Kelulusan')
    plt.xticks(ticks=[0, 1], labels=['Dropout', 'Graduate'])

    plt.subplot(1, 2, 2)
    ax = sns.boxplot(data = df, x = 'Target', y = 'Curricular units 2nd sem (enrolled)', palette='Set1')
    plt.xlabel('Status Kelulusan')
    plt.ylabel('Jumlah SKS Semester 2')
    plt.title('Jumlah SKS Semester 2 Berdasarkan Status Kelulusan')
    plt.xticks(ticks=[0, 1], labels=['Dropout', 'Graduate'])

    # plt.grid(axis='y')
    st.pyplot(plt)

    with st.expander("📋 Analisis Visualisasi", expanded=True):
        st.info('Tampak bahwa mahasiswa yang lulus cenderung mengambil lebih banyak SKS dibandingkan mahasiswa yang dropout. Hal tersebut dapat menunjukkan bahwa mahasiswa yang lulus memiliki komitmen yang lebih tinggi terhadap studi mereka dan mampu mengelola waktu dengan baik untuk menyelesaikan banyaknya SKS tersebut.')

        st.info('Namun, terdapat outlier pada mahasiswa yang dropout dengan jumlah SKS yang juga banyak. Hal ini menunjukkan bahwa dropout tidak selalu berhubungan dengan jumlah SKS yang diambil, tetapi bisa juga disebabkan oleh faktor lainnya, seperti tidak mampu mengelola waktu dengan baik karena mengambil terlalu banyak SKS.')
        


    st.markdown("### **9. Bagaimana distribusi kelulusan mahasiswa berdasarkan gender?**")
    plt.figure(figsize = (10,6))
    palette_inverse = sns.color_palette("Set1", n_colors=2)[::-1]  # Membalikkan palet warna
    ax = sns.countplot(data = df, x = 'Gender', hue = 'Target', palette=palette_inverse)
    plt.xlabel('Status Pembayaran Uang Kuliah')
    plt.ylabel('Jumlah Mahasiswa')
    plt.legend(title='Status Kelulusan')
    gender_labels = {
        0: "Perempuan",
        1: "Laki-laki",
    }
    plt.xticks(ticks=list(gender_labels.keys()), labels=list(gender_labels.values()))

    # Untuk menampilkan nilai detail di atas bar
    for i in ax.containers:
        ax.bar_label(i,)

    plt.title('Kelulusan Siswa Berdasarkan Gender')
    st.pyplot(plt)

    with st.expander("📋 Analisis Visualisasi", expanded=True):
        st.info('Tampak terdapat perbedaan proporsi status kelulusan berdasarkan gendernya. Mahasiswa perempuan memiliki proporsi kelulusan yang jauh lebih tinggi dibandingkan yang tidak lulus. Sementara itu, mahasiswa laki-laki justru memiliki proporsi dropout yang lebih tinggi dibandingkan yang lulus.')

        st.info("Hal tersebut menunjukkan bahwa dibutuhkan evaluasi lebih lanjut untuk memahami faktor-faktor yang menyebabkan proporsi kelulusan mahasiswa laki-laki yang jauh lebih rendah dibandingkan mahasiswa perempuan. Masalah ini perlu segera diselesaikan karena lebih banyak mahasiswa laki-laki yang dropout dibandingkan yang lulus.")



    st.markdown("### **10. Bagaimana distribusi kelulusan berdasarkan program studi?**")
    plt.figure(figsize = (10,6))
    # palette_inverse = sns.color_palette("Set1", n_colors=2)[::-1]  # Membalikkan palet warna
    ax = sns.countplot(data = df, x = 'Course', hue = 'Target', palette="Set1")
    plt.xlabel('Kode Program Studi')
    plt.ylabel('Jumlah Mahasiswa')
    plt.legend(title='Status Kelulusan')

    # Untuk menampilkan nilai detail di atas bar
    for i in ax.containers:
        ax.bar_label(i,)

    plt.title('Kelulusan Siswa Berdasarkan Program Studi')
    st.pyplot(plt)

    with st.expander("📋 Analisis Visualisasi", expanded=True):
        st.info("Program studi dengan kode 33, 9119, 9130, 9853, dan 9991 perlu dievaluasi lebih lanjut karena proporsi mahasiswa yang dropout jauh lebih tinggi dibandingkan yang lulus. Hal ini menunjukkan bahwa ada masalah yang perlu segera diselesaikan agar mahasiswa di program studi tersebut dapat lulus dengan baik.")

        st.info("Program studi tersebut juga dapat mempelajari strategi dari program studi 9238 dan 9500 karena proporsi mahasiswa yang lulus di program studi tersebut jauh lebih tinggi dibandingkan yang dropout. Hal ini menunjukkan bahwa program studi kemungkinan memiliki sistem pembelajaran yang lebih efektif dan dapat menjadi contoh bagi program studi lainnya.")

    st.markdown('### **11. Bagaimana distribusi nilai mahasiswa berdasarkan status beasiswa?**')
    plt.figure(figsize = (14,6))
    plt.subplot(1, 2, 1)
    ax = sns.boxplot(data = df, x = 'Scholarship holder', y = 'Curricular units 1st sem (grade)', palette='Set1')
    plt.xlabel('Status Beasiswa')
    plt.ylabel('Nilai Rata-rata Semester 1')
    plt.title('Nilai Rata-rata Semester 1 Berdasarkan Status Beasiswa')
    plt.xticks(ticks=[0, 1], labels=['Tanpa Beasiswa', 'Dengan Beasiswa'])

    plt.subplot(1, 2, 2)
    ax = sns.boxplot(data = df, x = 'Scholarship holder', y = 'Curricular units 2nd sem (grade)', palette='Set1')
    plt.xlabel('Status Beasiswa')
    plt.ylabel('Nilai Rata-rata Semester 2')
    plt.title('Nilai Rata-rata Semester 2 Berdasarkan Status Beasiswa')
    plt.xticks(ticks=[0, 1], labels=['Tanpa Beasiswa', 'Dengan Beasiswa'])  

    # plt.grid(axis='y')
    st.pyplot(plt)

    with st.expander("📋 Analisis Visualisasi", expanded=True):
        st.info('Tampak bahwa mahasiswa yang menerima beasiswa cenderung memiliki nilai yang lebih tinggi dibandingkan mahasiswa yang tidak menerima beasiswa. Hal ini menunjukkan bahwa mahasiswa yang menerima beasiswa mungkin lebih termotivasi untuk belajar dan berprestasi karena mereka merasa berutang budi kepada pemberi beasiswa.')

        st.info('Hal ini juga menunjukkan bahwa hanya siswa dengan nilai tinggi yang eligible untuk mendapatkan beasiswa.')

        st.info('Tampak bahwa nilai mahasiswa yang tidak menerima beasiswa menjadi sangat bervariasi di semester 2. Hal tersebut bisa menjadi indikator bahwa banyak mahasiswa yang kehilangan motivasi belajar karena tidak berhasil mendapatkan beasiswa.')


    st.markdown("### **12. Bagaimana rata-rata nilai mahasiswa berdasarkan usianya?**")

    age_grade_avg = df.groupby('Age at enrollment')[['Curricular units 1st sem (grade)', 'Curricular units 2nd sem (grade)']].mean().reset_index()

    # Plot the line graph
    plt.figure(figsize=(12, 6))
    sns.lineplot(
        data=age_grade_avg,
        x='Age at enrollment',
        y='Curricular units 1st sem (grade)',
        label='Semester 1'
    )
    sns.lineplot(
        data=age_grade_avg,
        x='Age at enrollment',
        y='Curricular units 2nd sem (grade)',
        label='Semester 2'
    )
    plt.title("Rata-rata Nilai Mahasiswa Berdasarkan Usia Saat Mendaftar")
    plt.xlabel("Usia Saat Mendaftar")
    plt.ylabel("Rata-rata Nilai")
    plt.legend(title="Semester")
    plt.tight_layout()

    st.pyplot(plt)

    with st.expander("📋 Analisis Visualisasi", expanded=True):
        st.info('Tampak bahwa mahasiswa yang masih muda atau baru saja lulus SMA cenderung memiliki rata-rata nilai yang lebih tinggi dibandingkan mahasiswa yang lebih tua.')
        st.info('Hal ini menunjukkan bahwa mahasiswa yang lebih muda mungkin lebih mudah beradaptasi dengan sistem pembelajaran di perguruan tinggi dan memiliki semangat belajar yang lebih tinggi. Sementara itu, mahasiswa yang lebih tua dapat sulit beradaptasi dengan sistem perguruan tinggi jaman sekarang, terutama jika mahasiswa tersebut sudah lama tidak merasakan kehidupan di dunia akademis.')
        st.info('Rata-rata nilai mahasiswa yang berusia di atas 50 tahun cenderung fluktuatif karena jumlah mahasiswa yang berusia di atas 50 tahun sangat sedikit sehingga perbedaan nilai satu mahasiswa dapat menyebabkan perubahan yang mencolok.')
        st.info('Tampak pula bahwa rata-rata nilai mahasiswa di semester 2 cenderung lebih rendah dibandingkan semester 1. Hal ini menunjukkan bahwa mahasiswa dapat mengalami penurunan motivasi atau kesulitan dalam mengikuti materi yang semakin kompleks di semester 2.')


    st.markdown("### **13. Bagaimana korelasi usia dengan jumlah SKS yang diambil?**")

    fig, axs = plt.subplots(1, 2, figsize=(14, 6))

    # Scatterplot: Usia vs SKS Semester 1
    sns.scatterplot(
        data=df,
        x='Age at enrollment',
        y='Curricular units 1st sem (enrolled)',
        # hue='Target',
        # alpha=0.6,
        ax=axs[0]
    )
    axs[0].set_title("Usia Mahasiswa vs Jumlah SKS Semester 1")
    axs[0].set_xlabel("Usia Mahasiswa")
    axs[0].set_ylabel("Jumlah SKS (Semester 1)")

    # Scatterplot: Usia vs SKS Semester 2
    sns.scatterplot(
        data=df,
        x='Age at enrollment',
        y='Curricular units 2nd sem (enrolled)',
        # hue='Target',
        # alpha=0.6,
        ax=axs[1]
    )
    axs[1].set_title("Usia Mahasiswa vs Jumlah SKS Semester 2")
    axs[1].set_xlabel("Usia Mahasiswa")
    axs[1].set_ylabel("Jumlah SKS (Semester 2)")

    plt.tight_layout()
    st.pyplot(fig)

    with st.expander("📋 Analisis Visualisasi", expanded=True):
        st.info('Walaupun tidak terlalu tampak korelasi yang kuat, namun bisa terlihat bahwa semakin tua usia mahasiswa, maka semakin sedikit jumlah SKS yang diambil, terutama setelah memasuki semester 2. Tidak ada mahasiswa yang berusia di atas 30 tahun yang mengambil lebih dari 20 SKS pada semester 2.')

        st.info('Hal tersebut dapat disebabkan karena mahasiswa yang lebih tua sudah memiliki banyak kesibukan dan tanggung jawab, seperti pekerjaan dan keluarga sehingga tidak bisa mengambil banyak SKS sebab waktu yang dimiliki juga terbatas.')

    # st.markdown("### **9. Bagaimana distribusi nilai pendaftaran berdasarkan status kelulusannya?**")
    # plt.figure(figsize = (14,6))

    # ax = sns.boxplot(data = df, x = 'Target', y = 'Admission grade', palette='Set1')
    # plt.xlabel('Status Kelulusan')
    # plt.ylabel('Nilai Pendaftaran')
    # plt.title('Nilai Pendaftaran Berdasarkan Status Kelulusan')
    # plt.xticks(ticks=[0, 1], labels=['Dropout', 'Graduate'])

    # st.pyplot(plt)

    # st.markdown("### **9. Bagaimana distribusi status utang terhadap status kelulusan mahasiswa?**")
    # plt.figure(figsize = (10,6))
    # # palette_inverse = sns.color_palette("Set1", n_colors=2)[::-1]  # Membalikkan palet warna
    # ax = sns.countplot(data = df, x = 'Debtor', hue = 'Target', palette="Set1")
    # plt.xlabel('Status Utang')
    # plt.ylabel('Jumlah Mahasiswa')
    # plt.legend(title='Status Kelulusan')
    # debtor_labels = {
    #     0: "Tidak",
    #     1: "Iya",
    # }
    # plt.xticks(ticks=list(debtor_labels.keys()), labels=list(debtor_labels.values()))

    # # Untuk menampilkan nilai detail di atas bar
    # for i in ax.containers:
    #     ax.bar_label(i,)

    # plt.title('Kelulusan Siswa Berdasarkan Status Utang')
    # st.pyplot(plt)


    st.markdown("## **⭐ Kesimpulan**")
    st.write('1. Mahasiswa penerima beasiswa memiliki proporsi kelulusan yang lebih tinggi.')
    st.write('2. Mahasiswa yang masih lajang memiliki proporsi kelulusan yang lebih tinggi dibandingkan yang sudah menikah.')
    st.write('3. Mahasiswa yang memiliki nilai 0 di semester 1 perlu mendapatkan perhatian khusus agar tidak mengulanginya di semester 2.')
    st.write('4. Semakin tinggi nilai mahasiswa, maka semakin tinggi proporsi kelulusannya.')
    st.write('5. Mahasiswa yang berusia di bawah 30 tahun memiliki proporsi kelulusan yang lebih tinggi dibandingkan yang berusia di atas 30 tahun.')
    st.write('6. Mahasiswa yang terlambat membayar uang kuliah memiliki proporsi dropout yang jauh lebih tinggi dibandingkan yang tepat waktu.')
    st.write('7. Mahasiswa yang lulus cenderung mengambil lebih banyak SKS dibandingkan mahasiswa yang dropout.')
    st.write('8. Mahasiswa perempuan memiliki proporsi kelulusan yang lebih tinggi dibandingkan mahasiswa laki-laki.')
    st.write('9. Program studi dengan kode 33, 9119, 9130, 9853, dan 9991 perlu dievaluasi lebih lanjut karena proporsi mahasiswa yang dropout jauh lebih tinggi dibandingkan yang lulus.')
    st.write('10. Mahasiswa penerima beasiswa cenderung memiliki nilai yang lebih tinggi dibandingkan mahasiswa yang tidak menerima beasiswa.')
    st.write('11. Mahasiswa yang lebih muda cenderung memiliki rata-rata nilai yang lebih tinggi dibandingkan mahasiswa yang lebih tua.')
    st.write('12. Rata-rata nilai mahasiswa di semester 2 cenderung lebih rendah dibandingkan semester 1.')
    st.write('13. Mahasiswa yang lebih tua cenderung mengambil lebih sedikit SKS, terutama di semester 2.')


show_insight()