Project Name:

Medical Prescription Handling Using AI Techniques
Description: Handwritten Text Recognition system that Help pharmacists and normal people to read a doctor’s handwritten prescription.

Based On:

1.Medicine Box: Doctor’s Prescription Recognition Using Deep Machine Learning

2.Doctor’s Cursive Handwriting Recognition System Using Deep Learning

Main Idea:

Help pharmacists and normal people to read a doctor’s handwritten prescription using “CRNN” Computer Vision system.
Using the recognized text and search for the most similar Drug names using an existing API for Drugs.
Save all prescriptions and medical information in a digital format to avoid losing or using any papers.
Used Technologies:

TensorFlow: Model Architecture from SimpleHTR.
Flask: Creating an API to receive image from mobile app and return recognized text and a list of most similar Drug names.
Google Colab: For training the model and as a development server during the test.
MySQL: Creating a Database to store all users information.(See Database Description File)
Explanation:

Train a Convolutional-Recurrent Neural Network "CRNN" model using Handwritten English Words from IAM dataset, using saved model to predict new handwritten words (drug names).

Since the training was operating using Normal English words, so it was predicted that there would be some error ratio in the recognized Drug names to reduce error we used the recognized text from the model and search for the most similar Drug names using an existing API for Drugs getSpellingSuggestions.

Result:

We test the model using 20 images like test image number2 Recognized text: "systonre"

Suggestion list: "Systane"

Model Accuracy: 60.41%

The model accuracy is not good enough to be used in a final product. in future work, the main goal is to improve the model accuracy by using these techniques or other suitable methods:

Using dataset for drug names instead of regular English words.
Improving Model Architecture by adding more Layers.
Using other preprocessing techniques to process images for training
