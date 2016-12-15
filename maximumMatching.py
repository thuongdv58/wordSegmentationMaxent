# -*- coding: utf-8 -*-
import string
import collections
import math
import re
from preprocessingSentence import Lower,Upper,isLower,isUpper
class Graph:

    ''' graph class inspired by https://gist.github.com/econchick/4666413
    '''

    def __init__(self):
        self.vertices = set()

        # makes the default value for all vertices an empty list
        self.edges = collections.defaultdict(list)
        self.weights = {}

    def add_vertex(self, value):
        self.vertices.add(value)

    def add_edge(self, from_vertex, to_vertex, distance):
        if from_vertex == to_vertex:
            pass  # no cycles allowed
        self.edges[from_vertex].append(to_vertex)
        self.weights[(from_vertex, to_vertex)] = distance

    def __str__(self):
        string = "Vertices: " + str(self.vertices) + "\n"
        string += "Edges: " + str(self.edges) + "\n"
        string += "Weights: " + str(self.weights)
        return string


def dijkstra(graph, start):
    # initializations
    S = set()

    # delta represents the length shortest distance paths from start -> v, for v in delta.
    # We initialize it so that every vertex has a path of infinity (this line
    # will break if you run python 2)
    delta = dict.fromkeys(list(graph.vertices), 10000)
    previous = dict.fromkeys(list(graph.vertices), None)

    # then we set the path length of the start vertex to 0
    delta[start] = 0

    # while there exists a vertex v not in S
    while S != graph.vertices:
        # let v be the closest vertex that has not been visited...it will begin
        # at 'start'
        v = min((set(delta.keys()) - S), key=delta.get)

        # for each neighbor of v not in S
        for neighbor in set(graph.edges[v]) - S:
            new_path = delta[v] + graph.weights[v, neighbor]

            # is the new path from neighbor through
            if new_path < delta[neighbor]:
                # since it's optimal, update the shortest path for neighbor
                delta[neighbor] = new_path
            # set the previous vertex of neighbor to v
                previous[neighbor] = v
        S.add(v)

    return (delta, previous)


def shortest_path(graph, start, end):
    '''Uses dijkstra function in order to output the shortest path from start to end
    '''

    delta, previous = dijkstra(graph, start)

    path = []
    vertex = end

    while vertex is not None:
        path.append(vertex)
        vertex = previous[vertex]

    path.reverse()
    return path


def maximumMatchingGraph(sentence, wset):
    segmentedSentence=[]
    G = Graph()
    score = [7, 4, 2.5, 1, 1]

    foreignWordScore=[40,35,40,50,100]
    wordList = sentence.split(' ')
    firstWord= None
    firstCapital=False
    if isUpper(wordList[0][0]): 
        if isLower(wordList[1][0]):
            wordList[0]= Lower(wordList[0][0])+wordList[0][1:]
            firstCapital=True
        else:
            for index in range(1,len(wordList)):
                if isLower(wordList[index][0]):
                    break
            if index >1:
                firstWord=' '.join(wordList[0:index])
                wordList=wordList[index:]

    wordList.append('end')  # last node
    sentenceLength = len(wordList)
    for wordIndex in range(sentenceLength):
        G.add_vertex(wordIndex)
    for i in range(sentenceLength):
        edgeRange = min(sentenceLength-i, 5)
        for edge in range(edgeRange):
            if ' '.join(wordList[i:i+edge+1]) in wset[edge+1]:
                G.add_edge(i, i+edge+1, score[edge])
            # else:
            #     G.add_edge(i, i+edge+1, score[edge])
    path=shortest_path(G, 0, sentenceLength-1)
    for i in range(len(path)-1):
        segmentedSentence.append(' '.join(wordList[path[i]:path[i+1]]))
    if firstWord:
        return [firstWord]+segmentedSentence
    if firstCapital:
        segmentedSentence[0]=Upper(segmentedSentence[0][0])+segmentedSentence[0][1:]

    return segmentedSentence

def maximumMatchingSegment(sentence, wset, foreigns, caseNumber):
    """Segments a string into words prefering longer words givens
    a dictionary wset."""
    # Sort word set in decreasing string order
    token = ''
    results = tokenize(sentence, wset, foreigns, token, caseNumber)
    for result in results:
        result.pop()  # Remove the empty string token
        result.reverse()  # Put the list into correct order
    return results


def tokenize(string, wset, foreigns, token, caseNumber):
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
                string.replace(pref, '', 1), wset, foreigns, pref, caseNumber-len(possibleCases))
            if reses:
                for res in reses:
                    res.append(token)
                    possibleCases.append(res)
            if len(possibleCases) >= caseNumber:
                break
    # Not possible
    return possibleCases
