import re

"""stop_words are words are the most common words of a language and are often removed to improve statistics. """
stop_words = {w.strip() for w in open('data/stops.txt', 'r').readlines()}

# Sentiment analysis data from <https://github.com/jeffreybreen/twitter-sentiment-analysis-tutorial-201107>
"""pos_words contain positive English words """
pos_words = {w.strip() for w in open('data/vendor/pos.txt', 'r').readlines() if not w.startswith(';')}

"""neg_words contain negative English words """
neg_words = {w.strip() for w in open('data/vendor/neg.txt', 'r').readlines() if not w.startswith(';')}

"""participants is a tuple of debate participants """
participants = ('CLINTON', 'TRUMP', 'KAINE', 'PENCE')

"""exparticipants is a tuple of debate participants including moderators """
exparticipants = ('CLINTON', 'TRUMP', 'KAINE', 'PENCE', 'HOLT', 'RADDATZ', 'COOPER', 'QUIJANO', 'WALLACE')

"""moderators is a tuple of debate moderators """
moderators = ('HOLT', 'RADDATZ', 'COOPER', 'QUIJANO', 'WALLACE')

# Regular expressions for processing raw debate files
r_line = {who: re.compile(r"%s:((?:.|\s)*?)(?=\s[A-Z]+:)" % who) for who in participants}
r_tokenize = re.compile(r"[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\w\-]+")
r_normalize = re.compile(r"\[(?:Applause|Laughter|Crosstalk|Inaudible)\]")
r_interjections = (
    {a: {p: re.compile(r"%s:.*?\.\.\.\s+(?:\[Crosstalk\])?\s+%s:" % (p, a)) for p in exparticipants} for a in exparticipants},
    {a: {p: re.compile(r"%s:.*?--?\s+%s:" % (p, a)) for p in exparticipants} for a in exparticipants}
)
r_speaker = re.compile("(%s): " % "|".join(exparticipants))
r_applause = re.compile(r"\[Applause\]")
r_laughter = re.compile(r"\[Laughter\]")


def count_reactions(s, speaker, r_expr):
    """count_reactions counts the number of audience reactions to a participant for some regular expression """
    pos = 0
    last = r_speaker.search(s)
    m = last
    count = 0
    while m:
        s = s[m.start()+1:]
        m = r_speaker.search(s)
        r = r_expr.search(s)
        if r and last.group(1) == speaker and (not m or r.start() < m.start()):
            count += 1
        last = m
    return count


def count_interjections(s, agent, patient):
    """count_interjections counts the number of interjections for a given agent and patient participant """
    count = 0
    for r_int in r_interjections:
        count += len(r_int[agent][patient].findall(s))
    return count


def lines(s, who):
    """lines takes a raw debate `s` and a participant `who` and finds all utterances made by `who`. """
    return r_line[who].findall(s)
    

def tokenize(s, stop=False, normalize=False):
    """tokenize splits up the raw string `s` into tokens
    
    tokenize also may apply optional stopping and normalization.
    """
    f = (lambda w: w.lower() not in stop_words) if stop else lambda w: True
    g = (lambda w: w.isalnum()) if normalize else lambda w: True
    if normalize:
        s = r_normalize.sub('', s).lower()
    return [w for w in r_tokenize.findall(s) if f(w) and g(w)]


def freqdist(tokens):
    """freqdist generates a frequency distribution over tokens """
    fd = {}
    for w in tokens:
        fd[w] = 1 + fd.get(w, 0)
    return fd


def freqdistlines(lines):
    """freqdist generates a frequency distribution over tokens in lines format """
    fd = {}
    for tokens in lines:
        for w in tokens:
            fd[w] = 1 + fd.get(w, 0)
    return fd
    

def sortedfd(fd):
    """sortedfd returns a sorted copy of a frequency dictionary (as item tuples). """
    return sorted(fd.items(), key=lambda i: i[1], reverse=True)
    
    
def ngrams(tokens, n, begin='#BEGIN#', end='#END#'):
    """ngrams generates `n`-grams from a token list
    
    You may optionally set the begin and end symbols.
    """
    if n <= 0:
        raise ValueError('n must be positive: %d' % n)
    tokens = [begin] + tokens + [end]
    for i in range(len(tokens) - n + 1):
        yield tuple(tokens[i:i+n])
