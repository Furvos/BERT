from data.vocab import vocab

pair = ('o', 'w')

def merge_vocab(pair, v_in):
    v_out = {}
    bigram = ' '.join(pair)
    replacement = ''.join(pair)
    for word, freq in v_in.items():
        new_word = word.replace(bigram, replacement)
        v_out[new_word] = freq
    return v_out

print(merge_vocab(pair, vocab))