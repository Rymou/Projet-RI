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
        self.ComboBMV.addItems(["","Produit Interne", "Coef de Dice", "Cosinus", "Jaccard"])
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(380, 30, 101, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(160, 140, 51, 21))
        self.label_3.setObjectName("label_3")
        self.BEnvoyerMV = QtWidgets.QPushButton(self.tab_2)
        self.BEnvoyerMV.setGeometry(QtCore.QRect(590, 200, 75, 23))
        self.BEnvoyerMV.setObjectName("BEnvoyerMV")
        self.BEnvoyerMV.clicked.connect(self.evalVectoriel)
        self.ListeResu = QtWidgets.QListView(self.tab_2)
        self.ListeResu.setGeometry(QtCore.QRect(90, 240, 571, 241))
        self.ListeResu.setObjectName("ListeResu")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(30, 30, 101, 21))
        self.label_4.setObjectName("label_4")
        self.ComboBMV_2 = QtWidgets.QComboBox(self.tab_2)
        self.ComboBMV_2.setGeometry(QtCore.QRect(150, 30, 151, 31))
        self.ComboBMV_2.setObjectName("ComboBMV_2")
        self.ComboBMV_2.addItems(["","1", "2", "3", "4"])
        self.ListViewMV.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.ListViewMV.addTab(self.tab_4, "")
        self.BOkDemarrer.clicked.connect(self.get_term)
        self.gridLayout.addWidget(self.ListViewMV, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.BOuvrirDoc.clicked.connect(self.openFile)
        self.BEnvoyerReqB.clicked.connect(self.evalBoolean)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.ListViewMV.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def evalVectoriel(self):
        requete = self.TEditReqMV.toPlainText()
        formule = self.ComboBMV.currentText()
        numDoc = self.ComboBMV_2.currentText()
        sim = mv.ModeleVectoriel(requete,int(numDoc),formule)
        model = QtGui.QStandardItemModel()
        self.ListeResu.setModel(model)
        StringSim = "Resultat pour la formule : "+formule+" dans le document "+str(numDoc)+" == "+str(sim)
        simDocQ = QtGui.QStandardItem(StringSim)
        model.appendRow(simDocQ)
        print("finitooooooooooo et sim == ", sim)




    def evalBoolean(self):
        string = self.tEditReqB.toPlainText()
        lis = mb.ModelBooleen(string)
        model = QtGui.QStandardItemModel()
        self.ListeViewMB.setModel(model)
        for k in lis:
            resultat = "Requete satisfaite dans le document :  "+str(k)
            item = QtGui.QStandardItem(resultat)
            model.appendRow(item)

    def get_term(self):
        term=self.TEditTerme.toPlainText()
        fichierInverse = trM.fichierInverse()
        li = trM.indexMot(fichierInverse,term)
        model = QtGui.QStandardItemModel()
        self.ListRTerme.setModel(model)
        if(len(li)==0):
            item = QtGui.QStandardItem("Le terme : "+term+" n'existe dans aucun document")
            model.appendRow(item)
        else:
            for k ,v in li:
                item = QtGui.QStandardItem("Le terme : "+term+" apparait dans le fichier : "+str(v))
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
                print("liiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
                print(li)
                model = QtGui.QStandardItemModel()
                self.ListeRDoc.setModel(model)
                document = "************** Document "+str(numDoc)+" **************"
                item = QtGui.QStandardItem(document)
                model.appendRow(item)
                for k ,v in li.items():
                    it = k+ " , "+str(v)+" : "+str(tf[k,numDoc])
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
        self.label_4.setText(_translate("MainWindow", "Choix du document"))
        self.ListViewMV.setTabText(self.ListViewMV.indexOf(self.tab_2), _translate("MainWindow", "Modele Vectoriel"))
        self.ListViewMV.setTabText(self.ListViewMV.indexOf(self.tab_4), _translate("MainWindow", "Modele Probabiliste"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())