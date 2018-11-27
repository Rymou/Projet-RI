from math import *
import ModeleVectoriel as mv
import TransformationsMethodes as trM
#ri = nombre de docs pertinents contenant ti
#ni = nombre de docs contenant ti
#R = nombre de docs pertinents
#N = nombre de docs de la collection


def nombreDeDocsContenantTerme(terme):
    freq = trM.fichierInverse()
    nombreDoc = []
    for (w,d) in freq:
        if w == terme:
            nombreDoc.append(d)
    return set(nombreDoc)


def nombreDeDocsPertinentContenantTerme(terme,doc):
    freq = trM.fichierInverse()
    nombreDoc = []
    for (w,d) in freq:
        if w == terme:
            if d in doc:
                nombreDoc.append(d)
    return set(nombreDoc)


def modeleProbabiliste(requete,listDoc):
    freq = trM.tfIdf(trM.fichierInverse())
    listRequete = requete.split()
    requeteTransformee = mv.transformationRequete(requete)
    N = trM.N()
    R = len(listDoc)
    dict={}
    for d in range(1,N+1):
        somme = 0
        for word in listRequete:
            ni=len(nombreDeDocsContenantTerme(word))
            ri = len(nombreDeDocsPertinentContenantTerme(word,listDoc))
            form = ((ri + 0.5) / (R - ri + 0.5)) / ((ni - ri + 0.5) /(N - ni - R + ri + 0.5))
            try:
                somme = somme+freq[word,d]*log10(form)
            except KeyError as error:
                continue

        dict[d]=somme
    return dict

print(modeleProbabiliste("information recherche module",[1,3]))
