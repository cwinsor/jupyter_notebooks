def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        contents = pickle.load(fo, encoding='bytes')
    return contents
