from string import *
from math import *
import TransformationsMethodes as trM 


def requestTransform(requete, docNumber):
    fichierInverse = trM.fichierInverse()
    re = requete.split(" ")
    newRequest = []
    for (k, v) in fichierInverse.items():
        if (k[1] == docNumber):
            if (k[0] in re):
                newRequest.append(1)
            else:
                newRequest.append(0)
        else:
            newRequest.append(0)
    return newRequest


def QueryVector():
    fichierInverse = trM.fichierInverse()
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
        vectors.append(vector)
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
    requteL=requete.split(" ")
    requeteTransformee = transformationRequete(requete)
    vector=QueryVector()[numDoc-1]
    q=[]
    for word in vector:
        if(word in requteL):
            q.append(1)
        else:
            q.append(0)

    sim = 0
    i = 0
    poids=trM.tfIdf(trM.fichierInverse())
    if(formule == 'Produit Interne'):
        sim = 0
        for word in requteL:
           for k, v in poids:
                if word==k and v==numDoc:
                    sim = sim + poids[k,v]
    if(formule=="Coef de Dice"):
        sim = 0
        simR=0
        simF=0
        simF=len(requteL)
        for k, v in poids:
            if k in requteL and v==numDoc:
                sim = sim + poids[k,v]
                simF = simF + pow(poids[k,v],2)
            elif v==numDoc:
                simF = simF + pow(poids[k, v], 2)
            i = i + 1
        if simF==0:
            sim = 0
        else:
            sim = (sim*2) / (simF)
    if(formule=="Cosinus"):
        sim = 0
        simR = 0
        simF = len(requteL)

        for k, v in poids:
            if k in requteL and v==numDoc:
                sim = sim + poids[k,v]
                simR = simR + pow(poids[k,v],2)
           # elif v==numDoc:
               # simR = simR + pow(poids[k, v], 2)
        if(simR*simF==0):
            sim=0
        else:
            sim = sim  / sqrt(simR * simF)
    if(formule=='Jaccard'):
        sim = 0
        simR = 0
        simF = len(requteL)
        for k, v in poids:
            if k in requteL and v==numDoc:
                print("the k : "+k+"  the v : "+str(v))
                sim = sim + poids[k,v]
                print("sim :"+str(sim))
                simR = simR + pow(poids[k,v],2)
                print("simR : "+str(simR))
            elif v==numDoc:
                simR = simR + pow(poids[k, v], 2)
        print("mul"+ str(simR*simF))
        numerateur = simR + simF - sim
        if(numerateur==0):
            numerateur=0
        else:
            sim = sim / numerateur
    return sim
        

print(ModeleVectoriel('information recherche module',1,'Jaccard'))
