from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from supply import read_train_data, read_test_data


def eval_classifier(is_test_run=False, train_file='train.tsv', test_file='data.txt'):
    test_text = read_test_data(test_file, x_col=0)
    train_text, train_labels = read_train_data(file_name=train_file, x_col=1, y_col=2, with_shuffle=True)

    test_labels = []

    if is_test_run:
        train_text, test_text, train_labels, test_labels = train_test_split(train_text, train_labels, test_size=0.2,
                                                                            random_state=0)

    # vct stands for 'vectorizer', which is an utility class to transform word into table of frequencies
    # clf stands for 'classifier', which is an utility class to perform a stochastic gradient descent classification
    # best hyperparameters has been chosen by grid search cross-validation based on f1 score
    classifier = Pipeline([('vct', TfidfVectorizer(use_idf=True, sublinear_tf=True, ngram_range=(1, 2), max_df=0.6)),
                           ('clf', SGDClassifier(average=True, alpha=1e-4, epsilon=1e-8, n_iter=10, random_state=42))])

    classifier = classifier.fit(train_text, train_labels)

    prediction = classifier.predict(test_text)

    if is_test_run:
        print(classification_report(test_labels, prediction))

    return prediction


result = eval_classifier(is_test_run=True)

# write the resulting labels to the file if needed
# with open('answer.csv', 'w') as result_file:
#     result_file.write(u"\"label\"\n".encode('utf-8'))
#     for label in result:
#         result_file.write(u"\"{}\"\n".format(label).encode('utf-8'))
