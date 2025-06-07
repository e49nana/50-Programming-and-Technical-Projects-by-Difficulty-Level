from spam_detector import load_data, preprocess_and_train, predict

def test_predict():
    df = load_data()
    model, vectorizer = preprocess_and_train(df)
    results = predict(model, vectorizer, ["Hello friend", "You won a prize"])
    assert len(results) == 2
    assert all(r in ["spam", "ham"] for r in results)
    print("Test passed.")

if __name__ == "__main__":
    test_predict()
