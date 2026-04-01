# Laboratório 6 — Tokenização com BPE e WordPiece

## Objetivo

Este laboratório teve como objetivo compreender como modelos de linguagem modernos processam texto através de **tokenização baseada em subpalavras**. Foram explorados dois métodos amplamente utilizados:

* **Byte Pair Encoding (BPE)**, implementado manualmente para entender seu funcionamento interno.
* **WordPiece**, utilizado por modelos da família BERT e acessado através da biblioteca Hugging Face.

A atividade buscou demonstrar como esses métodos permitem representar palavras raras ou desconhecidas de forma eficiente.

---

# Parte 1 — Implementação do Byte Pair Encoding (BPE)

## Corpus inicial

O treinamento do tokenizador foi realizado sobre um pequeno corpus simulado, representado por um dicionário contendo palavras separadas em caracteres e suas frequências:

```
vocab = {
'l o w </w>': 5,
'l o w e r </w>': 2,
'n e w e s t </w>': 6,
'w i d e s t </w>': 3
}
```

O símbolo `</w>` representa o **fim da palavra**, permitindo que o algoritmo identifique limites morfológicos.

---

## Motor de Frequências

Foi implementada a função `get_stats(vocab)`, responsável por calcular a frequência de **pares adjacentes de símbolos** no corpus.

A função percorre cada palavra do vocabulário, separa seus símbolos e contabiliza os pares consecutivos, ponderando pela frequência da palavra.

Exemplo de resultado esperado:

```
('e','s') → 9
```

Esse valor ocorre porque o par aparece:

* 6 vezes em `newest`
* 3 vezes em `widest`

---

## Operação de Fusão (Merge)

Foi implementada a função:

```
merge_vocab(pair, vocab)
```

Essa função substitui todas as ocorrências do par mais frequente por um novo token unificado.

Exemplo:

```
e s → es
```

Assim, a palavra:

```
n e w e s t </w>
```

passa a ser representada como:

```
n e w es t </w>
```

---

## Loop de Treinamento do BPE

O treinamento do tokenizador foi realizado por **5 iterações**, repetindo o seguinte processo:

1. calcular as frequências dos pares
2. identificar o par mais frequente
3. realizar a fusão no vocabulário
4. atualizar o corpus

Resultados observados:

| Iteração | Par Fundido    | Resultado |
| -------- | -------------- | --------- |
| 1        | ('e','s')      | es        |
| 2        | ('es','t')     | est       |
| 3        | ('est','</w>') | est</w>   |
| 4        | ('l','o')      | lo        |
| 5        | ('lo','w')     | low       |

Esse processo demonstra como o algoritmo aprende **estruturas morfológicas comuns**, como o sufixo `est`.

---

# Parte 2 — Tokenização com WordPiece

Após a implementação do BPE, foi utilizado o tokenizador multilíngue do BERT através da biblioteca Hugging Face:

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")
```

A seguinte frase foi utilizada para teste:

```
Os hiper-parâmetros do transformer são inconstitucionalmente difíceis de ajustar.
```

Resultado da tokenização:

```
['Os', 'hip', '##er', '-', 'par', '##âm', '##etros', 'do', 'transform', '##er',
'são', 'in', '##cons', '##tit', '##uc', '##ional', '##mente',
'di', '##f', '##í', '##cei', '##s', 'de', 'aj', '##usta', '##r', '.']
```

---

# Significado do prefixo `##`

No WordPiece, tokens que começam com `##` indicam que **o fragmento não inicia uma nova palavra**, mas sim continua a palavra anterior.

Exemplo:

```
hip + ##er → hiper
```

Outro exemplo mais complexo:

```
in + ##cons + ##tit + ##uc + ##ional + ##mente
```

que forma a palavra:

```
inconstitucionalmente
```

---

# Por que subpalavras evitam vocabulário desconhecido

Sem tokenização por subpalavras, palavras que não aparecem no treinamento seriam representadas como:

```
[UNK]
```

Isso faz com que o modelo perca completamente a informação da palavra.

Com métodos como BPE ou WordPiece, palavras raras podem ser decompostas em **subcomponentes conhecidos**, permitindo que o modelo:

* represente qualquer palavra
* reutilize padrões morfológicos
* mantenha um vocabulário relativamente pequeno

Essa abordagem é um dos fatores que possibilitam a escalabilidade dos **Transformers modernos**.

---

# Conclusão

Neste laboratório foi possível compreender na prática o funcionamento de dois métodos fundamentais de tokenização utilizados em processamento de linguagem natural.

A implementação do **BPE** demonstrou como tokens podem ser construídos gradualmente a partir de padrões frequentes no corpus. Já o uso do **WordPiece** mostrou como modelos reais, como o BERT, utilizam subpalavras para representar palavras complexas e raras de maneira eficiente.

Esses mecanismos são essenciais para permitir que modelos de linguagem lidem com grandes vocabulários e generalizem para textos não vistos durante o treinamento.


obs: IA generativa foi utilizada na criação deste documento README.md