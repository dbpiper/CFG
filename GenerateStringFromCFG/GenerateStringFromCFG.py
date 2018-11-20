from nltk import CFG, ChartParser
from random import choice
import configparser

# based on this example:
#   https://stackoverflow.com/questions/603687/how-do-i-generate-sentences-from-a-formal-grammar/3292027#3292027


cfg_file = open('./config/CFG.txt', 'r')
config = configparser.ConfigParser()
config.read('./config/config.ini')

max_len = int(float(config['default']['max_len']))


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
grammar = CFG.fromstring(cfg_file.read())

parser = ChartParser(grammar)

gr = parser.grammar()


def generate_string(grammar_parser):

    return produce(grammar_parser, grammar_parser.start())


generated_string = generate_string(gr)
if max_len > 0:
    while len(generated_string) > max_len:
        generated_string = generate_string(gr)

print(' '.join(generated_string))
