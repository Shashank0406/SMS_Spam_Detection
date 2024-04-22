# Spam Detection Project

This project focuses on building a spam detection system using machine learning techniques. Below are the steps involved in the development process:

1. Data Collection:

The dataset used for this project was obtained from Kaggle. It consists of SMS messages labeled as spam or ham.

2. Data Cleaning:

Removed columns with missing values using pandas drop() function.
Renamed columns for clarity.
Converted non-numerical values in the target column to numerical values (0 for ham, 1 for spam) using Label Encoder from scikit-learn.

3. Exploratory Data Analysis (EDA):

Checked for null values and duplicates.
Visualized the distribution of spam and ham messages using pie charts.
Investigated the data's characteristics through summary statistics and visualization using seaborn.

4. Text Processing:

Utilized NLTK library for text processing.
Tokenized messages into words and sentences.
Calculated the number of characters, words, and sentences in each message.
Preprocessed text by converting to lowercase, removing special characters, punctuation, stop words, and stemming.

5. Model Building:

Applied Naive Bayes Classifier due to its effectiveness with text data.
Used TF-IDF vectorizer to convert text data into numerical format.
Split data into training and testing sets.
Trained various classification algorithms including GaussianNB, MultinomialNB, and BernoulliNB.
Evaluated models based on accuracy and precision scores.

6. Evaluation and Improvements:

Tuned hyperparameters for Multinomial Naive Bayes model.
Explored other classification algorithms including Logistic Regression, Support Vector Machines, Decision Trees, etc.
Selected Multinomial Naive Bayes as the best-performing model based on evaluation metrics.

7. Pickle Files:

Saved TF-IDF vectorizer and Multinomial Naive Bayes model using pickle for future use.

8. Deployment:

Deployed the spam detection system using Streamlit for its simplicity and ease of use.
