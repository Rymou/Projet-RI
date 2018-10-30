import TransformationsMethodes as trM 
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import RegexpTokenizer

def ModelBooleen(requete):
    tknzr = RegexpTokenizer('[A-Za-z]\w+')
    freq =  trM.fichierInverse()
    #listR = requete.split()
    listR = tknzr.tokenize(requete)
    lisDoc=[]
    numDoc=1
    i = 0
    listOp = ['and','or','not','(',')']
    newList=[]
    
    while(numDoc<trM.N()):
        newList = []
        for word in listR:
            if(word not in listOp):
               # print("1")
                if(word,numDoc) in freq:
                    if(freq[word,numDoc]):
                        newList.append("1")
                    else:
                        newList.append("0")
                else:
                    newList.append("0")
            else:
                newList.append(word)
        print("Document numero"+str(numDoc))
        print(newList)
        
        string = (" ").join(newList)
        if(eval(string)):
            lisDoc.append(numDoc)
        numDoc +=1
    print("lisDoc ")
    print(lisDoc)   
    return lisDoc


print(ModelBooleen("hiba and ryma or dahmani"))
