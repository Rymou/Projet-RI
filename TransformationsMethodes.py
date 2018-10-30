from string import *
from math import *
import os


def fichierInverse():
    k = 1
    N = 4
    freq = {}
    ListCar = {'.', ',', '!', '?', '"','-','_',':',';'}
    stoplist = open('stopwords_fr.txt', 'r')
    stoplist = stoplist.read()
    stoplist = stoplist.lower()
    stoplist = stoplist.split(",")

    while (k<=N):
        print("Indexe de fréquences du document",k)
        f = open('D'+str(k)+'.txt','r')
        t = f.read()
        t = t.lower()
        i=0
        while (i < len(t)):
            if (t[i] in ListCar):
                t.replace(t[i], " ")
            i = i + 1
        a = t.split()
        nb = len(a)
        for w in a:
            if (not w in stoplist and len(w) > 1):
                if (not (w, k) in freq):
                    freq[w, k] = a.count(w)
                   # print(w,k,freq[w, k])
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
    for (w, d) in freq:
        if (w == mot):
            li[mot,d] = freq[w, d]
        
    li=set(li)
    return li


def myMax(freq):
    maxi = {}
    for (w, d) in freq:
        if (w not in maxi):
            maxi[w] = freq[w, d]
        else:
            if (maxi[w] < freq[w, d]):
                maxi[w] = freq[w, d]
    return maxi


def ni(freq):
    ni = {}
    for (w1, d1) in freq:
        if (w1 not in ni):
            ni[w1] = 1
        else:
            ni[w1] += 1
    return ni

def N():
    return 4

#Retourne un dictionnaire contenant (terme, numéroDuFichier):poids
def tfIdf(freq):
    poids = {}
    for (w, d) in freq:
        poids[w, d] = (freq[w, d] / myMax(freq)[w]) * log10((N() / ni(freq)[w]) + 1)
    return poids


print("**************************ponderation TF*IDF*************************")


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


requete = "hiba and ryma or dahmani"
listR = requete.split()