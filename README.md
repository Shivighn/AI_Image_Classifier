# Image Classification using CNN

This project aims to classify images into 2 different classes using a convolutional neural network (CNN). The dataset used for this project is the CIFAKE: Real and AI-Generated Synthetic Images in Kaggle by JORDAN J. BIRD, There are 100,000 images for training (50k per class) and 20,000 for testing (10k per class) which contains 60,000 synthetically-generated images and 60,000 real images (collected from CIFAR-10) of size 32x32 pixels, divided into 2 classes: FAKE, REAL.

## Usage
1. Clone this repository to your local machine using the following command:
   ```bash
   git clone https://github.com/Shivighn/AI_Image_Classifier.git
   ```
2. To view or run the notebook you can run it in Kaggle as the dataset is available in Kaggle
     Open the image-classifier.ipynb in Kaggle.
3. To run it locally you need a few dependencies:
   - streamlit
   - openCV
   - Tensorflow
   - Numpy
   - Keras
   - PIL

    You can download them using pip:
   ```
   pip install streamlit opencv-python keras tensorflow numpy pillow
   ```
   
4. To run it locally you need to open main.py and util.py
   Then in the terminal in your desired code editor in which these 2 codes are open, run:
   ```
   streamlit run main.py
   ```
5. Now the project has opened locally in your machine.
   Try it out by uploading the images and getting the classification shown.
   I suggest you use the cifake 32*32 images (test_images folder) in this model for testing as this isn't perfect for HD images.

## Results
The CNN model achieved an accuracy of 98%, a precision of 0.96, and a recall of 1, on the test set. The model could classify most images that are 32*32 size correctly, but it also had some misclassifications for the images that are not of that size.

## Contributions
We welcome contributions from the community. Feel free to suggest improvements, fixes, or new features through issues or pull requests.
