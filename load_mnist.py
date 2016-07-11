import pickle, gzip

def load_mnist(fname):
    with gzip.open(fname, 'rb') as f:
        train_set, valid_set, test_set = pickle.load(f, encoding='latin1')
    return train_set, valid_set, test_set