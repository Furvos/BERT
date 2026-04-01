import get_stats, merge_vocab

for i in range(5):

    pairs = get_stats(vocab)

    best = max(pairs, key=pairs.get)

    vocab = merge_vocab(best, vocab)

    print(vocab)