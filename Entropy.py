# Open source file to extract text
with open('Sample.txt', 'r') as inp:
    data = inp.read()

str = ""
for i in data:
    str += i


def letterCount(str):
    # str = str.lower().strip()
    # str = str.strip(string.punctuation)
    list1 = list(str)
    charCountDict = {}
    for item in list1:
        # if item.isalpha():
        if item in charCountDict:
            charCountDict[item] += 1
        else:
            charCountDict[item] = 1
    totalWords = sum(charCountDict.values())
    return charCountDict, totalWords


# letterCount(str)

import math


def probability(countDict, total):
    newDict = {}
    for key in countDict:
        prob = countDict[key] / total
        newDict[key] = prob
    return newDict


def entropy(probDict):
    sum = 0.0
    for key in probDict:
        sum += probDict[key] * math.log(1 / probDict[key], 2)
    return sum


# def computeInformation(dictionary):
#     return entropy(dictionary) * len()


# n = {"0": 0.25, "1": 0.75}
n, total = letterCount(str)
probDict = (probability(n, sum(n.values())))
print(probDict)
print(entropy(probDict) * total)
