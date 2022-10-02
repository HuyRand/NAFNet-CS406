# NAFNet-CS406-DEPLOYMENT
## Image processing and its application
The applicaiton is carried out with the help of Simple Baselines for Image Restoration and their implementation, hence the structural integrity remains the same as original. The gopro dataset which is performed on is provided by the author of papers is splitted into the train part and the test part accordingly to the paper .Two new models were trained on the 2 smaller datasets with tuned down setting given the limited resources and time, specifically 100 and 215 pair of images consisting of the input image which is blurred and the ground truth. 

(This is repo is only for demonstration and is deployed via streamlit so it isn't modular by any mean and should refer to the author's repo for furthur instruction and notice)

## Quick start
* The training process: [<a href="https://colab.research.google.com/drive/1l6Ci4lgrYf3re6F5_dNvLqlkxjbgWCSR?usp=sharing"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="google colab logo"></a>](https://colab.research.google.com/drive/1l6Ci4lgrYf3re6F5_dNvLqlkxjbgWCSR?usp=sharing)
* The deployed application: [<a href="https://huyrand-nafnet-cs406-app-lpblps.streamlitapp.com/"><img src="https://raw.githubusercontent.com/rlew631/rlew631/b09a7af3f30f8b5a5428dbeb07b9021622018685/red_streamlit.svg" ></a>](https://huyrand-nafnet-cs406-app-lpblps.streamlitapp.com/)
## Reference
The official pytorch implementation of the paper **[NAFNet](https://github.com/megvii-research/NAFNet)**

The official paper **[Simple Baselines for Image Restoration (ECCV2022)](https://github.com/megvii-research/NAFNet)**
## Citations
```
@article{chen2022simple,
  title={Simple Baselines for Image Restoration},
  author={Chen, Liangyu and Chu, Xiaojie and Zhang, Xiangyu and Sun, Jian},
  journal={arXiv preprint arXiv:2204.04676},
  year={2022}
}
```
