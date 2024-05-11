from newspaper import Article
import Base

def GetPage(url):
    page = Article(url)
    page.download()
    page.parse()    
    return page.text



def stripWord(word):
    _skipChars = []
    for _c in set(Base.INVALID_CHARS).union(set(Base.MATH_SYMBOL)).union(set(Base.NUMBERS)):
        word = word.replace(_c,'')
    return word    

def stripSentence(word):
    _skipChars = []
    for _c in set(Base.INVALID_CHARS).union(set(Base.MATH_SYMBOL)):
        word = word.replace(_c,'')
    return word    

def GetSentences(url):
    _text = GetPage(url)
    #_items = _text.split('.').join('. ').split('!').join('. ').split('?').join('. ').split('.')
    _items = []
    for _c in Base.SENTENCE_CHAR:
        _sentences = _text.split(_c)
        for _s in _sentences:
            _items.append(stripSentence(_s))

    _results = []
    for _item in _items:
        _s = stripSentence(_item)
        _results.append(_s)
    return _results


def GetWords(url,n,isDistinct):
    _text = GetPage(url)    
    _words = _text.split(' ')
    _results = []
    for _word in _words:
        _results.append(stripWord(_word))
    
    if(isDistinct == True):
        _results = list(set(_results))

    if(n == 0):
        return _results
    else:
        return list(filter(lambda x:len(x)==n,_results))

# url = "https://niithanoi.edu.vn/phim-tat-trong-visual-studio-code.html"
#url = "https://vnexpress.net/thu-tuong-neu-6-muc-tieu-chong-covid-19-4325397.html"
#print(GetSentences(url))
# print(GetWords(url,1))
# print(GetWords(url,2))
# print(GetWords(url,3))
# print(GetWords(url,4))
# print(GetWords(url,5))
# print(GetWords(url,6))
# print(GetWords(url,7))
# print(GetWords(url,8))