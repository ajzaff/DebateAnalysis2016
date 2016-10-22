from __future__ import print_function
import nlp
import sys

"""debates are keys to data value. """
debates = {
    '1':  ['CLINTON', 'TRUMP'],
    '2':  ['CLINTON', 'TRUMP'],
    '3':  ['CLINTON', 'TRUMP'],
    'vp': ['KAINE', 'PENCE']
}


def init():
    """init prepares the raw debate transcript for consumption. """
    global raw, lines, tokens, lens, ns, posw, negw, pwfd, nwfd, spwfd, snwfd, bigrams, trigrams, fd, sfd, bgfd, sbgfd, tgfd, stgfd, vocab, inject, minject, applause, laughter
    raw      = {d: '' for d in debates}  # raw is raw transcript text
    lines    = {d: {} for d in debates}  # lines holds string utterances
    tokens   = {d: {} for d in debates}  # tokens holds tokenized uterances
    lens     = {d: {} for d in debates}  # lens holds lengths of tokenized utterances
    ns       = {d: {} for d in debates}  # ns is the total number of tokens uttered
    posw     = {d: {} for d in debates}  # posw are the list of positive class words uttered
    negw     = {d: {} for d in debates}  # negw are the list of negative class words uttered
    pwfd     = {d: {} for d in debates}  # pwfd is a frequency distribution of positive class words
    nwfd     = {d: {} for d in debates}  # nwfd is a frequency distribution of positive class words 
    spwfd    = {d: {} for d in debates}  # spwfd holds positive class word items sorted by frequency
    snwfd    = {d: {} for d in debates}  # snwfd holds negative class word items sorted by frequency
    bigrams  = {d: {} for d in debates}  # bigrams is arrays of bigrams for each debate
    trigrams = {d: {} for d in debates}  # trigrams is arrays of trigrams for each debate
    fd       = {d: {} for d in debates}  # fd holds frequency distribution of tokens
    sfd      = {d: {} for d in debates}  # sfd holds token fd items in sorted order
    bgfd     = {d: {} for d in debates}  # bgfd holds frequency distributions of token bigrams
    sbgfd    = {d: {} for d in debates}  # sbgfd holds token bigram fd items in sorted order
    tgfd     = {d: {} for d in debates}  # tgfd holds frequency distributions of token trigrams
    stgfd    = {d: {} for d in debates}  # stgfd holds token trigram fd items in sorted order
    vocab    = {d: {} for d in debates}  # vocab holds the set of vocabularies
    inject   = {d: {} for d in debates}  # inject is count of the number of debate interjections
    minject  = {d: {} for d in debates}  # minject is the count on the number of moderator interjections
    applause = {d: {} for d in debates}  # applause is the count of applause for each participant
    laughter = {d: {} for d in debates}  # laughter is the count of audience laughter for each participant
    for d in debates:
        with open('data/%s.txt' % d, 'r') as f:
            raw[d] = f.read()
            for p in debates[d]:
                lines[d][p]    = nlp.lines(raw[d], who=p)
                tokens[d][p]   = [nlp.tokenize(line, stop=True, normalize=True) for line in lines[d][p]]
                lens[d][p]     = [len(u) for u in tokens[d][p]]
                ns[d][p]       = sum(lens[d][p])
                posw[d][p]     = [w for u in tokens[d][p] for w in u if w in nlp.pos_words]
                negw[d][p]     = [w for u in tokens[d][p] for w in u if w in nlp.neg_words]
                pwfd[d][p]     = nlp.freqdist(posw[d][p])
                nwfd[d][p]     = nlp.freqdist(negw[d][p])
                spwfd[d][p]    = nlp.sortedfd(pwfd[d][p])
                snwfd[d][p]    = nlp.sortedfd(nwfd[d][p])
                bigrams[d][p]  = [list(nlp.ngrams(u, 2)) for u in tokens[d][p]]
                trigrams[d][p] = [list(nlp.ngrams(u, 3)) for u in tokens[d][p]]
                fd[d][p]       = nlp.freqdistlines(tokens[d][p])
                sfd[d][p]      = nlp.sortedfd(fd[d][p])
                bgfd[d][p]     = nlp.freqdistlines(bigrams[d][p])
                sbgfd[d][p]    = nlp.sortedfd(bgfd[d][p])
                tgfd[d][p]     = nlp.freqdistlines(trigrams[d][p])
                stgfd[d][p]    = nlp.sortedfd(tgfd[d][p])
                vocab[d][p]    = set([t for ts in tokens[d][p] for t in ts])
                inject[d][p]   = {who: nlp.count_interjections(raw[d], p, who) for who in nlp.participants}
                minject[d][p]  = {who: nlp.count_interjections(raw[d], p, who) for who in nlp.moderators}
                applause[d][p] = nlp.count_reactions(raw[d], p, nlp.r_applause)
                laughter[d][p] = nlp.count_reactions(raw[d], p, nlp.r_laughter)


OUTPUT_FORMAT='html'  # plain | html


def print_header(d, width=40):
    """print_header prints a table header row """
    if OUTPUT_FORMAT == 'plain':
        print(('(%s)' % d).ljust(width), end='')
        for p in debates[d]:
            print(p.ljust(width), end='')
        print()
    elif OUTPUT_FORMAT == 'html':
        print('<tr>')
        print('<th></th>')
        for p in debates[d]:
            print('<th>%s</th>' % p)
        print('</tr>')
    else:
        raise ValueError('bad output format: %s' % OUTPUT_FORMAT)
    

def print_subheading(d, heading, width=40):
    """print_subheading prints a table subheading row """
    if OUTPUT_FORMAT == 'plain':
        print(heading.ljust(width), end='')
        for p in debates[d]:
            print('-'.ljust(width), end='')
        print()
    elif OUTPUT_FORMAT == 'html':
        print('<tr>')
        print('<th colspan="%d">%s</th>' % (len(debates[d]), heading))
        print('</tr>')
    else:
        raise ValueError('bad output format: %s' % OUTPUT_FORMAT)


def print_simple_row(d, heading, func, width=40):
    """print_simple_row prints a single row of stats using func """
    if OUTPUT_FORMAT == 'plain':
        print(heading.ljust(width), end='')
        for p in debates[d]:
            print(str(func(d, p)).ljust(width), end='')
        print()
    elif OUTPUT_FORMAT == 'html':
        print('<tr>')
        print('<th>%s</th>' % heading)
        for p in debates[d]:
            print('<td>%s</td>' % str(func(d, p)))
        print('</tr>')
    else:
        raise ValueError('bad output format: %s' % OUTPUT_FORMAT)
    
    
def print_enumerated_rows(d, heading, fd, key_format='%s', n=10, width=40):
    """print_enumerated_row prints multiple rows of stats using func """
    print_subheading(d, heading, width=width)
    if OUTPUT_FORMAT == 'plain':
        for i in range(n):
            print(('        %d' % (i + 1)).ljust(width), end='')
            for p in debates[d]:
                print(str.format('{c} {w}', c=str(fd[d][p][i][1]).ljust(4), w=key_format % fd[d][p][i][0]).ljust(width), end='')
            print()
        print()
    elif OUTPUT_FORMAT == 'html':
        for i in range(n):
            print('<tr>')
            print('<th>%d</th>' % (i + 1))
            for p in debates[d]:
                print('<td>%s</td>' % str.format('{c} {w}', c=fd[d][p][i][1], w=key_format % fd[d][p][i][0]))
            print('</tr>')
    else:
        raise ValueError('bad output format: %s' % OUTPUT_FORMAT)
    
    
def percent(a, b, f='%.2f'):
    return f % (100. * a / b)


def suite(
    do_total=True,
    do_vocab=True,
    do_diversity=True,
    do_average=True,
    do_sentiment=True,
    do_interjections=True,
    do_applause=True,
    do_laughter=True,
    do_unigram=True,
    do_positives=True,
    do_bigrams=True,
    do_trigrams=True,
    num_examples=15,
    width=40
    ):
    """suite runs the stats suite for the all debate transcripts."""
    init()
    
    for d in sorted(debates):
        # Start table
        if OUTPUT_FORMAT == 'plain':
            print('-' * (1 + len(debates[d])) * width)
            print()
        elif OUTPUT_FORMAT == 'html':
            print('<table>')
            
        print_header(d, width=width)

        if do_total:
            # Total utterances
            print_simple_row(d, 'total tokens      (tokens)', lambda d, p: ns[d][p], width=width)
            
        if do_total:
            # Total utterances
            print_simple_row(d, 'total utterances   (lines)', lambda d, p: len(lines[d][p]), width=width)
            
        if do_vocab:
            # Vocabulary size
            print_simple_row(d, 'vocab size        (tokens)', lambda d, p: len(vocab[d][p]), width=width)
            
        if do_diversity:
            # Lexical diversity
            print_simple_row(d, 'lexical diversity      (%)', lambda d, p: percent(len(vocab[d][p]), ns[d][p]), width=width)
        
        if do_average:
            # Average utterance
            print_simple_row(d, 'average utterance (tokens)', lambda d, p: ns[d][p] / len(tokens[d][p]), width=width)
        
        if do_sentiment:
            # Sentiment score
            print_simple_row(d, 'positivity score       (%)', lambda d, p: percent(len(set(posw[d][p])), len(set(posw[d][p])) + len(set(negw[d][p]))), width=width)
        
        if do_interjections:
            # Print instances of debate interjections
            print_simple_row(d, 'cut off other  (instances)', lambda d, p: sum(inject[d][p].values()), width=width)
            
        if do_interjections:
            # Print instances of moderator interjections
            print_simple_row(d, 'cut off moder  (instances)', lambda d, p: sum(minject[d][p].values()), width=width)
            
        if do_applause:
            # Print instances of audience applause
            print_simple_row(d, 'applause       (instances)', lambda d, p: applause[d][p], width=width)
            
        if do_laughter:
            # Print instances of audience laughter
            print_simple_row(d, 'laughter       (instances)', lambda d, p: laughter[d][p], width=width)
        
        if do_unigram:
            # Top unigrams 
            print_enumerated_rows(d, 'top unigrams      (tokens)', sfd, n=num_examples, width=width)
            
        if do_positives:
            # Top unigrams 
            print_enumerated_rows(d, 'top positive      (tokens)', spwfd, n=num_examples, width=width)
            
        if do_positives:
            # Top unigrams 
            print_enumerated_rows(d, 'top negative      (tokens)', snwfd, n=num_examples, width=width)
            
        if do_bigrams:
            # Top bigrams
            print_enumerated_rows(d, 'top bigrams    (token x 2)', sbgfd, n=num_examples, width=width, key_format='%s %s')
            
        if do_trigrams:
            # Top bigrams
            print_enumerated_rows(d, 'top trigrams   (token x 3)', stgfd, n=num_examples, width=width, key_format='%s %s %s')
        
        # End Table
        if OUTPUT_FORMAT == 'plain':
            print()
        elif OUTPUT_FORMAT == 'html':
            print('</table>')
        

if __name__ == '__main__':
    suite(width=30)