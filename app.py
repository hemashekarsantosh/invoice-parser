from pdf2image import convert_from_bytes
import easyocr
import streamlit as st
from PIL import Image
import os
from pathlib import Path
import easyocr

def get_text(img_text):
  final_text=" "
  for _, text, _ in img_text:
    final_text+=" "
    final_text+= text
  return final_text

st.set_page_config(
     page_title="Invoice Parser",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",
 )

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Invoice Parser")

uploaded_file = st.file_uploader("Choose an PDF...", type="pdf")
if uploaded_file is not None:
    image = convert_from_bytes(uploaded_file.getvalue(),300)[0]
    #image = Image.open(images)
    #st.image(image, caption='Uploaded PDF.', use_column_width=True)
    directory = "tempDir"
    path = os.path.join(os.getcwd(), directory)
    p = Path(path)
    if not p.exists():
        os.mkdir(p)
    file_loc =uploaded_file.name+'.png'
    image.save(os.path.join(p,file_loc))
    reader = easyocr.Reader(['en'])
    img_text = reader.readtext(os.path.join(p,file_loc))
    text=" "
    text+=get_text(img_text)
    
    col1, col2 = st.beta_columns(2)
    with col1:
        st.header("Uploaded PDF")
        st.image(image, use_column_width=True)
    with col2:
        st.header("OCR Text")
        st.write(text)
