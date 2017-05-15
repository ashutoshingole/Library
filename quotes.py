import json
import random


def read_quotes():
    with open('quotes.json') as f:
        lines = (l.strip() for l in f)
        return [json.loads(l.decode('utf-8')) for l in lines if l]


def get_quote_and_author():
    quotes = read_quotes()
    return random.choice(quotes)