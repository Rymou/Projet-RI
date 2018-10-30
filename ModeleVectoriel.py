from string import *
from math import *
import TransformationsMethodes as trM 


def requestTransform(requete, docNumber):
    fichierInverse = trM.fichierInverse()
    re = requete.split(" ")
    print(re)
    newRequest = []
    for (k, v) in fichierInverse.items():
        if (k[1] == docNumber):
            if (k[0] in re):
                newRequest.append(1)
            else:
                newRequest.append(0)
        else:
            newRequest.append(0)
    print(fichierInverse)
    print(len(newRequest))
    print(len(fichierInverse))
    print(newRequest)
    return newRequest


def QueryVector():
    fichierInverse = trM.fichierInverse()
    #listq=requete.split(" ")
    motUnique=[]
    vector={}
    vectors=[]
    for fi,k in fichierInverse.items():
        motUnique.append(fi[0])
    motUnique = set(motUnique)
    poids = trM.tfIdf(fichierInverse)
    for i in range(1,trM.N()+1):
        poidsDoc = {}
        vector = {}
        for k,v in poids.items():
            if k[1] == i:
                poidsDoc[k[0]]=v
        for word in motUnique:
            if word in poidsDoc:
                vector[word]=poidsDoc[word]
            else:
                vector[word]=0
        #print("this is vector"+str(i))

        #print(vector)
        vectors.append(vector)
    #print(motUnique)
    #print(len(motUnique))
    #print("Poiiiiiiiiids doooooooc")
    #print(len(vectors[1]))
    #print(vectors[1])
    return vectors

def transformationRequete(requete):
    requeteList = requete.split(" ")
    vector = QueryVector()[0]
    requeteTransformee = {}
    for word in vector:
        if word in requeteList:
            requeteTransformee[word] = 1
        else: 
            requeteTransformee[word] = 0
    return requeteTransformee

def ModeleVectoriel(requete, numDoc,formule):
    #fichierInverse = trM.fichierInverse()
    requteL=requete.split(" ")
    requeteTransformee = transformationRequete(requete)
    print("Requeeeeete == ")
    print(requeteTransformee)

    vector=QueryVector()[numDoc-1]
    print("Vectooooooor du document1 == ")
    print(vector)

    q=[]
    for word in vector:
        if(word in requteL):
            q.append(1)
        else:
            q.append(0)

    sim = 0
    i = 0

    if(formule == 'Produit Interne'):
        for k, v in vector.items():
            sim = sim + (v * requeteTransformee[k])
            i = i + 1
        #print("Le produit interne == ", sim)

    if(formule=="Coef de Dice"):
        simR=0
        simF=0
        for k, v in vector.items():
            sim = sim + (v * requeteTransformee[k])
            simR = simR + requeteTransformee[k] * requeteTransformee[k]
            simF = simF + v * v
            i = i + 1
        sim = (sim*2) / (simR+simF)
        #print("Le Coef de Dice == ", sim)

    if(formule=="Cosinus"):
        simR = 0
        simF = 0

        for k, v in vector.items():
            print(i)
            sim = sim + (v * requeteTransformee[k])
            simR = simR + requeteTransformee[k] * requeteTransformee[k]
            simF = simF + v * v
            i = i + 1
        sim = sim  / sqrt(simR + simF)
        #print("Le Cosinus == ",sim)

    if(formule=='Jaccard'):
        simR = 0
        simF = 0

        for k, v in vector.items():
            sim = sim + (v * requeteTransformee[k])
            simR = simR + requeteTransformee[k] * requeteTransformee[k]
            simF = simF + v * v
            i = i + 1
        sim = sim / ((simR + simF)-sim)
        #print("Jaccad == ",sim)
    return sim
        
print("Resultaaaaaaaaaaaat")
print(ModeleVectoriel('hiba of ryma',1,'Coef de Dice'))