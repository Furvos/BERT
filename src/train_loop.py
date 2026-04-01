from data.vocab import vocab
from get_stats import get_stats
from merge_vocab import merge_vocab

for i in range(5):

    pairs = get_stats(vocab)

    best = max(pairs, key=pairs.get)

    vocab = merge_vocab(best, vocab)

    print(f"\nIteração {i+1}")
    print("Par fundido:", best)
    print("Vocab:", vocab)