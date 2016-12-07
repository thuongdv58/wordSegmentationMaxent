# -*- coding: utf-8 -*-
import string
from preprocessingSentence import dateFormatMatch,vietnameseDecimalMatch

def maximumMatchingSegment(morphoSyllableList, wset, signSet,foreigns, caseNumber):
    """Segments a string into words prefering longer words givens
    a dictionary wset."""
    # Sort word set in decreasing string order
    token=''
    wset.sort(key=len, reverse=True)
    sentence= u' '.join(morphoSyllableList)
    results = tokenize(sentence, wset, signSet, foreigns, token, caseNumber)
    for result in results:
        result.pop()  # Remove the empty string token
        result.reverse()  # Put the list into correct order
    return results

def tokenize(string, wset, signSet, foreigns, token, caseNumber):
    """Returns either [] if the string can't be segmented by 
    the current wset or a list of words that segment the string
    in reverse order.
    CaseNumber is number of possible segmentations will be return"""

    if string == "":
        return [[token]]
    if string[0] == ' ':
        string = string[1:]
    # Find all possible prefixes
    possibleCases = []
    firstWord = string.split(' ')[0]
    if firstWord in signSet or dateFormatMatch(firstWord) or vietnameseDecimalMatch(firstWord):
        reses = tokenize(
                string.replace(firstWord, '', 1), wset, signSet, foreigns, firstWord, caseNumber-len(possibleCases))
        if reses:
            for res in reses:
                res.append(token)
                possibleCases.append(res)
        if len(possibleCases) >= caseNumber:
            return possibleCases
    else:
        for pref in wset:
            if string.startswith(pref+' ') or string == pref:
                reses = tokenize(
                    string.replace(pref, '', 1), wset, signSet, foreigns, pref, caseNumber-len(possibleCases))
                if reses:
                    for res in reses:
                        res.append(token)
                        possibleCases.append(res)
                if len(possibleCases) >= caseNumber:
                    break
    # Not possible
    return possibleCases
