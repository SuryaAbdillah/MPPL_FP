import streamlit as st
import requests
from PIL import Image
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np
# from streamlit_back_camera_input import back_camera_input

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# Sidebar
with st.sidebar:
    selected = option_menu("Konversi",
        ["Carakan Madura ke Alfabet Latin",
        "Alfabet Latin ke Carakan Madura"],
        default_index=0)

# function to predict latin OCR
def predik(IMAGE_PATH, flag):
    # READ LATIN HANDWRITING
    reader = easyocr.Reader(['id'])
    result = reader.readtext(IMAGE_PATH)
    
    kalimat = ""
    for i in range(len(result)):
        kalimat += result[i][1] + " "

    # st.write(kalimat)
    if flag == 0:
        input = st.text_area("Hasil Scan :", key='01', value=kalimat,height=50)
    if flag == 1:
        input = st.text_area("Hasil Terjemahan :", key='11', value=kalimat,height=50)
        

    # CARAKAN KE LATIN
    if(selected == "Carakan Madura ke Alfabet Latin"):
        kalimat = "ꦥꦶꦝꦥꦺꦚ"
        dictionary = {"ꦥꦶ":"pi", "ꦥꦸ":"pu", "ꦥꦺꦴ":"po", "ꦥꦺ":"pe", "ꦝꦶ":"dhi", "ꦝꦸ":"dhu", "ꦝꦺꦴ":"dho", "ꦝꦺ":"dhe", "ꦗꦶ":"ji", "ꦗꦸ":"ju", "ꦗꦺꦴ":"jo", "ꦗꦺ":"je", "ꦪꦶ":"yi", "ꦪꦸ":"yu", "ꦪꦺꦴ":"yo", "ꦪꦺ":"ye", "ꦚꦶ":"nyi", "ꦚꦸ":"nyu", "ꦚꦺꦴ":"nyo", "ꦚꦺ":"nye", "ꦩꦶ":"mi", "ꦩꦸ":"mu", "ꦩꦺꦴ":"mo", "ꦩꦺ":"me", "ꦒꦶ":"gi", "ꦒꦸ":"gu", "ꦒꦺꦴ":"go", "ꦒꦺ":"ge", "ꦧꦶ":"bi","ꦧꦸ":"bu", "ꦧꦺꦴ":"bo", "ꦧꦺ":"be", "ꦛꦶ":"thi", "ꦛꦸ":"thu", "ꦛꦺꦴ":"tho", "ꦛꦺ":"the", "ꦔꦶ":"ngi", "ꦔꦸ":"ngu", "ꦔꦺꦴ":"ngo", "ꦔꦺ":"nge", "ꦲꦶ":"hi", "ꦲꦸ":"hu", "ꦲꦺꦴ":"ho", "ꦲꦺ":"he", "ꦤꦶ":"ni", "ꦤꦸ":"nu", "ꦤꦺꦴ":"no", "ꦤꦺ":"ne", "ꦕꦶ":"ci", "ꦕꦸ":"cu", "ꦕꦺꦴ":"co", "ꦕꦺ":"ce", "ꦫꦶ":"ri", "ꦫꦸ":"ru", "ꦫꦺꦴ":"ro", "ꦫꦺ":"re", "ꦏꦶ":"ki", "ꦏꦸ":"ku", "ꦏꦺꦴ":"ko", "ꦏꦺ":"ke", "ꦢꦶ":"di", "ꦢꦸ":"du", "ꦢꦺꦴ":"do", "ꦢꦺ":"de", "ꦠꦶ":"ti", "ꦠꦸ":"tu", "ꦠꦺꦴ":"to", "ꦠꦺ":"te", "ꦱꦶ":"si", "ꦱꦸ":"su", "ꦱꦺꦴ":"so", "ꦱꦺ":"se", "ꦮꦶ":"wi", "ꦮꦸ":"wu", "ꦮꦺꦴ":"wo", "ꦮꦺ":"we", "ꦭꦶ":"li", "ꦭꦸ":"lu", "ꦭꦺꦴ":"lo", "ꦭꦺ":"le"}
        dictionary2 = {"ꦥ":"pa", "ꦝ":"dha", "ꦗ":"ja", "ꦪ":"ya", "ꦚ":"nya", "ꦩ":"ma", "ꦒ":"ga", "ꦧ":"ba", "ꦛ":"tha", "ꦔ":"nga","ꦲ":"ha", "ꦤ":"na", "ꦕ":"ca", "ꦫ":"ra", "ꦏ":"ka", "ꦢ":"da", "ꦠ":"ta", "ꦱ":"sa", "ꦮ":"wa", "ꦭ":"la", "ꦲ":"a"}
        for char in dictionary.keys():
            kalimat = kalimat.replace(char, dictionary[char])
        for char in dictionary2.keys():
            kalimat = kalimat.replace(char, dictionary2[char])

        # st.write(kalimat)
        if flag == 0:
            input = st.text_area("Hasil Scan :", key='02', value=kalimat,height=50)
        if flag == 1:
            input = st.text_area("Hasil Terjemahan :", key='12', value=kalimat,height=50)
        
    # LATIN KE CARAKAN
    if(selected == "Alfabet Latin ke Carakan Madura"):
        dictionary = {"pa":"ꦥ", "pi":"ꦥꦶ", "pu":"ꦥꦸ", "pe":"ꦥꦺ", "po":"ꦥꦺꦴ", "dha":"ꦝ", "dhi":"ꦝꦶ", "dhu":"ꦝꦸ", "dhe":"ꦝꦺ", "dho":"ꦝꦺꦴ", "ja":"ꦗ", "ji":"ꦗꦶ", "ju":"ꦗꦸ", "je":"ꦗꦺ", "jo":"ꦗꦺꦴ", "ya":"ꦪ", "yi":"ꦪꦶ", "yu":"ꦪꦸ", "ye":"ꦪꦺ", "yo":"ꦪꦺꦴ", "nya":"ꦚ", "nyi":"ꦚꦶ", "nyu":"ꦚꦸ", "nye":"ꦚꦺ", "nyo":"ꦚꦺꦴ", "ma":"ꦩ", "mi":"ꦩꦶ", "mu":"ꦩꦸ", "me":"ꦩꦺ", "mo":"ꦩꦺꦴ", "ga":"ꦒ", "gi":"ꦒꦶ", "gu":"ꦒꦸ", "ge":"ꦒꦺ", "go":"ꦒꦺꦴ", "ba":"ꦧ", "bi":"ꦧꦶ","bu":"ꦧꦸ", "be":"ꦧꦺ", "bo":"ꦧꦺꦴ", "tha":"ꦛ", "thi":"ꦛꦶ", "thu":"ꦛꦸ", "the":"ꦛꦺ", "tho":"ꦛꦺꦴ", "nga":"ꦔ", "ngi":"ꦔꦶ", "ngu":"ꦔꦸ", "nge":"ꦔꦺ", "ngo":"ꦔꦺꦴ","ha":"ꦲ", "hi":"ꦲꦶ", "hu":"ꦲꦸ", "he":"ꦲꦺ", "ho":"ꦲꦺꦴ", "na":"ꦤ", "ni":"ꦤꦶ", "nu":"ꦤꦸ", "ne":"ꦤꦺ", "no":"ꦤꦺꦴ", "ca":"ꦕ", "ci":"ꦕꦶ", "cu":"ꦕꦸ", "ce":"ꦕꦺ", "co":"ꦕꦺꦴ", "ra":"ꦫ", "ri":"ꦫꦶ", "ru":"ꦫꦸ", "re":"ꦫꦺ", "ro":"ꦫꦺꦴ", "ka":"ꦏ", "ki":"ꦏꦶ", "ku":"ꦏꦸ", "ke":"ꦏꦺ", "ko":"ꦏꦺꦴ", "da":"ꦢ", "di":"ꦢꦶ", "du":"ꦢꦸ", "de":"ꦢꦺ", "do":"ꦢꦺꦴ", "ta":"ꦠ", "ti":"ꦠꦶ", "tu":"ꦠꦸ", "te":"ꦠꦺ", "to":"ꦠꦺꦴ", "sa":"ꦱ", "si":"ꦱꦶ", "su":"ꦱꦸ", "se":"ꦱꦺ", "so":"ꦱꦺꦴ", "wa":"ꦮ", "wi":"ꦮꦶ", "wu":"ꦮꦸ", "we":"ꦮꦺ", "wo":"ꦮꦺꦴ", "la":"ꦭ", "li":"ꦭꦶ", "lu":"ꦭꦸ", "le":"ꦭꦺ", "lo":"ꦭꦺꦴ"}

        kalimat = kalimat.lower()

        for char in dictionary.keys():
            kalimat = kalimat.replace(char, dictionary[char])

        # st.write(kalimat)
        if flag == 0:
            input = st.text_area("Hasil Scan :", key='03', value=kalimat,height=50)
        if flag == 1:
            input = st.text_area("Hasil Terjemahan :", key='13', value=kalimat,height=50)

# function for loading lottie
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottie("https://assets5.lottiefiles.com/packages/lf20_b6LhWw.json")
lottie_coding2 = load_lottie("https://assets1.lottiefiles.com/packages/lf20_NxAJBy.json")
lottie_coding3 = load_lottie("https://assets5.lottiefiles.com/packages/lf20_0isufwmo.json")

# load CSS STYLE 
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# PAGE PENGENALAN
with st.container():
    st.title("CAMAD")
    image = Image.open('gambar/carakan.jpeg')
    st.image(image)
    st.write("CAMAD merupakan sebuah aplikasi yang membantu para pengguna untuk mengartikan tulisan carakan madura.")

# PAGE HOW TO USE
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)

    with left_column:
        st.header('Cara Penggunaan')
        st.write("#")
        st.write(
            """
            Cara menggunakan aplikasi ini adalah sebagai berikut:
            - Pilih jenis konversi yang ingin dilakukan pada side bar (sisi kiri)
            - Lakukan upload foto baik melalui fitur upload file maupun ambil gambar secara langsung
            - Tunggu beberapa saat hingga hasil dari scan dan terjemahaan foto muncul
            """
        )

    with right_column:
        st_lottie(lottie_coding, height=200, key="photo")
        st_lottie(lottie_coding2, height=200, key="upload")

# INPUT GAMBAR DARI UPLOAD FILE
with st.container():
    st.write("---")
    st.header('Upload/Ambil Gambar')

with st.container():
    file = st.file_uploader("Silahkan Upload Foto", type=(['png', 'jpg', 'jpeg']))

if file is None:
    st.text('')
else:
    image = Image.open(file)
    # st.image(image)
    predik(image, 0)

st.text("")

# INPUT GAMBAR DARI KAMERA
cam_file = st.camera_input("Ambil Gambar")
# cam_file = st.back_camera_input("Ambil Gambar")

if cam_file is None:
    st.text('')
else:
    cam_image = Image.open(cam_file)
    # show file image
    # st.image(cam_image)
    predik(cam_image, 1)