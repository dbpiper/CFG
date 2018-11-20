from nltk import CFG, ChartParser
from random import choice

# based on this example:
#   https://stackoverflow.com/questions/603687/how-do-i-generate-sentences-from-a-formal-grammar/3292027#3292027

MAX_LEN = 7

def produce(cfg, symbol):

    words = []
    productions = cfg.productions(lhs=symbol)
    production = choice(productions)
    for sym in production.rhs():
        if isinstance(sym, str):
            words.append(sym)
        else:
            words.extend(produce(cfg, sym))
    return words


# using A instead of S' because CFG.fromstring rejects S'
grammar = CFG.fromstring('''
A -> S
S -> '(' L ')'
S -> 'x'
L -> S
L -> L ',' S
''')

parser = ChartParser(grammar)

gr = parser.grammar()


def generate_string(grammar_parser):

    return produce(grammar_parser, grammar_parser.start())


generated_string = generate_string(gr)
while len(generated_string) > MAX_LEN:
    generated_string = generate_string(gr)

print(generated_string)
print(' '.join(generated_string))
