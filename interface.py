# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#from PyQt5.QtWidgets import QWidget
#import UserInterface
import os
import sys
import TransformationsMethodes as trM 
import ModeleBooleen as mb
import ModeleVectoriel as mv
import ModeleProbabiliste as mp
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.ListViewMV = QtWidgets.QTabWidget(self.centralwidget)
        self.ListViewMV.setObjectName("ListViewMV")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.TEditTerme = QtWidgets.QTextEdit(self.tab)
        self.TEditTerme.setGeometry(QtCore.QRect(40, 30, 201, 41))
        self.TEditTerme.setObjectName("TEditTerme")
        self.BOkDemarrer = QtWidgets.QPushButton(self.tab)
        self.BOkDemarrer.setGeometry(QtCore.QRect(160, 80, 81, 31))
        self.BOkDemarrer.setObjectName("BOkDemarrer")
        self.ListRTerme = QtWidgets.QListView(self.tab)
        self.ListRTerme.setGeometry(QtCore.QRect(40, 150, 201, 331))
        self.ListRTerme.setObjectName("ListRTerme")
        self.OTEditOuvrirDocument = QtWidgets.QTextEdit(self.tab)
        self.OTEditOuvrirDocument.setGeometry(QtCore.QRect(310, 30, 431, 41))
        self.OTEditOuvrirDocument.setReadOnly(True)
        self.OTEditOuvrirDocument.setObjectName("OTEditOuvrirDocument")
        self.BOuvrirDoc = QtWidgets.QPushButton(self.tab)
        self.BOuvrirDoc.setGeometry(QtCore.QRect(670, 90, 75, 31))
        self.BOuvrirDoc.setObjectName("BOuvrirDoc")
        self.ListeRDoc = QtWidgets.QListView(self.tab)
        self.ListeRDoc.setGeometry(QtCore.QRect(310, 150, 431, 331))
        self.ListeRDoc.setObjectName("ListeRDoc")
        self.ListViewMV.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tEditReqB = QtWidgets.QTextEdit(self.tab_3)
        self.tEditReqB.setGeometry(QtCore.QRect(230, 30, 431, 41))
        self.tEditReqB.setObjectName("tEditReqB")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(100, 40, 101, 21))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.BEnvoyerReqB = QtWidgets.QPushButton(self.tab_3)
        self.BEnvoyerReqB.setGeometry(QtCore.QRect(580, 100, 75, 31))
        self.BEnvoyerReqB.setObjectName("BEnvoyerReqB")
        self.ListeViewMB = QtWidgets.QListView(self.tab_3)
        self.ListeViewMB.setGeometry(QtCore.QRect(90, 170, 571, 261))
        self.ListeViewMB.setObjectName("ListeViewMB")
        self.ListViewMV.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.TEditReqMV = QtWidgets.QTextEdit(self.tab_2)
        self.TEditReqMV.setGeometry(QtCore.QRect(230, 130, 431, 41))
        self.TEditReqMV.setObjectName("TEditReqMV")
        self.ComboBMV = QtWidgets.QComboBox(self.tab_2)
        self.ComboBMV.setGeometry(QtCore.QRect(508, 30, 151, 31))
        self.ComboBMV.setObjectName("ComboBMV")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(380, 30, 101, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(160, 140, 51, 21))
        self.label_3.setObjectName("label_3")
        self.BEnvoyerMV = QtWidgets.QPushButton(self.tab_2)
        self.BEnvoyerMV.setGeometry(QtCore.QRect(590, 200, 75, 23))
        self.BEnvoyerMV.setObjectName("BEnvoyerMV")
        self.ListeResu = QtWidgets.QListView(self.tab_2)
        self.ListeResu.setGeometry(QtCore.QRect(90, 240, 571, 241))
        self.ListeResu.setObjectName("ListeResu")
        self.ListViewMV.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.RequeteEntry = QtWidgets.QTextEdit(self.tab_4)
        self.RequeteEntry.setGeometry(QtCore.QRect(140, 110, 521, 51))
        self.RequeteEntry.setObjectName("RequeteEntry")
        self.Bvect = QtWidgets.QPushButton(self.tab_4)
        self.Bvect.setGeometry(QtCore.QRect(490, 410, 101, 23))
        self.Bvect.setObjectName("Bvect")
        self.vectCombo = QtWidgets.QComboBox(self.tab_4)
        self.vectCombo.setGeometry(QtCore.QRect(490, 380, 101, 22))
        self.vectCombo.setObjectName("vectCombo")
        self.Bproba = QtWidgets.QPushButton(self.tab_4)
        self.Bproba.setGeometry(QtCore.QRect(210, 390, 101, 23))
        self.Bproba.setObjectName("Bproba")
        self.probaList = QtWidgets.QListView(self.tab_4)
        self.probaList.setGeometry(QtCore.QRect(140, 180, 241, 192))
        self.probaList.setObjectName("probaList")
        self.vectorList = QtWidgets.QListView(self.tab_4)
        self.vectorList.setGeometry(QtCore.QRect(420, 180, 241, 192))
        self.vectorList.setObjectName("vectorList")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_4)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 190, 101, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkDoc1 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkDoc1.setObjectName("checkDoc1")
        self.verticalLayout.addWidget(self.checkDoc1)
        self.checkDoc2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkDoc2.setObjectName("checkDoc2")
        self.verticalLayout.addWidget(self.checkDoc2)
        self.checkDoc3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkDoc3.setObjectName("checkDoc3")
        self.verticalLayout.addWidget(self.checkDoc3)
        self.checkDoc4 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkDoc4.setObjectName("checkDoc4")
        self.verticalLayout.addWidget(self.checkDoc4)
        self.choisirDoc = QtWidgets.QLabel(self.tab_4)
        self.choisirDoc.setGeometry(QtCore.QRect(20, 140, 101, 31))
        self.choisirDoc.setObjectName("choisirDoc")
        self.LabRequete = QtWidgets.QLabel(self.tab_4)
        self.LabRequete.setGeometry(QtCore.QRect(360, 80, 51, 20))
        self.LabRequete.setObjectName("LabRequete")
        self.ListViewMV.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.ListViewMV, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.BEnvoyerMV.clicked.connect(self.evalVectoriel)
        self.BOkDemarrer.clicked.connect(self.get_term)
        self.ComboBMV.addItems(["", "Produit Interne", "Coef de Dice", "Cosinus", "Jaccard"])
        self.vectCombo.addItems(["", "Produit Interne", "Coef de Dice", "Cosinus", "Jaccard"])
        self.BOuvrirDoc.clicked.connect(self.openFile)
        self.BEnvoyerReqB.clicked.connect(self.evalBoolean)
        self.Bvect.clicked.connect(self.evalVectoriel2)
        self.Bproba.clicked.connect(self.evalProba)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.ListViewMV.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def evalProba(self):
        listDocs=[]
        checkBoxList = self.verticalLayoutWidget.findChildren(QtWidgets.QCheckBox)
        #print(checkBoxList)
        for loop in range(len(checkBoxList)):
                if checkBoxList[loop].isChecked():
                    #listDocs.append(checkBoxList[loop])
                    listDocs.append(int(checkBoxList[loop].text()[len(checkBoxList[loop].text())-1]))
        requete = self.RequeteEntry.toPlainText()
        requete = trM.cleanQuery(requete)
        res = mp.modeleProbabiliste(requete,listDocs)
        model = QtGui.QStandardItemModel()
        self.probaList.setModel(model)
        print("here")
        for (k,v) in res.items():
            print("key"+str(k)+" value "+str(v))
            StringSim = "Document "+str(k)+" == "+str(v)
            simDocQ = QtGui.QStandardItem(StringSim)
            model.appendRow(simDocQ)
    def evalVectoriel(self):
        requete = self.TEditReqMV.toPlainText()
        requete = trM.cleanQuery(requete)
        formule = self.ComboBMV.currentText()
        model = QtGui.QStandardItemModel()
        self.ListeResu.setModel(model)
        for doc in range(1,trM.N()+1):
            sim = mv.ModeleVectoriel(requete,doc,formule)
            StringSim = "Resultat pour la formule : "+formule+" dans le document "+str(doc)+" == "+str(sim)
            simDocQ = QtGui.QStandardItem(StringSim)
            model.appendRow(simDocQ)
    def evalVectoriel2(self):
        requete = self.RequeteEntry.toPlainText()
        requete = trM.cleanQuery(requete)
        formule = self.vectCombo.currentText()
        model = QtGui.QStandardItemModel()
        self.vectorList.setModel(model)
        for doc in range(1,trM.N()+1):
            sim = mv.ModeleVectoriel(requete,doc,formule)
            StringSim = "Document "+str(doc)+" == "+str(sim)
            simDocQ = QtGui.QStandardItem(StringSim)
            model.appendRow(simDocQ)




    def evalBoolean(self):
        string = self.tEditReqB.toPlainText()
        string = trM.cleanQuery(string)
        lis = mb.ModelBooleen(string)
        model = QtGui.QStandardItemModel()
        self.ListeViewMB.setModel(model)
        if len(lis)==0:
            resultat = "Aucun document ne satisfait la requete"
            item = QtGui.QStandardItem(resultat)
            model.appendRow(item)
        else:
            for k in lis:
                resultat = "Requete satisfaite dans le document :  "+str(k)
                item = QtGui.QStandardItem(resultat)
                model.appendRow(item)

    def get_term(self):
        term=self.TEditTerme.toPlainText()
        fichierInverse = trM.fichierInverse()
        print(fichierInverse)
        poid=trM.tfIdf(fichierInverse)
        term = trM.cleanQuery(term)
        li = trM.indexMot(fichierInverse,term)
        print(li)
        model = QtGui.QStandardItemModel()
        self.ListRTerme.setModel(model)
        if(len(li)==0):
            item = QtGui.QStandardItem("Le terme : "+term+" n'existe dans aucun document")
            model.appendRow(item)
        else:
            for k ,v in li:
                item = QtGui.QStandardItem("Doc :"+str(v)+" poid :"+str(poid[k,v]))
                model.appendRow(item)

        

    def openFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","All Files (*);;Text Files (*.txt)", options=options)

        if fileName:
            model = QtGui.QStandardItemModel()
            model.removeRows( 0, model.rowCount())
            fichierInverse = trM.fichierInverse()
            tf = trM.tfIdf(fichierInverse)
            self.OTEditOuvrirDocument.setText(fileName)
            string=fileName.split("/")
            f=string[-1]
            fN=f.split(".")
            if(fN[1]=="txt"):
                fichier=fN[0]
                #print(tf)
                numDoc=int(fichier[1])
                li = trM.indexDoc(fichierInverse,numDoc)
                model = QtGui.QStandardItemModel()
                self.ListeRDoc.setModel(model)
                document = "************** Document "+str(numDoc)+" **************"
                item = QtGui.QStandardItem(document)
                model.appendRow(item)
                for k ,v in li.items():
                    it = k+ " : "+str(tf[k,numDoc])
                    #it = k+" : "+str(v)+" ==> poids : " + str(tf[k,numDoc])
                    item = QtGui.QStandardItem(it)
                    model.appendRow(item)
                return fileName
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BOkDemarrer.setText(_translate("MainWindow", "Ok"))
        self.BOuvrirDoc.setText(_translate("MainWindow", "Ouvrir"))
        self.ListViewMV.setTabText(self.ListViewMV.indexOf(self.tab), _translate("MainWindow", "Demarrer"))
        self.label.setText(_translate("MainWindow", "Requete booleenne"))
        self.BEnvoyerReqB.setText(_translate("MainWindow", "Envoyer"))
        self.ListViewMV.setTabText(self.ListViewMV.indexOf(self.tab_3), _translate("MainWindow", "Modele Booleen"))
        self.label_2.setText(_translate("MainWindow", "Choix de la formule"))
        self.label_3.setText(_translate("MainWindow", "Requete"))
        self.BEnvoyerMV.setText(_translate("MainWindow", "Envoyer"))
        self.ListViewMV.setTabText(self.ListViewMV.indexOf(self.tab_2), _translate("MainWindow", "Modele Vectoriel"))
        self.Bvect.setText(_translate("MainWindow", "Vectorial Score"))
        self.Bproba.setText(_translate("MainWindow", "Probabilistic Score"))
        self.checkDoc1.setText(_translate("MainWindow", "Doc 1"))
        self.checkDoc2.setText(_translate("MainWindow", "Doc 2"))
        self.checkDoc3.setText(_translate("MainWindow", "Doc 3"))
        self.checkDoc4.setText(_translate("MainWindow", "Doc 4"))
        self.choisirDoc.setText(_translate("MainWindow", "choisir un document"))
        self.LabRequete.setText(_translate("MainWindow", "REQUETE"))
        self.ListViewMV.setTabText(self.ListViewMV.indexOf(self.tab_4), _translate("MainWindow", "Modele Probabiliste"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
