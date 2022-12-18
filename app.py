import streamlit as st
import requests
from PIL import Image
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# Sidebar
with st.sidebar:
    selected = option_menu("Konversi",
        ["Carakan Madura ke Alfabet Latin",
        "Alfabet Latin ke Carakan Madura"],
        default_index=0)

# Penggunaan
# if(selected == "Carakan Madura ke Alfabet Latin"):

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottie("https://assets5.lottiefiles.com/packages/lf20_b6LhWw.json")
lottie_coding2 = load_lottie("https://assets1.lottiefiles.com/packages/lf20_NxAJBy.json")
lottie_coding3 = load_lottie("https://assets5.lottiefiles.com/packages/lf20_0isufwmo.json")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

with st.container():
    st.title("CAMAD")
    image = Image.open('gambar/carakan.jpeg')
    st.image(image)
    st.write("CAMAD merupakan sebuah aplikasi yang membantu para pengguna untuk mengartikan tulisan carakan madura.")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)

    with left_column:
        st.header('Cara Penggunaan')
        st.write("#")
        st.write(
            """
            Cara menggunakan aplikasi ini adalah sebagai berikut:
            - Lakukan upload foto baik melalui fitur upload file maupun ambil gambar secara langsung
            - Tunggu beberapasaat hingga hasil dari scan foto muncul
            - Setelah hasil muncul pastikan hasil scan sesuai dengan text yang difoto
            - Pilih tombol terjemahkan untuk menampilkan hasil terjemahan dari tulisan carakan madura
            """
        )

    with right_column:
        st_lottie(lottie_coding, height=200, key="photo")
        st_lottie(lottie_coding2, height=200, key="upload")

with st.container():
    st.write("---")
    st.header('Upload/Ambil Gambar')


with st.container():
        uploaded_file = st.file_uploader("Silahkan Upload Foto", type='png, jpg')
if uploaded_file is not None:
  
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)


    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)


    string_data = stringio.read()
    st.write(string_data)

    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)


img_file_buffer = st.camera_input("Ambil Gambar")

if img_file_buffer is not None:
        
    bytes_data = img_file_buffer.getvalue()
   
    st.write(type(bytes_data))


with st.container():
    st.header("Hasil Scan dan Terjemahan")
    st.write("##")
    left_column, right_column = st.columns(2)
    with left_column:
        st_lottie(lottie_coding3, height=200, key="hasil")

text = ""
btnTest = 1
if st.checkbox('test'):
    btnTest = 1

if btnTest:
    text = "surya"

input = st.text_area("Hasil Scan :", value=text,height=100)

output = input.upper() # final_result_from_processing_the_input


if st.checkbox('Translate Sentence'):
    if input == "":
        st.warning('Please **enter text** for translation')

    else:
        st.text_area('Terjemahan :',value=output,height=100)

