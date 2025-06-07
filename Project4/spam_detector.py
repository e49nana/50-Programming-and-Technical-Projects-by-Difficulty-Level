import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

def load_data(filepath="spam.csv"):
    df = pd.read_csv(filepath, encoding='latin-1')[['v1', 'v2']]
    df.columns = ['label', 'text']
    return df

def preprocess_and_train(df):
    X = df['text']
    y = df['label'].map({'ham': 0, 'spam': 1})

    vectorizer = TfidfVectorizer(stop_words='english')
    X_vect = vectorizer.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_vect, y, test_size=0.3, random_state=42)

    model = MultinomialNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print(classification_report(y_test, y_pred))
    return model, vectorizer

def predict(model, vectorizer, new_texts):
    X_new = vectorizer.transform(new_texts)
    predictions = model.predict(X_new)
    return ["spam" if p == 1 else "ham" for p in predictions]

if __name__ == "__main__":
    df = load_data()
    model, vectorizer = preprocess_and_train(df)
    examples = ["Win money now!", "Are we still meeting today?"]
    results = predict(model, vectorizer, examples)
    for text, label in zip(examples, results):
        print(f"'{text}' -> {label}")
