# -*- coding: utf-8 -*-
import string


def maximumMatchingSegment(string, wset, caseNumber):
    """Segments a string into words prefering longer words givens
    a dictionary wset."""
    # Sort word set in decreasing string order
    wset.sort(key=len, reverse=True)
    results = tokenize(string, wset, "", caseNumber)
    if not results:
        raise Exception("No possible segmentation!")
    for result in results:
        result.pop()  # Remove the empty string token
        result.reverse()  # Put the list into correct order
    return results


def tokenize(string, wset, token, caseNumber):
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
    for pref in wset:
        if string.startswith(pref+' ') or string == pref:
            reses = tokenize(
                string.replace(pref, '', 1), wset, pref, caseNumber-len(possibleCases))
            if reses:
                for res in reses:
                    res.append(token)
                    possibleCases.append(res)
            if len(possibleCases) >= caseNumber:
                break
    # Not possible
    return possibleCases