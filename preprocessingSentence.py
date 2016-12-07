# -*- coding: utf-8 -*-
import string
import re
from dateutil.parser import parse


def sentenceProcessing(sentence):
    """ return clear uniform processed sentence """
    return sentenceAtomSegmentation(spellingStandardization(sentence))


def spellingStandardization(sentence):
    """ implement this if sentence from many nonuniform source.
    To standardize sentence to the unique form of spelling"""
    return sentence


def sentenceAtomSegmentation(sentence):
    """ segment sentence into atom unit which cannot be segmented into smaller unit.
    Atom unit can be morpho-syllable, sign, foreign string,  symbol, abbreviation, factorids"""
    return sentence.split(' ')


# may not use ???
def properNameRecognition():
    """recognizing foreign word, person name, organization name,location,factorids ..."""
    pass


def vietnameseDecimalMatch(value):
    if re.match('\d+[\,\.]\d+', value):
        return True
    return False


def dateFormatMatch(value):
    try:
        parse(value)
        return True
    except Exception:
        return False
