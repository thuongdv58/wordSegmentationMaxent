# -*- coding: utf-8 -*-
import string

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
    return sentence


#may not use ???
def properNameRecognition():
    """recognizing foreign word, person name, organization name,location,factorids ..."""
    pass
