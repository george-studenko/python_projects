#!/usr/bin/env python3
"""
Author : George Studenko <george@georgestudenko.com>
Date   : 09-apr-2020
Purpose: Crow's Nest -- choose the correct article
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crow''s Nest -- choose the correct article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='str',
                        help='A word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Start the program"""

    args = get_args()
    word = args.word
    print_message(word)


def print_message(word):
    article = get_article(word)
    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')


def get_article(word):
    article = 'a'
    if word[0].lower() in 'aeiou':
        article = 'an'
    return article


# --------------------------------------------------
if __name__ == '__main__':
    main()
