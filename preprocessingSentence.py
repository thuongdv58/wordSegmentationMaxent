# -*- coding: utf-8 -*-
import string
import re
from dateutil.parser import parse
from dictionaryRead import *

def sentenceProcessing(sentence,signdict):
    """ return clear uniform processed sentence """
    sentence= spellingStandardization(sentence)
    atomSentence=[]
    phrases= sentence.split(' ')
    spliter=True
    for phrase in phrases:
        for Atom in sentenceAtomSegmentation(phrase,signdict):
            if Atom in signdict or vietnameseDecimalMatch(phrase) or dateFormatMatch(phrase) or URLFormatMatch(phrase):
                atomSentence.append(Atom)
                spliter=True
            else:
                if spliter:
                    atomSentence.append(Atom)
                    spliter=False
                else:
                    atomSentence[-1]+=' '+Atom
    return atomSentence
    
def spellingStandardization(sentence):
    """ implement this if sentence from many nonuniform source.
    To standardize sentence to the unique form of spelling"""
    return sentence


def sentenceAtomSegmentation(phrase,signdict):
    """ segment sentence into atom unit which cannot be segmented into smaller unit.
    Atom unit can be morpho-syllable, sign, foreign string,  symbol, abbreviation, factorids"""
    if re.match("^[ạảãàáâậầấẩẫăắằặẳẵóòọõỏôộổỗồốơờớợởỡéèẻẹẽêếềệểễúùụủũưựữửừứíìịỉĩýỳỷỵỹđa-zA-Z]*$", phrase):
        return [phrase]
    atomPhrase=[]
    tail=''
    if phrase[0] in signdict:
        atomPhrase.append(phrase[0])
        phrase=phrase[1:]
    if phrase and phrase[-1] in signdict:
        tail=phrase[-1]
        phrase=phrase[:-1]
    if vietnameseDecimalMatch(phrase) or dateFormatMatch(phrase) or URLFormatMatch(phrase):
        atomPhrase.append(phrase)
    else:
        for sign in signdict:
            phrase= (' '+sign+' ').join(filter(None, phrase.split(sign)))
        atomPhrase += phrase.split(' ')
    if tail:
        atomPhrase.append(tail)
    return filter(None,atomPhrase)


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

def URLFormatMatch(value):
    try:
        re.search("(?P<url>(?:https|http|ftp|smtp)://[^\s]+)", value).group("url")
        return True
    except Exception:
        return False

def Upper(s):
    if type(s) == type(u""):
       return s.upper()
    return unicode(s, "utf8").upper().encode("utf8")

def Lower(s):
    if type(s) == type(u""):
       return s.lower()
    return unicode(s, "utf8").lower().encode("utf8")

def isUpper(s):
    try:
        return unicode(s, "utf8").isupper()
    except Exception:
        return s.isupper()

def isLower(s):
    try:
        return unicode(s, "utf8").islower()
    except Exception:
        return s.islower()