# NAFNet-CS406-DEPLOYMENT
## Image processing and its application
The applicaiton is carried out with the help of Simple Baselines for Image Restoration and their implementation, hence the structural integrity remains the same as original. The gopro dataset which is performed on is provided by the author of papers is splitted into the train part and the test part accordingly to the paper .Two new models were trained on the 2 smaller datasets with tuned down setting given the limited resources and time, specifically 100 and 215 pair of images consisting of the input image which is blurred and the ground truth. 

(This is repo is only for demonstration and is deployed via streamlit so it's not modular by any mean and one should refer to the author's repo for furthur instruction and notice)

## Dataset
The gopro dataset provided by Seungjun Nah consists of 3,214 blurred images with the size 1,280×720 that are divided into 2,103 training images and 1,111 test images. The dataset consists of pairs of a realistic blurry image and the corresponding ground truth sharp image that are obtained by a high-speed camera.

The 2 models we experimented were trained on a 100 and 215 training images dataset.
* The 100 images dataset: https://drive.google.com/file/d/1RjPUSwx52PIYeCIQyYzNbdbxGMMIXgmo/view?usp=sharing
* The 215 images dataset: https://drive.google.com/file/d/1njXPwcowUR4179yXzCagiQYQL8UZfeOK/view?usp=sharing

## Installation guide
* Clone the repo and make a virtual environment using requirements.txt via anaconda
```
pip install -r requirements.txt
```
* Run the application
```
streamlit run App.py
```
* The application will run locally on port 8501
## Quick start
* The training process
* - 100 images: [<a href="https://colab.research.google.com/drive/16g4UNwuob_qRSTAfyusUqWiugVN71Dls?usp=sharing"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="google colab logo"></a>](https://colab.research.google.com/drive/16g4UNwuob_qRSTAfyusUqWiugVN71Dls?usp=sharing)
* - 215 images:[<a href="https://colab.research.google.com/drive/1qUmWq3n5F8Xtj2SPu6Vs6hd2dxpzQKJZ?usp=sharing"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="google colab logo"></a>](https://colab.research.google.com/drive/1qUmWq3n5F8Xtj2SPu6Vs6hd2dxpzQKJZ?usp=sharing)
* The deployed application: [<a href="https://huyrand-nafnet-cs406-app-lpblps.streamlitapp.com/"><img src="https://raw.githubusercontent.com/rlew631/rlew631/b09a7af3f30f8b5a5428dbeb07b9021622018685/red_streamlit.svg" ></a>](https://huyrand-nafnet-cs406-app-lpblps.streamlitapp.com/)
## Reference
The official pytorch implementation of the paper **[NAFNet](https://github.com/megvii-research/NAFNet)**

The official paper **[Simple Baselines for Image Restoration (ECCV2022)](https://arxiv.org/abs/2204.04676)**
## Citations
```
@article{chen2022simple,
  title={Simple Baselines for Image Restoration},
  author={Chen, Liangyu and Chu, Xiaojie and Zhang, Xiangyu and Sun, Jian},
  journal={arXiv preprint arXiv:2204.04676},
  year={2022}
}
```

```
@InProceedings{Nah_2017_CVPR,
  author = {Nah, Seungjun and Kim, Tae Hyun and Lee, Kyoung Mu},
  title = {Deep Multi-Scale Convolutional Neural Network for Dynamic Scene Deblurring},
  booktitle = {CVPR},
  month = {July},
  year = {2017}
}
```
