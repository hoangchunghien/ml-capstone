
# Overview
While go through vacation photos, people always ask themself: What is the name of this temple I visited in Thailand? Who created this monument in France? Landmark recognition can help! This technology can predict landmark labels directly from image pixels, to help people better understand and organize their photo collections.
 
In this project, a model use for landmark recognition will be built based on ImageNet Classification With Deep Convolutional Neural Networks

# Requirements
- Python 3.x
- Install the requirements packages `pip install -r requirements.txt`

# Dataset
- The dataset can be downloaded from [Google Landmark Recognition Challenge](https://www.kaggle.com/c/landmark-recognition-challenge/data).
- Unzip the downloaded dataset and put under `src/data/dataset.csv` and follow the notebook `src/analysis.ipynb` or just use the reduced version of the original dataset.
- Use the script `src/utils/download_data.py` to download the images. Use the command line way: `python src/utils/download_data.py "src/data/train.csv" "src/data/train"` or just follow the notebook `src/analysis.ipynb`

# File Descriptions
- `src/data/train.csv` - the training images set
- `src/data/valid.csv` - the validation images set
- `src/data/test.csv` - the test images set
- `src/analysis.ipynb` - The notebook that I've used to analyze and preprocess dataset
- `src/benchmark_model.ipynb` - The notebook that I've used to build a benchmark model
- `src/vgg16_model.ipynb` - The notebook that I've used to build my final solution
