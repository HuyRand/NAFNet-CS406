import streamlit as st
import setup

from basicsr.models import create_model
from basicsr.utils import img2tensor as _img2tensor, tensor2img, imwrite
from basicsr.utils.options import parse
import numpy as np
import cv2


def imread(uploaded_file):
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img
def img2tensor(img, bgr2rgb=False, float32=True):
    img = img.astype(np.float32) / 255.
    return _img2tensor(img, bgr2rgb=bgr2rgb, float32=float32)

def single_image_inference(model, img):
      model.feed_data(data={'lq': img.unsqueeze(dim=0)})

      if model.opt['val'].get('grids', False):
          model.grids()

      model.test()

      if model.opt['val'].get('grids', False):
          model.grids_inverse()

      visuals = model.get_current_visuals()
      sr_img = tensor2img([visuals['result']])
      return sr_img

st.title('CS406-NAFNet-Image Deblurring')
uploaded_file = st.file_uploader("Choose a file",type = (["jpg", "jpeg","png"]))
if uploaded_file is not None:
    img_input=imread(uploaded_file)
    option = st.selectbox('Pretrained model type',
                        ('None','Best','100 images','215 images'))

    opt_path = None



    if option == 'Best':
        opt_path = 'options/test/GoPro/NAFNet-width32.yml' 
    elif option == '100 images':
        opt_path = 'options/test/GoPro/NAFNet-width32-100images.yml'
    elif option == '215 images':
        opt_path = 'options/test/GoPro/NAFNet-width32-215images.yml'
    if st.button('Process'):
        if opt_path == None or option=='None':
            st.write('Please select model')
        else:
            
            opt = parse(opt_path, is_train=False)
            opt['dist'] = False

            data_load_state = st.text('Loading model...')
            NAFNet = create_model(opt)
            data_load_state.text('Loading model...done!')

            inp = img2tensor(img_input)
            data_load_state_process = st.text('Processing image...')
            processed_image = single_image_inference(NAFNet, inp)
            data_load_state_process = st.text('Processing image...done!')

            col1, col2 = st.columns(2)
            with col1:
                st.header("Original")
                st.image(img_input)
            with col2:
                st.header("Deblurred")
                st.image(processed_image, channels="BGR")


