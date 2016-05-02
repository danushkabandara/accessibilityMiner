import sys
import urllib
import lxml.html
import random
import numpy as np
import pickle
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


class target(object):
    target_names = {}
    target = None

    def __init__(self, classes):
        i = 0
        # Obtain unique classes
        unique = set(classes)
        # Assign id to each unique class
        for name in unique:
            self.target_names[name] = i
            i += 1

        # Construct numpy id array for classifier
        x = [self.target_names[name] for name in classes]
        self.target = np.array(x)

    def target_name(self):
        return [key for key, value in self.target_names.iteritems()]

    def print_target_name(self, ids):
        if ids in self.target_names.values():
            for key, value in self.target_names.iteritems():
                if value == ids:
                    return key
        else:
            print "Id not valid."
            return None


def load_dataset(filename):
    dataset = []
    f = open(filename, 'r')
    for line in f.readlines():
        dataset.append(line.split('\t'))
    f.close()
    return dataset


# Separate dataset in train data and test data
def split_dataset(dataset):
    # Randomize element in dataset
    random.shuffle(dataset)
    train_limit = int(len(dataset) * (2.0/3.0))
    test_limit = len(dataset)
    print train_limit
    print test_limit
    train_dataset = dataset[:train_limit]
    test_dataset = dataset[train_limit:test_limit]
    return train_dataset, test_dataset


# Get url metadata description of a given url
def get_url_description(url):
    try:
        request_url = urllib.urlopen(url)
        resource = lxml.html.fromstring(request_url.read())
        # Extract document metadata
        meta = resource.xpath('//meta')
        for elem in meta:
            if elem.get('name') == "description":
                description = elem.get('content')
                print "Description: " + description
                return True, description
            else:
                return False, None
    except:
        e = sys.exc_info()
        print e
        return False, e


def train_classifier(train_dataset, test_dataset):
    train_classes = []
    train_descriptions = []
    test_classes = []
    test_descriptions = []
    count_vector = CountVectorizer()
    tfidf_transformer = TfidfTransformer()

    model = open("url_classifier.pkl", 'wb')

    # Split both classes and descriptions for train dataset
    for elem in train_dataset:
        train_classes.append(elem[0])
        train_descriptions.append(elem[2])

    # Split both classes and descriptions for test dataset
    for elem in test_dataset:
        test_classes.append(elem[0])
        test_descriptions.append(elem[2])

    # Convert train classes to numpy array
    train_targets = target(train_classes)

    # Convert test classes to numpy array
    test_targets = target(test_classes)

    # Vectorize descriptions
    X_train_counts = count_vector.fit_transform(train_descriptions)

    # Construct feature vector
    X_train_ttfidf = tfidf_transformer.fit_transform(X_train_counts)

    # Train classifier
    clf = MultinomialNB().fit(X_train_ttfidf, train_targets.target)

    # Persist classifier model
    pickle.dump(clf, model)

    # Persist feature matrix
    pickle.dump(count_vector, model)
    pickle.dump(tfidf_transformer, model)
    pickle.dump(test_targets, model)

    model.close()

    # Vectorize test data point
    X_new_counts = count_vector.transform(test_descriptions)
    X_new_tfidf = tfidf_transformer.transform(X_new_counts)

    predicted = clf.predict(X_new_tfidf)

    print np.mean(predicted == test_targets.target)

    print(metrics.classification_report(test_targets.target, predicted, \
        target_names=test_targets.target_name()))


def classify_url(url, desc):
    # Open pickle file
    model = open('url_classifier.pkl', 'rb')

    # Load classifier
    clf = pickle.load(model)
    count_vector = pickle.load(model)
    tfidf_transformer = pickle.load(model)
    targets = pickle.load(model)

    # Vectorize test data point
    X_new_counts = count_vector.transform(desc)
    X_new_tfidf = tfidf_transformer.transform(X_new_counts)

    predicted = clf.predict(X_new_tfidf)

    model.close()

    print "{} classified as {}".format(desc, targets.print_target_name(predicted[0]))

    return predicted


def main():
    # Load url dataset
    dataset = load_dataset('normalized_urls.txt')

    # Split dataset in train and test data
    train_dataset, test_dataset = split_dataset(dataset)

    # Train classifier on train and test data
    train_classifier(train_dataset, test_dataset)

    # Test classifier on arbitrary point

    data = "Disc Golf Equipment | DICK'S Sporting"

    classify_url(None, data)


if __name__ == "__main__":
    sys.exit(main())
