from gensim.models import KeyedVectors

import janome
import sys
from janome.analyzer import Analyzer
from janome.tokenizer import Tokenizer
from janome.tokenfilter import *
import collections

# model_dir = './entity_vector/entity_vector.model.bin'
# model = KeyedVectors.load_word2vec_format(model_dir, binary=True)

def Morphological_Analysis(text, parts):
    '''
    text : 形態素解析を行いたい文章
    parts　：　品詞
    '''

    tokenizer = Tokenizer()
    # a = Analyzer(token_filters=[POSKeepFilter(parts)])
    
    # parts_list = ([token.surface for token in a.analyze(text)
    #    if token.part_of_speech.startswith(parts)])

    b  = Analyzer(token_filters=[POSKeepFilter(parts), TokenCountFilter()])
    c = list(b.analyze(text))[:10]
    d = sorted(c, reverse=True, key=lambda x: x[1])
    word_count = list(map(lambda x: x[0], d))
    return word_count

def W2V(word_count,model):
  if len(word_count) !=0:
      
    posi = [word for word in word_count if word in model]
    print(posi)

    results = model.most_similar(positive=posi)
    result = results[0][0]

    return result
  else:
    return "..."


# while True:

  # script = input('Enter Script : ')
  # result, word_count = Morphological_Analysis(script, '名詞')
  # result = W2V()
  # print(result)