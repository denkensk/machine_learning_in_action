import kNN

def main():
    group, labels = kNN.createDataSet()
    print kNN.classify0([0,0], group, labels, 3)

main()