import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.probability import FreqDist
from nltk import NaiveBayesClassifier
from nltk.classify import accuracy as nltk_accuracy

# Sample training data
training_data = [
    ("What's the weather like today?", "weather"),
    ("Can you recommend a good restaurant?", "food"),
    ("How do I fix a leaky faucet?", "home_repair"),
    ("Tell me about the latest tech news.", "technology"),
    # Add more training examples for different topics
]

# Tokenization and preprocessing
def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token.isalnum()]
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return tokens

# Feature extraction
def extract_features(text):
    features = {}
    for word in preprocess(text):
        features[word] = True
    return features

# Train a Naive Bayes classifier
featuresets = [(extract_features(text), topic) for (text, topic) in training_data]
classifier = NaiveBayesClassifier.train(featuresets)

# Test the classifier
test_sentence = "What are the top tech trends this year?"
test_features = extract_features(test_sentence)
print("Predicted topic:", classifier.classify(test_features))
