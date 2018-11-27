from string import *
from math import *
import os
import collections,re

def fichierInverse():
    k = 1
    N = 4
    freq = {}
    ListCar = {".", ",", "!", '?', "'"}
    stoplist = open('stopwords_fr.txt', 'r')
    stoplist = stoplist.read()
    stoplist = stoplist.lower()
    stoplist = stoplist.split()

    while (k<=N):
        #f = open('./DocsFatim/D'+str(k)+'.txt','r')
        f = open('D'+str(k)+'.txt','r')
        t = f.read()
        t = t.lower()
        i=0
        while (i < len(t)):
            if (t[i] in ListCar):
                t=t.replace(t[i], " ")
            i = i + 1
        a = t.split()
        nb = len(a)
        for w in a:
            if (not w in stoplist and len(w) > 1):
                if (w, k) not in freq:
                    freq[w, k] = a.count(w)
        k = k + 1

        f.close()
    return freq


#cette fonction retourne un dictionnaire de frequence d'un fichier numDoc (terme): freq
def indexDoc(freq, numDoc):
    li = {}
    for (a, b) in freq:
        if (b == numDoc):

            li[a]=freq[a, b]
    return li



def indexMot(freq, mot):
    li = {}
   # print("le mot")
   # print(mot)
    for (w, d) in freq:
        if (w == mot):
            li[mot,d] = freq[w, d]
    return li


def cleanQuery(query):
    query = query.lower()
    ListCar = {'.', ',', '!', '?', '"', ':', ';', "'"}
    stoplist = open('stopwords_fr.txt', 'r')
    stoplist = stoplist.read()
    stoplist = stoplist.lower()
    stoplist = stoplist.split()
    import re
    a = re.split('\s+',query)
    i = 0
    while i < len(query):
        if query[i] in ListCar:
            query = query.replace(query[i], " ")
        i += 1

    f =""
    for w in a:
        if w not in stoplist and len(w) > 1:
            if w not in f:
                f=f+" "+w

    li=f.split()
    f=" ".join(li)
    return f
def myMax(freq):
    maxi = {}
    for (w, d) in freq:
        if not d in maxi:
            maxi[d] = freq[w, d]
        else:
            if (maxi[d] < freq[w, d]):
                maxi[d] = freq[w, d]
    return maxi


def ni(freq):
    ni = {}
    for (w1, d1) in freq:
        if w1 not in ni:
            ni[w1] = 1
        else:
            ni[w1] += 1
    return ni

def N():
    return 4

#Retourne un dictionnaire contenant (terme, numeroDuFichier):poids
def tfIdf(freq):
    poids = {}
    for (w, d) in freq:
        poids[w,d] = (float(freq[w,d]) / float(myMax(freq)[d])) * log10(float(N()) / float(ni(freq)[w]) + 1)
    
    
    return poids


#print("**************************ponderation TF*IDF*************************")


def poidFichier(numDoc,poids):
    liste = {}
    for (w, d) in poids:
        if (numDoc == d):
            liste[w] = poids[w, d]
    return liste


def poidWord(word,poids):
    liste = {}
    for (w, d) in poids:
        if (word == w):
            liste[d] = poids[w, d]

    return liste



