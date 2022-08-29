# import cltk
# from nltk.tokenize import word_tokenize
# from cltk.tokenizers.lat.lat import LatinWordTokenizer
# import matplotlib.pyplot as plt
#
# from cltk.core.data_types import Process, Pipeline
# from cltk.tokenizers import LatinTokenizationProcess
# from cltk.lemmatize.processes import LatinLemmatizationProcess
# from cltk.languages.utils import get_lang
# from cltk.languages.example_texts import get_example_text
# from cltk.nlp import NLP
# from cltk.lexicon.processes import LatinLexiconProcess
#
## detex -w main.tex | sort --unique > wordlist.txt
# text = open('wordlist.txt', 'r').read()
#
#
# pipe = Pipeline(description="A custom Latin pipeline",     processes=[LatinTokenizationProcess, LatinLemmatizationProcess, LatinLexiconProcess],     language=get_lang("lat"))
# nlp = NLP(language='lat', custom_pipeline=pipe, suppress_banner=True)
#
# cltk_doc = nlp.analyze(text=get_example_text("lat"))
##print(cltk_doc)
#
# def dispersionPlot(text, words, lang):
#    languages = ["en","la"]
#    """
#    en:English
#    la:Latin
#    """
#    if lang in languages:
#        toker = LatinWordTokenizer()
#        tokens = toker.tokenize(text.lower())
#        for i in range(0,len(words)):
#            words[i] = words[i].lower()
#    # Locating the matches of the words in the text.
#        x_length = len(tokens)
#        y_length = len(words)
#        x_list = []
#        y_list = []
#        for i in range(0,x_length):
#            for j in range(0,y_length):
#                if tokens[i]==words[j]:
#                    x_list.append(i+1)
#                    y_list.append(j)
#    #Creation of Dispersion Plot with Matplotlib's pyplot.
#        plt.plot(x_list, y_list, "b|", scalex=.1)
#        plt.yticks(list(range(len(words))), words, color="b")
#        plt.ylim(-1, len(words))
#        plt.xlabel("Lexical Distribution")
#        plt.show()
#    else:
#        print("Language not presently covered by CLTK or wrong language code", lang)
#
#
# words = ["melancholy",]
# dispersionPlot(text, words, "la")

from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

text = open("plain.txt", "r").read()

# fdist = FreqDist(word.lower() for word in word_tokenize(text))
# print(dict(fdist))


from nltk.text import Text

print(len(text))
tokens = word_tokenize(text)
lower_tokens = [word.lower() for word in tokens]
t = Text(lower_tokens)
t.concordance("melancholy", lines=150)
