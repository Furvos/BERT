from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")

sentence = "Os hiper-parâmetros do transformer são inconstitucionalmente difíceis de ajustar."

tokens = tokenizer.tokenize(sentence)

print(tokens)