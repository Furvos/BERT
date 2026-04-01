## WordPiece Tokenization

Ao aplicar o tokenizador `bert-base-multilingual-cased` na frase de teste, observamos que várias palavras são divididas em subpalavras. Tokens que começam com o prefixo `##` indicam que aquele fragmento não inicia uma nova palavra, mas sim continua a palavra anterior.

Por exemplo, a palavra "hiper" foi tokenizada como `hip` e `##er`, enquanto a palavra "inconstitucionalmente" foi dividida em múltiplas subpalavras: `in`, `##cons`, `##tit`, `##uc`, `##ional` e `##mente`. O prefixo `##` sinaliza que esses tokens devem ser concatenados ao token anterior para formar a palavra completa.

Essa estratégia permite que o modelo represente palavras raras ou desconhecidas como combinações de subpalavras já presentes no vocabulário. Dessa forma, o modelo evita o uso excessivo do token `[UNK]` (unknown) e consegue generalizar melhor para palavras que não estavam explicitamente presentes no conjunto de treinamento.
