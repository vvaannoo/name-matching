import re

char_mapping = {
    'ა': 'a',
    'ბ': 'b',
    'გ': 'g',
    'დ': 'd',
    'ე': 'e',
    'ვ': 'v',
    'ზ': 'z',
    'თ': 't',
    'ი': 'i',
    'კ': 'k',
    'ლ': 'l',
    'მ': 'm',
    'ნ': 'n',
    'ო': 'o',
    'პ': 'p',
    'ჟ': 'zh',
    'რ': 'r',
    'ს': 's',
    'ტ': 't',
    'უ': 'u',
    'ფ': 'ph',
    'ქ': 'k',
    'ღ': 'gh',
    'ყ': 'k',
    'შ': 'sh',
    'ჩ': 'ch',
    'ც': 'ts',
    'ძ': 'dz',
    'წ': 'ts',
    'ჭ': 'ch',
    'ხ': 'kh',
    'ჯ': 'j',
    'ჰ': 'h'
}

stopwords = {'mr', 'ms', 'mrs', 'dze', 'asuli', 'as', 'ogli', 'oglu', 'ogly', 'oglou', 'or'}


def remove_symbols(s):
    return re.sub(r'[^a-z]+', ' ', s).strip()


def tokenize(s):
    s = normalize(s)
    return s.split() if s else []


def remove_stopwords(tokens):
    return list(filter(lambda token: token not in stopwords, tokens))


def transliterate(s):
    if not s:
        return None
    return ''.join([char_mapping.get(c) if c in char_mapping else c for c in s])


def normalize(s):
    if not s:
        return None
    s = transliterate(s)
    s = s.lower()
    s = remove_symbols(s)
    return s


def normalize_and_tokenize(s):
    tokens = tokenize(s)
    return remove_stopwords(tokens)
