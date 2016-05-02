import sys
import url_classifier
from collections import Counter


def main():
    # Load dirty dataset
    dataset = url_classifier.load_dataset('url_dataset.txt')
    classes = []

    # Open normalized datafile
    f = open('normalized_urls.txt', 'w')

    autos = ['Vehicles', 'Vehicle', 'Off-Road', 'Autos']
    shopping = ["Shopping", "Textiles", "Nonwovens", "Retailers", "Consumer", "Goods", "Equipment", "Accessories", "Apparel"]
    education = ['Educational', 'Education', 'Sciences', 'Science']
    business = ['Business', 'Finance', 'Telecom', 'Investing', 'Industry', 'Industrial']
    art = ['Arts', 'Art', 'Visual', 'Performing', 'Design']
    entertainment = ['Entertainment', 'Media', 'Movies', 'Music', 'Literature', 'Video', 'Fitness']
    reference = ['Reference', 'Resources', 'Interests']
    sports = ['Sports', 'Sporting']
    news = ['News', 'Leisure', 'World', 'People', 'Society']
    technology = ['Computer', 'Electronics', 'Computers', 'Internet', 'Technology', 'Hardware']
    government = ['Law', 'Government']
    games = ['Games', 'Toys']

    for i in range(0, len(dataset)):

        if any(s in dataset[i][0] for s in autos):
            dataset[i][0] = 'Autos'
        elif any(s in dataset[i][0] for s in shopping):
            dataset[i][0] = 'Shopping'
        elif any(s in dataset[i][0] for s in education):
            dataset[i][0] = 'Education'
        elif any(s in dataset[i][0] for s in business):
            dataset[i][0] = 'Business'
        elif any(s in dataset[i][0] for s in art):
            dataset[i][0] = 'Art'
        elif any(s in dataset[i][0] for s in entertainment):
            dataset[i][0] = 'Entertainment'
        elif any(s in dataset[i][0] for s in reference):
            dataset[i][0] = 'Reference'
        elif any(s in dataset[i][0] for s in sports):
            dataset[i][0] = 'Sports'
        elif any(s in dataset[i][0] for s in news):
            dataset[i][0] = 'News'
        elif any(s in dataset[i][0] for s in technology):
            dataset[i][0] = 'Technology'
        elif any(s in dataset[i][0] for s in government):
            dataset[i][0] = 'Government'
        elif any(s in dataset[i][0] for s in games):
            dataset[i][0] = 'Games'
        else:
            dataset[i][0] = 'General'

        classes.append(dataset[i][0])

        # Write normalized data point to file
        f.write(dataset[i][0] + '\t' + dataset[i][1] + '\t' + dataset[i][2])

    # Print stats on new dataset
    count = Counter(classes)
    print "Data points: " + str(len(classes))
    print count

    # Close file
    f.close()

if __name__ == "__main__":
    sys.exit(main())
