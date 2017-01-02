# -*- coding: utf-8 -*-
def bestCasesEvaluate(sentences):
    """compute probability for each possible maximum matching cases then
    choose the highest"""
    # featuresCalculation()
    if not sentences:
        return Exception('input invalid')
    return sentences[0]


def linearInterpolationProbability(bigramCount,unigramCount_current,unigramCount_pre,vocabCount,totalCount,alpha1,alpha2):
    return alpha1*(bigramCount+1)/(unigramCount_pre+vocabCount) +alpha2*(unigramCount_current+1)/(vocabCount+totalCount)

def localProbability(phrase,unigramCount,bigramCount,totalCount,alpha1,alpha2):
    vocab=len(unigramCount)
    finalProbab=1
    if unigramCount.has_key(phrase[0]):
        finalProbab= (unigramCount[phrase[0]]+1)/(totalCount+vocab)
    else:
        finalProbab= 1/(totalCount+vocab)

    for index in range(1,len(phrase)):
        word= phrase[index]
        preword= phrase[index-1]
        try:
            bi=bigramCount[word][preword]
        except Exception:
            bi=0
        try:
            uni_current=unigramCount[word]
        except Exception:
            uni_current=0
        try:
            uni_pre=unigramCount[preword]
        except Exception:
            uni_pre=0
        probab=linearInterpolationProbability(bi,uni_current,uni_pre,vocab,totalCount,alpha1,alpha2)
        finalProbab=finalProbab*probab
    return finalProbab

def phraseLinearInterpolationChoose(phrase,unigramCount,bigramCount,totalCount,alpha1,alpha2):
    finalPhrase=[]
    index=1
    while index< len(phrase):
        word=phrase[index].split(' ')
        preword=phrase[index-1].split(' ')
        if len(word)+len(preword)==3 and preword[0] != '<s>':
            atoms=preword+word
            if index-2 >=0:
                phrase1= [phrase[index-2]]
                phrase2= [phrase[index-2]]
            else:
                phrase1=[]
                phrase2=[]
            biword= ' '.join(atoms[0:2])
            phrase1.append(biword)
            phrase1.append(atoms[2])
            phrase2.append(atoms[0])
            phrase2.append(' '.join(atoms[1:3]))
            try:
                phrase1.append(phrase[index+1])
                phrase2.append(phrase[index+1])
            except Exception:
                phrase1=phrase1
            probab1=localProbability(phrase1,unigramCount,bigramCount,totalCount,alpha1,alpha2)
            probab2=localProbability(phrase2,unigramCount,bigramCount,totalCount,alpha1,alpha2)
            if probab1 > probab2:
                finalPhrase.append(u' '.join(atoms[0:2]))
                finalPhrase.append(atoms[2])
            else:
                finalPhrase.append(atoms[0])
                finalPhrase.append(u' '.join(atoms[1:3]))
            index+=1
        else:
            finalPhrase.append(phrase[index-1])
        index+=1
    if len(finalPhrase)!=len(phrase):
        finalPhrase.append(phrase[-1])
    return finalPhrase

from train import readBigram,readUnigram,readWordCount,linearInterpolationTrain
alpha1,alpha2= linearInterpolationTrain()
# print phraseLinearInterpolationChoose(['học','sinh học','sinh học'],readUnigram(),readBigram(),readWordCount(),alpha1,alpha2)