from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMenuBar, QAction
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor, QPixmap
import subprocess
import os
import sys
import time, random

def toggle_developer_mode():
    if developer_mode_action.isChecked():
        print("Developer Mode Enabled")
        sourcecode.setReadOnly(False)
    else:
        print("Developer Mode Disabled")
        sourcecode.setReadOnly(True)
    
def buildpy():
    buildpy = QNewWindow()
    buildpy.setWindowTitle("Build Python File")
    buildpy.setFixedSize(300, 150)

    timer = QtCore.QTimer()
    timer.setInterval(20)

    def startbuild():
        rndnum = random.randint(192, 3029372)
        code = sourcecode.toPlainText()
        btnbuild.setDisabled(True)
        btncheck.setDisabled(True)
        def update_progress():
            current_value = prgloadbuild.value()
            st = lbl1.setText
            if current_value < 100:
                prgloadbuild.setValue(current_value + 1)  # Increment the progress
                
            else:
                timer.stop()  # Stop the timer when 100% is reached
            if current_value == 5:
                st("Building Data")
            if current_value == 30:
                st("Getting Vars")
            if current_value == 35:
                st("Collect Vars System")
            if current_value == 36:
                st("GetWINDOWS")
            if current_value == 37:
                st("WindowTitle")
            if current_value == 38:
                st("WindowIcons")
            if current_value == 39:
                st("WindowFixedSize")
            if current_value == 40:
                st("WindowHeight")
            if current_value == 41:
                st("WindowWidth")
            if current_value == 42:
                st("exec_ Checker")
            if current_value == 60:
                st("Load src_1_data") 
            if current_value == 62:
                st("Load src_2_data")
            if current_value == 63:
                st("Load src_3_data")
            if current_value == 64:
                st("Load src_4_data")
            if current_value == 65:
                st("Widgets Loader")
            if current_value == 66:
                st("Public Loader")
            if current_value == 67:
                st("Paths (InVAR)")
            if current_value == 68:
                st("Load Images")
            if current_value == 69:
                st("QNEW.a(1)")
            if current_value == 81:
                st("Load Imports")
            if current_value == 90:
                st("Sys python QApp")
            if current_value == 92:
                st("Ready..DLLs(Py)")
            if current_value > 100 or current_value == 100:
                st("Done..")
                with open(f'PyQt5_ITRone{rndnum}.py', 'w') as file:
                    file.write(f'{code}\n')


        timer.timeout.connect(update_progress)
        timer.start()  # Start the timer

    def run_codecheck(self):
        # Get text from QTextEdit
        text = sourcecode.toPlainText()
        # Write the text to prj.py
        with open("prj.py", "w") as file:
            file.write(text)
        print("Text saved to prj.py")
        time.sleep(1)
        try:
            result = subprocess.run(["python", "prj.py"], check=True, capture_output=True, text=True)
            print("Output:", result.stdout)
            np = QMessageBox()
            np.setText("Your Applaction has no problem!")
            np.setWindowIcon(ico(IDEicons+"appicon.png"))
            np.setIconPixmap(QPixmap("IDE/icons/truetick.png"))
            np.show()
            np.exec_()   
        except subprocess.CalledProcessError as e:
            print("Error:", e.stderr)
            errordialog = QMessageBox()
            errordialog.setWindowTitle("Error SourceCode")
            errordialog.setText(e.stderr)
            errordialog.setWindowIcon(ico(IDEicons+"appicon.png"))
            errordialog.setIcon(QMessageBox.Critical)
            MsgCopyButton = errordialog.addButton("Copy", QMessageBox.ActionRole)
            errordialog.setStandardButtons(QMessageBox.Ok)
            
            errordialog.show()
            errordialog.exec_()

            response = errordialog.clickedButton()
            if response == errordialog.button(QMessageBox.Ok):
                print("OK clicked")
            elif response == MsgCopyButton:
                # Copy error message to clipboard
                clipboard = QApplication.clipboard()
                error_message = errordialog.text()
                clipboard.setText(error_message)


    btncheck = QPushButton("Check", buildpy)
    btncheck.clicked.connect(run_codecheck)
    btnbuild = QPushButton("Build", buildpy)
    btnbuild.clicked.connect(startbuild)
    btnbuild.move(0, 30)



    prgloadbuild = QProgressBar(buildpy)
    prgloadbuild.move(50, 70)
    prgloadbuild.resize(230, 20)
    prgloadbuild.setValue(0)

    lbl1 = QLabel("R: Type <b>(PyQt5)<\b>", buildpy)
    lbl1.move(100, 95)


    windows.append(buildpy)
    buildpy.show()
    
###

listvars = []
testfile = "prj.py"
created_widgets = {}
windows = []
ico = QtGui.QIcon
Qw = QtWidgets
QNewWindow = QtWidgets.QWidget
editWindows = []
#Functions -----------------------------------------------------------------------------
def create_window():
    cw = QNewWindow()
    cw.setFixedSize(300, 200)
    cw.setWindowTitle("Create Window")
    cw.setWindowIcon(ico(IDEicons+"create_window.png"))

    lbl1 = QLabel(parent=cw, text="Window ID :")
    lbl1.move(0, 3)
    ety1 = QLineEdit(parent=cw)
    ety1.move(65,0)
    ety1.setText("window")

    lbl2 = QLabel(parent=cw, text="Window Title :")
    lbl2.move(0, 33)
    ety2 = QLineEdit(parent=cw)
    ety2.move(75,30)
    ety2.setText("Python - ITRone")

    lbl3 = QLabel(parent=cw, text="Window Height:")
    lbl3.move(0, 63)
    ety3 = QLineEdit(parent=cw)
    ety3.resize(65, 20)
    ety3.move(80,60)
    ety3.setText("400")

    lbl4 = QLabel(parent=cw, text="Width:")
    lbl4.move(150, 63)
    ety4 = QLineEdit(parent=cw)
    ety4.resize(65, 20)
    ety4.move(190,60)
    ety4.setText("600")

    cb1 = QCheckBox(parent=cw, text="Use FixedSize")
    cb1.move(0, 85)
    cb1.setChecked(True)

    cb2 = QCheckBox(parent=cw, text="Set as Editor Window")
    cb2.setToolTip("Using Size to Editor Window")
    cb2.setChecked(True)
    cb2.move(110, 85)

    lbl5 = QLabel(parent=cw, text="Window Icon:")
    lbl5.move(5, 113)
    ety5 = QLineEdit(parent=cw)
    ety5.move(75, 110)
    ety5.resize(158, 20)
    ety5.setText('IDE\\icons\\example.png')
    
    def add_window():
        wicon = ety5.text()
        wid = ety1.text()
        wh = ety3.text()
        ww = ety4.text()
        wtitle = ety2.text()
        cb1ch = cb1.isChecked()
        cb2ch = cb2.isChecked()
        if cb1ch == False and wid and ww and wh and int(ww) < 601 and int(wh) < 701:
            sourcecode.append("\n\napp = QtWidgets.QApplication(sys.argv)")
            sourcecode.append(f"{wid} = QtWidgets.QWidget()")
            sourcecode.append(f"{wid}.resize({int(ww)}, {int(wh)})")
            sourcecode.append(f"{wid}.setWindowTitle('{wtitle}')")
            sourcecode.append(f"{wid}.setWindowIcon(QtGui.QIcon('{wicon}'))")
            editWindows.append(str(wid))
            if cb2ch == True:
                Editor.setFixedSize(int(ww), int(wh))
            cw.close()
        elif cb1ch == True and wid and ww and wh and int(ww) < 601 and int(wh) < 701:
            sourcecode.append("\n\napp = QtWidgets.QApplication(sys.argv)")
            sourcecode.append(f"{wid} = QtWidgets.QWidget()")
            sourcecode.append(f"{wid}.setFixedSize({int(ww)}, {int(wh)})")
            sourcecode.append(f"{wid}.setWindowTitle('{wtitle}')")
            sourcecode.append(f"{wid}.setWindowIcon(QtGui.QIcon('{wicon}'))")
            editWindows.append(str(wid))
            cw.close()
            if cb2ch == True:
                Editor.setFixedSize(int(ww), int(wh))


    btn1 = QPushButton(parent=cw, text="Apply")
    btn1.move(110, 150)
    btn1.clicked.connect(add_window)

    
    cw.show()


    windows.append(cw)
def end_window():
    ew = QNewWindow()
    ew.setFixedSize(300, 200)
    ew.setWindowTitle("End Window")
    ew.setWindowIcon(ico(IDEicons+"end_window.png"))

    lbl1 = QLabel(parent=ew, text="Choose Window:")
    lbl1.move(10, 13)

    cbx1 = QComboBox(parent=ew)
    cbx1.addItems(editWindows)
    cbx1.resize(100, 20)
    cbx1.move(100, 10)

    def end_window_apply():
        wcbx = cbx1.currentText()
        sourcecode.append(f"\n\n\n\n\n{wcbx}.show()\napp.exec_()")

    btn1 = QPushButton(parent=ew, text="Apply")
    btn1.move(110, 150)
    btn1.clicked.connect(end_window_apply)

    windows.append(ew)
    ew.show() 
def import_lib():
    cursor = QTextCursor(sourcecode.document())
    if developer_mode_action.isChecked():
        il = QNewWindow()
        il.setFixedSize(360, 200)
        il.setWindowTitle("Import")
        il.setWindowIcon(ico(IDEicons+"lib.png"))

        def importlibnow():
            i1 = cb1_1.isChecked()
            f1 = cb2_1.isChecked()
            i2 = cb1_2.isChecked()
            name1 = lib1.text()
            name2 = lib2.text()
            cursor.setPosition(0)
            sourcecode.setTextCursor(cursor)
            if i1 == True and f1 == False and i2 == False and name1:
                sourcecode.insertPlainText(f'import {name1}\n')
            elif i1 == False and f1 == True and i2 == True and name1 and name2:
                sourcecode.insertPlainText(f'from {name1} import {name2}\n')

        def checker():
            i1 = cb1_1.isChecked()
            f1 = cb2_1.isChecked()
            i2 = cb1_2.isChecked()
            if i1 == True:
                cb1_2.setDisabled(True)
                lib2.setDisabled(True)
                cb1_2.setChecked(False)
            else:
                cb1_2.setDisabled(False)
                lib2.setDisabled(False)
        
        cb1_1 = QRadioButton(parent=il, text="Import")
        cb1_1.move(20, 50)
        cb1_1.clicked.connect(checker)

        cb2_1 = QRadioButton(parent=il, text="From")
        cb2_1.move(20, 75)
        cb2_1.clicked.connect(checker)

        cb1_2 = QRadioButton(parent=il, text="Import")
        cb1_2.move(170, 65)

        lib1 = QLineEdit(parent=il)
        lib1.move(80, 65)
        lib1.resize(80, 20)

        lib2 = QLineEdit(parent=il)
        lib2.move(230, 65)
        lib2.resize(80, 20)

        gp1 = QButtonGroup(parent=il)
        gp1.addButton(cb1_1)
        gp1.addButton(cb2_1)

        btn1 = QPushButton(parent=il, text="Import")
        btn1.move(110, 170)
        btn1.clicked.connect(importlibnow)

        windows.append(il)
        il.show()
    else:
        info21 = QMessageBox()
        info21.setWindowTitle("Developer")
        info21.setText("This is for Developer Mode only \n Go to Source Code and Enable it")
        info21.setIcon(QMessageBox.Warning)
        info21.setWindowIcon(ico(IDEicons+"infoerrorwarn.png"))
        info21.show()
        info21.exec_()  
def create_var():

    if developer_mode_action.isChecked():
        cv = QNewWindow()
        cv.setFixedSize(300, 200)
        cv.setWindowTitle("New Varibale")
        cv.setWindowIcon(ico(IDEicons+"var.png"))

        def doandknow():
            getType = cbx.currentText()
            if getType == "Number":
                print("num")
                etynum.show()
                etybool.hide()
                etystr.hide()
                etynamelist.hide()
                btndellist.hide()
                btnaddlist.hide()
                etylist.hide()
            elif getType == "String":
                print("str")
                etynum.hide()
                etybool.hide()
                etystr.show()
                etynamelist.hide()
                btndellist.hide()
                btnaddlist.hide()
                etylist.hide()
            elif getType == "Boolen":
                print("bool")
                etybool.show()
                etynum.hide()
                etystr.hide()
                etynamelist.hide()
                btndellist.hide()
                btnaddlist.hide()
                etylist.hide()
            elif getType == "List":
                print("list")
                etynamelist.show()
                btndellist.show()
                btnaddlist.show()
                etylist.show()
                etynum.hide()
                etystr.hide()
                etybool.hide()

        def addtolist():
            itemname = etynamelist.text()
            etylist.addItem(itemname)

        def deltolist():
            etylist.clear()
                

        rd1 = QRadioButton(parent=cv, text="Global")
        rd1.move(0, 0)

        rd2 = QRadioButton(parent=cv, text="Local")
        rd2.move(0, 20)
        rd2.setChecked(True)

        cbx = QComboBox(parent=cv)
        cbx.addItems(["Number", "String", "Boolen"])
        cbx.move(0, 65)
        cbx.currentTextChanged.connect(doandknow)

        ety1 = QLineEdit(parent=cv)
        ety1.setPlaceholderText("Var Name")
        ety1.resize(70, 20)
        ety1.show()
        ety1.move(0, 40)

        etynum = QLineEdit(parent=cv)
        etynum.setPlaceholderText("Value")
        etynum.resize(70, 20)
        etynum.move(100, 40)

        etystr = QLineEdit(parent=cv)
        etystr.setPlaceholderText("String")
        etystr.resize(70, 20)
        etystr.hide()
        etystr.move(100, 40)

        etybool = QComboBox(parent=cv)
        etybool.addItems(["True", "False"])
        etybool.resize(70, 20)
        etybool.hide()
        etybool.move(100, 40)

        etylist = QComboBox(parent=cv)
        etylist.resize(70, 20)
        etylist.hide()
        etylist.move(100, 40)

        btndellist = QPushButton(parent=cv, text="Delete")
        btndellist.move(0, 130)
        btndellist.hide()
        btndellist.clicked.connect(deltolist)

        btnaddlist = QPushButton(parent=cv, text="Add")
        btnaddlist.move(75, 130)
        btnaddlist.hide()
        btnaddlist.clicked.connect(addtolist)

        etynamelist = QLineEdit(parent=cv)
        etynamelist.setPlaceholderText("Value Name")
        etynamelist.hide()
        etynamelist.move(10, 160)
        

        lbl1 = QLabel(parent=cv, text="=")
        lbl1.move(80, 43)

        def create():
            types = cbx.currentText()
            numberv = etynum.text()
            stringv = etystr.text()
            boolenv = etybool.currentText()
            varname = ety1.text()
            if varname:
                if types == "Number" and numberv and varname:
                    sourcecode.append(f"{varname} = {numberv}")
                if types == "String" and stringv and varname:
                    sourcecode.append(f"{varname} = '{stringv}'")
                if types == "Boolen" and boolenv and varname:
                    sourcecode.append(f"{varname} = {boolenv}")

                
                
        btncreate = QPushButton(parent=cv, text="Create")
        btncreate.move(170, 159)
        btncreate.clicked.connect(create)


        windows.append(cv)
        cv.show()
    else:
        info21 = QMessageBox()
        info21.setWindowTitle("Developer")
        info21.setText("This is for Developer Mode only \n Go to Source Code and Enable it")
        info21.setIcon(QMessageBox.Warning)
        info21.setWindowIcon(ico(IDEicons+"infoerrorwarn.png"))
        info21.show()
        info21.exec_()  
def close_all_windows(event):
    QApplication.exit()
def create_new_label():
    labelediting = QLabel(parent=Editor, text="Label")
    labelediting.show()
    add_label_dialog = QNewWindow()
    add_label_dialog.setFixedSize(300,200)
    add_label_dialog.setWindowTitle("Label")
    add_label_dialog.setWindowIcon(ico(IDEicons+"Label.png"))

    lbl1 = QLabel(parent=add_label_dialog, text="left:")
    lbl1.move(10, 10)
    ety1 = QLineEdit(parent=add_label_dialog)
    ety1.resize(50, 20)
    ety1.move(37, 7)
    ety1.setText("0")

    lbl2 = QLabel(parent=add_label_dialog, text="top:")
    lbl2.move(93, 10)
    ety2 = QLineEdit(parent=add_label_dialog)
    ety2.resize(50, 20)
    ety2.move(120, 7)
    ety2.setText("0")

    lbl3 = QLabel(parent=add_label_dialog, text="Text:")
    lbl3.move(10, 33)
    ety3 = QLineEdit(parent=add_label_dialog)
    ety3.resize(100, 20)
    ety3.move(37, 30)
    ety3.setText("Label")

    lbl4 = QLabel(parent=add_label_dialog, text="Width:")
    lbl4.move(10, 55)
    ety4 = QLineEdit(parent=add_label_dialog)
    ety4.resize(50, 20)
    ety4.move(45, 53)
    ety4.setText("40")

    lbl5 = QLabel(parent=add_label_dialog, text="Height:")
    lbl5.move(100, 55)
    ety5 = QLineEdit(parent=add_label_dialog)
    ety5.resize(50, 20)
    ety5.move(137, 53)
    ety5.setText("20")

    lbl6 = QLabel(parent=add_label_dialog, text="ID:")
    lbl6.move(210, 10)
    ety6 = QLineEdit(parent=add_label_dialog)
    ety6.resize(70, 20)
    ety6.move(230, 7)
    ety6.setText("SimpleLbl")

    ety7 = QLineEdit(parent=add_label_dialog)
    ety7.resize(70, 20)
    ety7.move(220, 120)
    ety7.setText("window")

    cb1 = QCheckBox(parent=add_label_dialog, text="Use Parent")
    cb1.move(220, 100)

    def preview():
        left = ety1.text()
        top = ety2.text()
        w = ety4.text()
        h = ety5.text()
        text = ety3.text()
        if left and top and h and w:
            labelediting.move(int(left), int(top))
            labelediting.setText(text)
            labelediting.resize(int(w), int(h))

    def apply():
        def remove(event):
            labelid.deleteLater()

        cb1ch = cb1.isChecked()
        labelid = QLabel(parent=Editor, text="Label")
        labelid.mouseDoubleClickEvent = remove
        labelid.show()
        left = ety1.text()
        top = ety2.text()
        w = ety4.text()
        h = ety5.text()
        text = ety3.text()
        id = ety6.text()
        prnt = ety7.text()
       
        if cb1ch == True and left and top and h and w:
            labelid.move(int(left), int(top))
            labelid.setText(text)
            labelid.resize(int(w), int(h))
            sourcecode.append(f"\n{id} = QtWidgets.QLabel(parent={prnt}, text=f'{text}')")
            sourcecode.append(f"{id}.move({left}, {top})")
            sourcecode.append(f"{id}.resize({w}, {h})")
            add_label_dialog.close()

        elif cb1ch == False and left and top and h and w:
            labelid.move(int(left), int(top))
            labelid.setText(text)
            labelid.resize(int(w), int(h))
            sourcecode.append(f"\n{id} = QtWidgets.QLabel(text=f'{text}')")
            sourcecode.append(f"{id}.move({left}, {top})")
            sourcecode.append(f"{id}.resize({w}, {h})")
            add_label_dialog.close()
            
    def dont_save(event):
        labelediting.deleteLater()
    add_label_dialog.closeEvent = dont_save

    btnpreview1 = QPushButton(parent=add_label_dialog, text="Preview")
    btnpreview1.move(50, 150)
    btnpreview1.clicked.connect(preview)

    btnapply1 = QPushButton(parent=add_label_dialog, text="Apply")
    btnapply1.move(150, 150)
    btnapply1.clicked.connect(apply)

    windows.append(add_label_dialog)
    add_label_dialog.show()
def create_new_btn():
    buttonediting = QPushButton(parent=Editor, text="Button")
    buttonediting.show()
    add_btn_dialog = QNewWindow()
    add_btn_dialog.setFixedSize(300,200)
    add_btn_dialog.setWindowTitle("Button")
    add_btn_dialog.setWindowIcon(ico(IDEicons+"Button.png"))

    lbl1 = QLabel(parent=add_btn_dialog, text="left:")
    lbl1.move(10, 10)
    ety1 = QLineEdit(parent=add_btn_dialog)
    ety1.resize(50, 20)
    ety1.move(37, 7)
    ety1.setText("0")

    lbl2 = QLabel(parent=add_btn_dialog, text="top:")
    lbl2.move(93, 10)
    ety2 = QLineEdit(parent=add_btn_dialog)
    ety2.resize(50, 20)
    ety2.move(120, 7)
    ety2.setText("0")

    lbl3 = QLabel(parent=add_btn_dialog, text="Text:")
    lbl3.move(10, 33)
    ety3 = QLineEdit(parent=add_btn_dialog)
    ety3.resize(100, 20)
    ety3.move(37, 30)
    ety3.setText("Button")

    lbl4 = QLabel(parent=add_btn_dialog, text="Width:")
    lbl4.move(10, 55)
    ety4 = QLineEdit(parent=add_btn_dialog)
    ety4.resize(50, 20)
    ety4.move(45, 53)
    ety4.setText("70")

    lbl5 = QLabel(parent=add_btn_dialog, text="Height:")
    lbl5.move(100, 55)
    ety5 = QLineEdit(parent=add_btn_dialog)
    ety5.resize(50, 20)
    ety5.move(137, 53)
    ety5.setText("23")

    lbl6 = QLabel(parent=add_btn_dialog, text="ID:")
    lbl6.move(210, 10)
    ety6 = QLineEdit(parent=add_btn_dialog)
    ety6.resize(70, 20)
    ety6.move(230, 7)
    ety6.setText("SimpleBtn")

    ety7 = QLineEdit(parent=add_btn_dialog)
    ety7.resize(70, 20)
    ety7.move(220, 70)
    ety7.setText("window")

    def checkChecked():
        cb2ch = cb2.isChecked()
        if cb2ch == True:
            ety8.setDisabled(False)
        elif cb2ch == False:
            ety8.setDisabled(True)
    def checkChecked2():
        cb1ch = cb1.isChecked()
        if cb1ch == True:
            ety7.setDisabled(False)
        elif cb1ch == False:
            ety7.setDisabled(True)

    cb1 = QCheckBox(parent=add_btn_dialog, text="Use Parent")
    cb1.move(220, 50)
    cb1.clicked.connect(checkChecked2)
    cb1.setChecked(True)

    ety8 = QLineEdit(parent=add_btn_dialog)
    ety8.resize(120, 20)
    ety8.move(175, 120)
    ety8.setText("This Is simple button")
    ety8.setDisabled(True)

    cb2 = QCheckBox(parent=add_btn_dialog, text="Use ToolTip")
    cb2.move(220, 100)
    cb2.clicked.connect(checkChecked)

    cb3 = QCheckBox(parent=add_btn_dialog, text="Disabled")
    cb3.move(150, 100)

    def preview():
        left = ety1.text()
        top = ety2.text()
        w = ety4.text()
        h = ety5.text()
        text = ety3.text()
        cbdis = cb3.isChecked()
        if left and top and h and w:
            buttonediting.move(int(left), int(top))
            buttonediting.setText(text)
            buttonediting.resize(int(w), int(h))
            if cbdis == True:
                buttonediting.setDisabled(True)
            else:
                buttonediting.setDisabled(False)

    def apply():
        def remove(event):
            btnid.deleteLater()
        cbdis = cb3.isChecked()
        cb1ch = cb1.isChecked()
        cb2ch = cb2.isChecked()
        btnid = QPushButton(parent=Editor, text="Button")
        btnid.mouseDoubleClickEvent = remove
        btnid.show()
        left = ety1.text()
        top = ety2.text()
        w = ety4.text()
        h = ety5.text()
        text = ety3.text()
        id = ety6.text()
        prnt = ety7.text()
        tt = ety8.text()

        

        if cb1ch == False and cb2ch == False and top and left and h and w:
            btnid.setText(text)
            btnid.move(int(left), int(top))
            btnid.resize(int(w), int(h))
            add_btn_dialog.close()
            sourcecode.append(f"{id} = QtWidgets.QPushButton(text=f'{text}')")
            sourcecode.append(f"{id}.move({left}, {top})")
            sourcecode.append(f"{id}.resize({w}, {h})")

        elif cb1ch == True and cb2ch == False and top and left and h and w:
            btnid.setText(text)
            btnid.move(int(left), int(top))
            btnid.resize(int(w), int(h))
            add_btn_dialog.close()
            sourcecode.append(f"{id} = QtWidgets.QPushButton(parent={prnt}, text=f'{text}')")
            sourcecode.append(f"{id}.move({left}, {top})")
            sourcecode.append(f"{id}.resize({w}, {h})")

        elif cb2ch == True and cb1ch == False and top and left and h and w:
            btnid.setText(text)
            btnid.move(int(left), int(top))
            btnid.resize(int(w), int(h))
            btnid.setToolTip(tt)
            add_btn_dialog.close()
            sourcecode.append(f"{id} = QtWidgets.QPushButton(text=f'{text}')")
            sourcecode.append(f"{id}.move({left}, {top})")
            sourcecode.append(f"{id}.resize({w}, {h})")
            sourcecode.append(f"{id}.setToolTip('{tt}')")

        elif top and left and cb2ch == True and cb1ch == True and h and w:
            btnid.setText(text)
            btnid.move(int(left), int(top))
            btnid.resize(int(w), int(h))
            btnid.setToolTip(tt)
            add_btn_dialog.close()
            sourcecode.append(f"{id} = QtWidgets.QPushButton(parent={prnt}, text=f'{text}')")
            sourcecode.append(f"{id}.move({left}, {top})")
            sourcecode.append(f"{id}.resize({w}, {h})")
            sourcecode.append(f"{id}.setToolTip('{tt}')")
        
        if cbdis == True and top and left and h and w:
            btnid.setDisabled(True)
            sourcecode.append(f"{id}.setDisabled(True)")
        else:
            sourcecode.append(f"{id}.setDisabled(False)")
            btnid.setDisabled(False)


    def dont_save(event):
        buttonediting.deleteLater()
    add_btn_dialog.closeEvent = dont_save

    btnpreview1 = QPushButton(parent=add_btn_dialog, text="Preview")
    btnpreview1.move(50, 150)
    btnpreview1.clicked.connect(preview)

    btnapply1 = QPushButton(parent=add_btn_dialog, text="Apply")
    btnapply1.move(150, 150)
    btnapply1.clicked.connect(apply)


    windows.append(add_btn_dialog)
    add_btn_dialog.show()
def create_new_cb():
    cbediting = QCheckBox(parent=Editor, text="CheckBox")
    cbediting.show()
    add_cb_dialog = QNewWindow()
    add_cb_dialog.setFixedSize(300,200)
    add_cb_dialog.setWindowTitle("CheckBox")
    add_cb_dialog.setWindowIcon(ico(IDEicons+"checkbox.png"))


    def dont_save(event):
        cbediting.deleteLater()
    add_cb_dialog.closeEvent = dont_save

    cb1 = QCheckBox(parent=add_cb_dialog, text="setChecked")
    cb1.move(0, 30)

    lbl1 = QLabel(parent=add_cb_dialog, text="Text :")
    lbl1.move(0, 3)
    ety1 = QLineEdit(parent=add_cb_dialog)
    ety1.setText("CheckBox")
    ety1.move(33, 0)

    lbl2 = QLabel("left:", add_cb_dialog)
    lbl2.move(5, 53)
    ety2 = QLineEdit(parent=add_cb_dialog)
    ety2.setText("0")
    ety2.move(30, 50)
    ety2.resize(50, 20)

    lbl3 = QLabel("top:", add_cb_dialog)
    lbl3.move(83, 53)
    ety3 = QLineEdit(parent=add_cb_dialog)
    ety3.setText("0")
    ety3.move(105, 50)
    ety3.resize(50, 20)

    lbl4 = QLabel("width:", add_cb_dialog)
    lbl4.move(5, 83)
    ety4 = QLineEdit(parent=add_cb_dialog)
    ety4.setText("0")
    ety4.move(40, 80)
    ety4.resize(50, 20)
    ety4.setText("65")

    lbl5 = QLabel("height:", add_cb_dialog)
    lbl5.move(95, 83)
    ety5 = QLineEdit(parent=add_cb_dialog)
    ety5.setText("0")
    ety5.move(135, 80)
    ety5.resize(50, 20)
    ety5.setText("15")

    def checkChecked():
        if cb3.isChecked() == True:
            ety7.setDisabled(False)
        else:
            ety7.setDisabled(True)

    def checkChecked1():
        if cb2.isChecked() == True:
            ety6.setDisabled(False)
        else:
            ety6.setDisabled(True)


    ety6 = QLineEdit(parent=add_cb_dialog)
    ety6.resize(70, 20)
    ety6.move(220, 120)
    ety6.setText("window")

    cb2 = QCheckBox(parent=add_cb_dialog, text="Use Parent")
    cb2.move(220, 100)
    cb2.setChecked(True)
    cb2.clicked.connect(checkChecked1)


    ety7 = QLineEdit(parent=add_cb_dialog)
    ety7.resize(120, 20)
    ety7.move(175, 30)
    ety7.setText("This Is simple Checkbox")
    ety7.setDisabled(True)

    lbl6 = QLabel(parent=add_cb_dialog, text="ID:")
    lbl6.move(158, 53)
    ety8 = QLineEdit(parent=add_cb_dialog)
    ety8.resize(120, 20)
    ety8.move(175, 50)
    ety8.setText("simpleCb1")


    cb3 = QCheckBox(parent=add_cb_dialog, text="Use ToolTip")
    cb3.move(220, 10)
    cb3.clicked.connect(checkChecked)

    cb4 = QCheckBox(parent=add_cb_dialog, text="Disabled")
    cb4.move(150, 100)

    def preview():
        cbdis = cb4.isChecked()
        text = ety1.text()
        left = ety2.text()
        top = ety3.text()
        w = ety4.text()
        h = ety5.text()
        cb1ch = cb1.isChecked()

        if cbdis == True:
            cbediting.setDisabled(True)
        else:
            cbediting.setDisabled(False)

        if cb1ch == False and top and left and h and w:
            cbediting.setText(text)
            cbediting.move(int(left), int(top))
            cbediting.resize(int(w), int(h))
            cbediting.setChecked(False)
        elif cb1ch == True and top and left and h and w :
            cbediting.setText(text)
            cbediting.move(int(left), int(top))
            cbediting.resize(int(w), int(h))
            cbediting.setChecked(True)

    def apply():
            def remove(event):
                cbid.deleteLater()
            
            cbid = Qw.QCheckBox(parent=Editor, text="CheckBox")
            cbid.mouseDoubleClickEvent = remove
            cbid.show()
            cbdis = cb4.isChecked()
            cid = ety8.text()
            text = ety1.text()
            left = ety2.text()
            prnt = ety6.text()
            top = ety3.text()
            w = ety4.text()
            tt = ety7.text()
            h = ety5.text()
            cb1ch = cb1.isChecked()
            cb2ch = cb2.isChecked()
            cb3ch = cb3.isChecked()
            if cb1ch == False and cb2ch == False and cb3ch == False and top and left and h and w:
                cbid.setText(text)
                cbid.move(int(left), int(top))
                cbid.resize(int(w), int(h))
                cbid.setChecked(False)
                sourcecode.append(f"{cid} = QtWidgets.QCheckBox(text=f'{text}')")
                sourcecode.append(f"{cid}.move({left}, {top})")
                sourcecode.append(f"{cid}.resize({w}, {h})")
                sourcecode.append(f"{cid}.setChecked(False)")
                add_cb_dialog.close()

            elif cb1ch == True and cb2ch == False and cb3ch == False and top and left and h and w:
                cbid.setText(text)
                cbid.move(int(left), int(top))
                cbid.resize(int(w), int(h))
                cbid.setChecked(True)
                sourcecode.append(f"\n{cid} = QtWidgets.QCheckBox(text=f'{text}')")
                sourcecode.append(f"{cid}.move({left}, {top})")
                sourcecode.append(f"{cid}.resize({w}, {h})")
                sourcecode.append(f"{cid}.setChecked(True)")
                add_cb_dialog.close()

            elif cb1ch == True and cb2ch == True and cb3ch == False and top and left and h and w:
                cbid.setText(text)
                cbid.move(int(left), int(top))
                cbid.resize(int(w), int(h))
                cbid.setChecked(True)
                sourcecode.append(f"\n{cid} = QtWidgets.QCheckBox(parent={prnt}, text=f'{text}')")
                sourcecode.append(f"{cid}.move({left}, {top})")
                sourcecode.append(f"{cid}.resize({w}, {h})")
                sourcecode.append(f"{cid}.setChecked(True)")
                add_cb_dialog.close()

            elif cb1ch == True and cb2ch == True and cb3ch == True and top and left and h and w:
                cbid.setText(text)
                cbid.move(int(left), int(top))
                cbid.resize(int(w), int(h))
                cbid.setChecked(True)
                sourcecode.append(f"\n{cid} = QtWidgets.QCheckBox(parent={prnt}, text=f'{text}')")
                sourcecode.append(f"{cid}.move({left}, {top})")
                sourcecode.append(f"{cid}.resize({w}, {h})")
                sourcecode.append(f"{cid}.setChecked(True)")
                sourcecode.append(f"{cid}.setToolTip('{tt}')")
                add_cb_dialog.close()

            elif cb1ch == False and cb2ch == True and cb3ch == True and top and left and h and w:
                cbid.setText(text)
                cbid.move(int(left), int(top))
                cbid.resize(int(w), int(h))
                cbid.setChecked(False)
                sourcecode.append(f"\n{cid} = QtWidgets.QCheckBox(parent={prnt}, text=f'{text}')")
                sourcecode.append(f"{cid}.move({left}, {top})")
                sourcecode.append(f"{cid}.resize({w}, {h})")
                sourcecode.append(f"{cid}.setChecked(False)")
                sourcecode.append(f"{cid}.setToolTip('{tt}')")
                add_cb_dialog.close()
            
            elif cb1ch == False and cb2ch == False and cb3ch == True and top and left and h and w:
                cbid.setText(text)
                cbid.move(int(left), int(top))
                cbid.resize(int(w), int(h))
                cbid.setChecked(False)
                sourcecode.append(f"\n{cid} = QtWidgets.QCheckBox(text=f'{text}')")
                sourcecode.append(f"{cid}.move({left}, {top})")
                sourcecode.append(f"{cid}.resize({w}, {h})")
                sourcecode.append(f"{cid}.setChecked(False)")
                sourcecode.append(f"{cid}.setToolTip('{tt}')")
                add_cb_dialog.close()

            elif cb1ch == False and cb2ch == True and cb3ch == False and top and left and h and w:
                cbid.setText(text)
                cbid.move(int(left), int(top))
                cbid.resize(int(w), int(h))
                cbid.setChecked(False)
                sourcecode.append(f"\n{cid} = QtWidgets.QCheckBox(parent={prnt}, text=f'{text}')")
                sourcecode.append(f"{cid}.move({left}, {top})")
                sourcecode.append(f"{cid}.resize({w}, {h})")
                sourcecode.append(f"{cid}.setChecked(False)")
                add_cb_dialog.close()

            elif cb1ch == True and cb2ch == False and cb3ch == True and top and left and h and w:
                cbid.setText(text)
                cbid.move(int(left), int(top))
                cbid.resize(int(w), int(h))
                cbid.setChecked(True)
                sourcecode.append(f"\n{cid} = QtWidgets.QCheckBox(text=f'{text}')")
                sourcecode.append(f"{cid}.move({left}, {top}")
                sourcecode.append(f"{cid}.resize({w}, {h})")
                sourcecode.append(f"{cid}.setChecked(True)")
                sourcecode.append(f"{cid}.setToolTip('{tt}')")
                add_cb_dialog.close()

            if cbdis == True:
                cbid.setDisabled(True)
                sourcecode.append(f"{cid}.setDisabled(True)")
            else:
                sourcecode.append(f"{cid}.setDisabled(False)")
                cbid.setDisabled(False)

            


    btnpreview1 = QPushButton(parent=add_cb_dialog, text="Preview")
    btnpreview1.move(50, 150)
    btnpreview1.clicked.connect(preview)

    btnapply1 = QPushButton(parent=add_cb_dialog, text="Apply")
    btnapply1.move(150, 150)
    btnapply1.clicked.connect(apply)


    windows.append(add_cb_dialog)
    add_cb_dialog.show()
def create_new_le():
    leediting = QLineEdit(parent=Editor)
    leediting.setReadOnly(True)
    leediting.show()
    add_le_dialog = QNewWindow()
    add_le_dialog.setFixedSize(300,200)
    add_le_dialog.setWindowTitle("LineEdit")
    add_le_dialog.setWindowIcon(ico(IDEicons+"inputfield.png"))

    lbl1 = QLabel("left:", add_le_dialog)
    lbl1.move(5, 53)
    ety1 = QLineEdit(parent=add_le_dialog)
    ety1.setText("0")
    ety1.move(30, 50)
    ety1.resize(50, 20)

    lbl2 = QLabel("top:", add_le_dialog)
    lbl2.move(83, 53)
    ety2 = QLineEdit(parent=add_le_dialog)
    ety2.setText("0")
    ety2.move(105, 50)
    ety2.resize(50, 20)

    lbl3 = QLabel(parent=add_le_dialog, text="setText:")
    lbl3.move(1, 3)
    ety3 = QLineEdit(parent=add_le_dialog)
    ety3.move(50, 0)

    lbl4 = QLabel(parent=add_le_dialog, text="setPlaceHolder:")
    lbl4.move(1, 23)
    ety4 = QLineEdit(parent=add_le_dialog)
    ety4.move(80, 20)

    lbl5 = QLabel("width:", add_le_dialog)
    lbl5.move(5, 75)
    ety5 = QLineEdit(parent=add_le_dialog)
    ety5.setText("75")
    ety5.move(36, 71)
    ety5.resize(50, 20)

    lbl6 = QLabel("height:", add_le_dialog)
    lbl6.move(87, 75)
    ety6 = QLineEdit(parent=add_le_dialog)
    ety6.setText("20")
    ety6.move(121, 71)
    ety6.resize(50, 20)

    ety7 = QLineEdit(parent=add_le_dialog)
    ety7.resize(70, 20)
    ety7.move(220, 120)
    ety7.setText("window")

    cb1 = QCheckBox(parent=add_le_dialog, text="Use Parent")
    cb1.move(220, 100)
    cb1.setChecked(True)

    cb2 = QCheckBox(parent=add_le_dialog, text="ReadOnly")
    cb2.setToolTip("Can't Write, only read")
    cb2.move(220, 80)
    cb2.setChecked(False)

    lbl7 = QLabel(parent=add_le_dialog, text="ID:")
    lbl7.move(158, 53)
    ety8 = QLineEdit(parent=add_le_dialog)
    ety8.resize(120, 20)
    ety8.move(175, 50)
    ety8.setText("simpleLE1")

    cb3 = QCheckBox(parent=add_le_dialog, text="Disabled")
    cb3.move(150, 100)

    def preview():
        cbdis = cb3.isChecked()
        cb1ch = cb1.isChecked()
        cb2ch = cb2.isChecked()
        left = ety1.text()
        top = ety2.text()
        text = ety3.text()
        ph = ety4.text()
        w = ety5.text()
        h = ety6.text()
        prnt = ety7.text()
        if w and h and top and left:
            leediting.move(int(left), int(top))
            leediting.resize(int(w), int(h))
            leediting.setText(text)
            leediting.setPlaceholderText(ph)
            if cbdis == True:
                leediting.setDisabled(True)
            else:
                leediting.setDisabled(False)

    def dont_save(event):
        leediting.deleteLater()
    add_le_dialog.closeEvent = dont_save

    def apply():
        def remove(event):
            leid.deleteLater()
        leid = QLineEdit(parent=Editor)
        leid.mouseDoubleClickEvent = remove
        leid.show()
        cbdis = cb3.isChecked()
        cb1ch = cb1.isChecked()
        cb2ch = cb2.isChecked()
        left = ety1.text()
        top = ety2.text()
        text = ety3.text()
        ph = ety4.text()
        w = ety5.text()
        h = ety6.text()
        prnt = ety7.text()
        id = ety8.text()
        if cb1ch == False and cb2ch == False and top and left and w and h:
            leid.move(int(left), int(top))
            leid.resize(int(w), int(h))
            leid.setText(text)
            leid.setPlaceholderText(ph)
            sourcecode.append(f"{id} = QtWidgets.QLineEdit(text='{text}')")
            sourcecode.append(f"{id}.resize({w}, {h})")
            sourcecode.append(f"{id}.move({left}, {top})")
            sourcecode.append(f"{id}.setPlaceHolder('{ph}')")
            add_le_dialog.close()

        elif cb1ch == True and cb2ch == False and top and left and w and h:
            leid.move(int(left), int(top))
            leid.resize(int(w), int(h))
            leid.setText(text)
            leid.setPlaceholderText(ph)
            sourcecode.append(f"{id} = QtWidgets.QLineEdit(parent={prnt},text='{text}')")
            sourcecode.append(f"{id}.resize({w}, {h})")
            sourcecode.append(f"{id}.move({left}, {top})")
            sourcecode.append(f"{id}.setPlaceholderText('{ph}')")
            add_le_dialog.close()

        elif cb1ch == False and cb2ch == True and top and left and w and h:
            leid.move(int(left), int(top))
            leid.resize(int(w), int(h))
            leid.setText(text)
            leid.setPlaceholderText(ph)
            sourcecode.append(f"{id} = QtWidgets.QLineEdit(text='{text}')")
            sourcecode.append(f"{id}.resize({w}, {h})")
            sourcecode.append(f"{id}.move({left}, {top})")
            sourcecode.append(f"{id}.setReadOnly(True)")
            sourcecode.append(f"{id}.setPlaceholderText('{ph}')")
            add_le_dialog.close()

        elif cb1ch == True and cb2ch == True and top and left and w and h:
            leid.move(int(left), int(top))
            leid.resize(int(w), int(h))
            leid.setText(text)
            leid.setPlaceholderText(ph)
            sourcecode.append(f"{id} = QtWidgets.QLineEdit(parent={prnt},text='{text}')")
            sourcecode.append(f"{id}.resize({w}, {h})")
            sourcecode.append(f"{id}.move({left}, {top})")
            sourcecode.append(f"{id}.setReadOnly(True)")
            sourcecode.append(f"{id}.setPlaceholderText('{ph}')")
            add_le_dialog.close()
        
        if cbdis == True:
            leid.setDisabled(True)
            sourcecode.append(f"{id}.setDisabled(True)")
        else:
            sourcecode.append(f"{id}.setDisabled(False)")
            leid.setDisabled(False)


    btnpreview1 = QPushButton(parent=add_le_dialog, text="Preview")
    btnpreview1.move(50, 150)
    btnpreview1.clicked.connect(preview)

    btnapply1 = QPushButton(parent=add_le_dialog, text="Apply")
    btnapply1.move(150, 150)
    btnapply1.clicked.connect(apply)


    windows.append(add_le_dialog)
    add_le_dialog.show()
def create_new_cbx():
    itemsincbx = []
    itemsincbx.clear()
    cbxediting = QComboBox(parent=Editor)
    cbxediting.show()
    add_cbx_dialog = QNewWindow()
    add_cbx_dialog.setFixedSize(300,200)
    add_cbx_dialog.setWindowTitle("ComboBox")
    add_cbx_dialog.setWindowIcon(ico(IDEicons+"ComboBox.png"))
    
    def additem():
        item = ety4.text()
        if item:
            itemsincbx.append(item)
            print(itemsincbx)
            cbx1.addItem(item)

    def clearlist():
        itemsincbx.clear()
        cbx1.clear()


    def dont_save(event):
        cbxediting.deleteLater()
    add_cbx_dialog.closeEvent = dont_save

    lbl1 = QLabel(parent=add_cbx_dialog, text="ID:")
    lbl1.move(176, 13)
    ety1 = QLineEdit(parent=add_cbx_dialog)
    ety1.setText("SimpleCbx1")
    ety1.move(190, 10)
    ety1.resize(100, 20)

    lbl2 = QLabel("left:", add_cbx_dialog)
    lbl2.move(5, 53)
    ety2 = QLineEdit(parent=add_cbx_dialog)
    ety2.setText("0")
    ety2.move(30, 50)
    ety2.resize(50, 20)

    lbl3 = QLabel("top:", add_cbx_dialog)
    lbl3.move(83, 53)
    ety3 = QLineEdit(parent=add_cbx_dialog)
    ety3.setText("0")
    ety3.move(105, 50)
    ety3.resize(50, 20)
#-----------------------------------------------------
    lbl5 = QLabel("width:", add_cbx_dialog)
    lbl5.move(0, 23)
    ety6 = QLineEdit(parent=add_cbx_dialog)
    ety6.setText("100")
    ety6.move(30, 20)
    ety6.resize(50, 20)

    lbl4 = QLabel("height:", add_cbx_dialog)
    lbl4.move(83, 23)
    ety5 = QLineEdit(parent=add_cbx_dialog)
    ety5.setText("20")
    ety5.move(120, 20)
    ety5.resize(50, 20)

    #Disabled, parent, apply, preview

    btn1 = QPushButton(parent=add_cbx_dialog, text="Add")
    btn1.move(30, 90)
    btn1.clicked.connect(additem)

    btn2 = QPushButton(parent=add_cbx_dialog, text="Clear")
    btn2.move(110, 90)
    btn2.clicked.connect(clearlist)

    ety4 = QLineEdit(parent=add_cbx_dialog)
    ety4.move(40, 120)

    cbx1 = QComboBox(parent=add_cbx_dialog)
    cbx1.move(201, 50)

    ety7 = QLineEdit(parent=add_cbx_dialog)
    ety7.resize(70, 20)
    ety7.move(220, 120)
    ety7.setText("window")

    cb2 = QCheckBox(parent=add_cbx_dialog, text="Use Parent")
    cb2.move(220, 100)
    cb2.setChecked(True)


    def preview():
        iid = ety1.text() 
        top = ety3.text()
        left = ety2.text()
        w = ety6.text()
        h = ety5.text()
        if top and left and w and h:
            cbxediting.move(int(left), int(top))
            cbxediting.resize(int(w), int(h))
            cbxediting.clear()
            cbxediting.addItems(itemsincbx)
            

    def apply():
        def deletecbx(event):
            cbxid.deleteLater()
        cbxid = QComboBox(parent=Editor)
        cbxid.mouseDoubleClickEvent = deletecbx
        cbxid.show()
        iid = ety1.text() 
        top = ety3.text()
        left = ety2.text()
        w = ety6.text()
        h = ety5.text()
        prnt = ety7.text()
        prnten = cb2.isChecked()
        if top and left and w and h and iid and prnten == False:
            cbxid.move(int(left), int(top))
            cbxid.resize(int(w), int(h))
            cbxid.clear()
            cbxid.addItems(itemsincbx)
            sourcecode.append(f"\n{iid} = QtWidgets.QComboBox()")
            sourcecode.append(f"{iid}.move({left}, {top})")
            sourcecode.append(f"{iid}.resize({w}, {h})")
            sourcecode.append(f"{iid}.addItems({itemsincbx})")
            add_cbx_dialog.close()

        elif top and left and w and h and iid and prnten == True:
            cbxid.move(int(left), int(top))
            cbxid.resize(int(w), int(h))
            cbxid.clear()
            cbxid.addItems(itemsincbx)
            sourcecode.append(f"\n{iid} = QtWidgets.QComboBox(parent={prnt})")
            sourcecode.append(f"{iid}.move({left}, {top})")
            sourcecode.append(f"{iid}.resize({w}, {h})")
            sourcecode.append(f"{iid}.addItems({itemsincbx})")
            add_cbx_dialog.close()


    btnpreview = QPushButton(parent=add_cbx_dialog, text="Preview")
    btnpreview.move(50,170)
    btnpreview.clicked.connect(preview)

    btnapply = QPushButton(parent=add_cbx_dialog, text="Apply")
    btnapply.move(160,170)
    btnapply.clicked.connect(apply)
    
    windows.append(add_cbx_dialog)
    add_cbx_dialog.show()
def create_new_rb():
    rbediting = QRadioButton(parent=Editor, text="RadioButton")
    rbediting.show()
    add_rb_dialog = QNewWindow()
    add_rb_dialog.setFixedSize(300,200)
    add_rb_dialog.setWindowTitle("RadioButton")
    add_rb_dialog.setWindowIcon(ico(IDEicons+"radiobutton.png"))


    def dont_save(event):
        rbediting.deleteLater()
    add_rb_dialog.closeEvent = dont_save

    cb1 = QCheckBox(parent=add_rb_dialog, text="setChecked")
    cb1.move(0, 30)

    lbl1 = QLabel(parent=add_rb_dialog, text="Text :")
    lbl1.move(0, 3)
    ety1 = QLineEdit(parent=add_rb_dialog)
    ety1.setText("RadioButton")
    ety1.move(33, 0)

    lbl2 = QLabel("left:", add_rb_dialog)
    lbl2.move(5, 53)
    ety2 = QLineEdit(parent=add_rb_dialog)
    ety2.setText("0")
    ety2.move(30, 50)
    ety2.resize(50, 20)

    lbl3 = QLabel("top:", add_rb_dialog)
    lbl3.move(83, 53)
    ety3 = QLineEdit(parent=add_rb_dialog)
    ety3.setText("0")
    ety3.move(105, 50)
    ety3.resize(50, 20)

    lbl4 = QLabel("width:", add_rb_dialog)
    lbl4.move(5, 83)
    ety4 = QLineEdit(parent=add_rb_dialog)
    ety4.setText("0")
    ety4.move(40, 80)
    ety4.resize(50, 20)
    ety4.setText("65")

    lbl5 = QLabel("height:", add_rb_dialog)
    lbl5.move(95, 83)
    ety5 = QLineEdit(parent=add_rb_dialog)
    ety5.setText("0")
    ety5.move(135, 80)
    ety5.resize(50, 20)
    ety5.setText("15")

    def checkChecked():
        if cb3.isChecked() == True:
            ety7.setDisabled(False)
        else:
            ety7.setDisabled(True)

    def checkChecked1():
        if cb2.isChecked() == True:
            ety6.setDisabled(False)
        else:
            ety6.setDisabled(True)


    ety6 = QLineEdit(parent=add_rb_dialog)
    ety6.resize(70, 20)
    ety6.move(220, 120)
    ety6.setText("window")

    cb2 = QCheckBox(parent=add_rb_dialog, text="Use Parent")
    cb2.move(220, 100)
    cb2.setChecked(True)
    cb2.clicked.connect(checkChecked1)


    ety7 = QLineEdit(parent=add_rb_dialog)
    ety7.resize(120, 20)
    ety7.move(175, 30)
    ety7.setText("This Is simple RadioButton")
    ety7.setDisabled(True)

    lbl6 = QLabel(parent=add_rb_dialog, text="ID:")
    lbl6.move(158, 53)
    ety8 = QLineEdit(parent=add_rb_dialog)
    ety8.resize(120, 20)
    ety8.move(175, 50)
    ety8.setText("simpleRb1")


    cb3 = QCheckBox(parent=add_rb_dialog, text="Use ToolTip")
    cb3.move(220, 10)
    cb3.clicked.connect(checkChecked)

    cb4 = QCheckBox(parent=add_rb_dialog, text="Disabled")
    cb4.move(150, 100)

    def preview():
        cbdis = cb4.isChecked()
        text = ety1.text()
        left = ety2.text()
        top = ety3.text()
        w = ety4.text()
        h = ety5.text()
        cb1ch = cb1.isChecked()

        if cbdis == True:
            rbediting.setDisabled(True)
        else:
            rbediting.setDisabled(False)

        if cb1ch == False and top and left and h and w:
            rbediting.setText(text)
            rbediting.move(int(left), int(top))
            rbediting.resize(int(w), int(h))
            rbediting.setChecked(False)
        elif cb1ch == True and top and left and h and w :
            rbediting.setText(text)
            rbediting.move(int(left), int(top))
            rbediting.resize(int(w), int(h))
            rbediting.setChecked(True)

    def apply():
            def remove(event):
                cbid.deleteLater()
            
            cbid = Qw.QRadioButton(parent=Editor, text="RadioButton")
            cbid.mouseDoubleClickEvent = remove
            cbid.show()
            cbdis = cb4.isChecked()
            cid = ety8.text()
            text = ety1.text()
            left = ety2.text()
            prnt = ety6.text()
            top = ety3.text()
            w = ety4.text()
            tt = ety7.text()
            h = ety5.text()
            cb1ch = cb1.isChecked()
            cb2ch = cb2.isChecked()
            cb3ch = cb3.isChecked()
            if cb1ch == False and cb2ch == False and cb3ch == False and top and left and h and w:
                cbid.setText(text)
                cbid.move(int(left), int(top))
                cbid.resize(int(w), int(h))
                cbid.setChecked(False)
                sourcecode.append(f"{cid} = QtWidgets.QRadioButton(text=f'{text}')")
                sourcecode.append(f"{cid}.move({left}, {top})")
                sourcecode.append(f"{cid}.resize({w}, {h})")
                sourcecode.append(f"{cid}.setChecked(False)")
                add_rb_dialog.close()

            elif cb1ch == True and cb2ch == False and cb3ch == False and top and left and h and w:
                cbid.setText(text)
                cbid.move(int(left), int(top))
                cbid.resize(int(w), int(h))
                cbid.setChecked(True)
                sourcecode.append(f"\n{cid} = QtWidgets.QRadioButton(text=f'{text}')")
                sourcecode.append(f"{cid}.move({left}, {top})")
                sourcecode.append(f"{cid}.resize({w}, {h})")
                sourcecode.append(f"{cid}.setChecked(True)")
                add_rb_dialog.close()

            elif cb1ch == True and cb2ch == True and cb3ch == False and top and left and h and w:
                cbid.setText(text)
                cbid.move(int(left), int(top))
                cbid.resize(int(w), int(h))
                cbid.setChecked(True)
                sourcecode.append(f"\n{cid} = QtWidgets.QRadioButton(parent={prnt}, text=f'{text}')")
                sourcecode.append(f"{cid}.move({left}, {top})")
                sourcecode.append(f"{cid}.resize({w}, {h})")
                sourcecode.append(f"{cid}.setChecked(True)")
                add_rb_dialog.close()

            elif cb1ch == True and cb2ch == True and cb3ch == True and top and left and h and w:
                cbid.setText(text)
                cbid.move(int(left), int(top))
                cbid.resize(int(w), int(h))
                cbid.setChecked(True)
                sourcecode.append(f"\n{cid} = QtWidgets.QRadioButton(parent={prnt}, text=f'{text}')")
                sourcecode.append(f"{cid}.move({left}, {top})")
                sourcecode.append(f"{cid}.resize({w}, {h})")
                sourcecode.append(f"{cid}.setChecked(True)")
                sourcecode.append(f"{cid}.setToolTip('{tt}')")
                add_rb_dialog.close()

            elif cb1ch == False and cb2ch == True and cb3ch == True and top and left and h and w:
                cbid.setText(text)
                cbid.move(int(left), int(top))
                cbid.resize(int(w), int(h))
                cbid.setChecked(False)
                sourcecode.append(f"\n{cid} = QtWidgets.QRadioButton(parent={prnt}, text=f'{text}')")
                sourcecode.append(f"{cid}.move({left}, {top})")
                sourcecode.append(f"{cid}.resize({w}, {h})")
                sourcecode.append(f"{cid}.setChecked(False)")
                sourcecode.append(f"{cid}.setToolTip('{tt}')")
                add_rb_dialog.close()
            
            elif cb1ch == False and cb2ch == False and cb3ch == True and top and left and h and w:
                cbid.setText(text)
                cbid.move(int(left), int(top))
                cbid.resize(int(w), int(h))
                cbid.setChecked(False)
                sourcecode.append(f"\n{cid} = QtWidgets.QRadioButton(text=f'{text}')")
                sourcecode.append(f"{cid}.move({left}, {top})")
                sourcecode.append(f"{cid}.resize({w}, {h})")
                sourcecode.append(f"{cid}.setChecked(False)")
                sourcecode.append(f"{cid}.setToolTip('{tt}')")
                add_rb_dialog.close()

            elif cb1ch == False and cb2ch == True and cb3ch == False and top and left and h and w:
                cbid.setText(text)
                cbid.move(int(left), int(top))
                cbid.resize(int(w), int(h))
                cbid.setChecked(False)
                sourcecode.append(f"\n{cid} = QtWidgets.QRadioButton(parent={prnt}, text=f'{text}')")
                sourcecode.append(f"{cid}.move({left}, {top})")
                sourcecode.append(f"{cid}.resize({w}, {h})")
                sourcecode.append(f"{cid}.setChecked(False)")
                add_rb_dialog.close()

            elif cb1ch == True and cb2ch == False and cb3ch == True and top and left and h and w:
                cbid.setText(text)
                cbid.move(int(left), int(top))
                cbid.resize(int(w), int(h))
                cbid.setChecked(True)
                sourcecode.append(f"\n{cid} = QtWidgets.QCheckBox(text=f'{text}')")
                sourcecode.append(f"{cid}.move({left}, {top}")
                sourcecode.append(f"{cid}.resize({w}, {h})")
                sourcecode.append(f"{cid}.setChecked(True)")
                sourcecode.append(f"{cid}.setToolTip('{tt}')")
                add_rb_dialog.close()

            if cbdis == True:
                cbid.setDisabled(True)
                sourcecode.append(f"{cid}.setDisabled(True)")
            else:
                sourcecode.append(f"{cid}.setDisabled(False)")
                cbid.setDisabled(False)

    btnpreview1 = QPushButton(parent=add_rb_dialog, text="Preview")
    btnpreview1.move(50, 150)
    btnpreview1.clicked.connect(preview)

    btnapply1 = QPushButton(parent=add_rb_dialog, text="Apply")
    btnapply1.move(150, 150)
    btnapply1.clicked.connect(apply)


    windows.append(add_rb_dialog)
    add_rb_dialog.show()

#Editor MainWIndow ----------------------------------------------------------------------------------------
IDEicons = "IDE\\icons\\"
app = QtWidgets.QApplication(sys.argv)
Editor = QtWidgets.QWidget()
Editor.setWindowTitle("ITRone - Editor")
Editor.setWindowIcon(ico(IDEicons+"appicon.png"))
Editor.setFixedSize(500, 400)
Editor.move(430, 200)
Editor.closeEvent = close_all_windows
Editor.show()


#Toolbar -----------------------------------------------------------------------------------------------------
Toolbar = QtWidgets.QWidget()
Toolbar.setFixedSize(450,100)
Toolbar.move(450, 10)
Toolbar.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
Toolbar.setWindowTitle("ToolBox")
Toolbar.setWindowIcon(ico(IDEicons+"appicon"))

#Source ---------------------------------------------------------------------------------------------------------------------
Sou = QNewWindow()
Sou.setFixedSize(400,700)
Sou.move(950, 0)
Sou.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
Sou.setWindowTitle("Source Code")
Sou.setWindowIcon(ico(IDEicons+"appicon"))

sourcecode = QTextEdit(parent=Sou)
sourcecode.setText("from PyQt5 import QtCore, QtGui, QtWidgets\nimport sys")
sourcecode.resize(400,670)
sourcecode.showNormal()
sourcecode.setReadOnly(True)
sourcecode.move(0,20)



menu_bar = QMenuBar(Sou)
options_menu = QMenu("Options", Sou)
build_menu = QMenu("Build", Sou)
developer_mode_action = QAction("DeveloperMode", Sou, checkable=True)
build_action = QAction("Build .py", Sou)
build_action.setIcon(ico(IDEicons+"example.png"))
developer_mode_action.setToolTip("This is not change Editor")
options_menu.addAction(developer_mode_action)
build_menu.addAction(build_action)
menu_bar.addMenu(options_menu)
menu_bar.addMenu(build_menu)
developer_mode_action.triggered.connect(toggle_developer_mode)
build_action.triggered.connect(buildpy)


Sou.show()
windows.append(Sou)

#Widgets -------------------------------
def run_code(self):
        # Get text from QTextEdit
        text = sourcecode.toPlainText()
        # Write the text to prj.py
        with open("prj.py", "w") as file:
            file.write(text)
        print("Text saved to prj.py")
        time.sleep(1)
        try:
            result = subprocess.run(["python", "prj.py"], check=True, capture_output=True, text=True)
            print("Output:", result.stdout)
        except subprocess.CalledProcessError as e:
            print("Error:", e.stderr)
            errordialog = QMessageBox()
            errordialog.setWindowTitle("Error SourceCode")
            errordialog.setText(e.stderr)
            errordialog.setWindowIcon(ico(IDEicons+"appicon.png"))
            errordialog.setIcon(QMessageBox.Critical)
            MsgCopyButton = errordialog.addButton("Copy", QMessageBox.ActionRole)
            errordialog.setStandardButtons(QMessageBox.Ok)
            
            errordialog.show()
            errordialog.exec_()

            response = errordialog.clickedButton()
            if response == errordialog.button(QMessageBox.Ok):
                print("OK clicked")
            elif response == MsgCopyButton:
                # Copy error message to clipboard
                clipboard = QApplication.clipboard()
                error_message = errordialog.text()
                clipboard.setText(error_message)



btncw = Qw.QPushButton(parent=Toolbar)
btncw.setIcon(ico(IDEicons+"create_window.png"))
btncw.setToolTip("Create Window")
btncw.setIconSize(QtCore.QSize(40, 35))
btncw.move(400, 0)
btncw.clicked.connect(create_window)

btnew = Qw.QPushButton(parent=Toolbar)
btnew.setIcon(ico(IDEicons+"end_window.png"))
btnew.setToolTip("End Window")
btnew.setIconSize(QtCore.QSize(40, 35))
btnew.move(400, 40)
btnew.clicked.connect(end_window)

btnrun = Qw.QPushButton(parent=Toolbar)
btnrun.setIcon(ico(IDEicons+"run.png"))
btnrun.setToolTip("Run Source Code")
btnrun.clicked.connect(run_code)
btnrun.move(0, 75)

btnlib = Qw.QPushButton(parent=Toolbar)
btnlib.setIcon(ico(IDEicons+"lib.png"))
btnlib.setToolTip("Import Library")
btnlib.clicked.connect(import_lib)
btnlib.move(60, 75)

btnvars = Qw.QPushButton(parent=Toolbar)
btnvars.setIcon(ico(IDEicons+"var.png"))
btnvars.setToolTip("Create a variables")
btnvars.clicked.connect(create_var)
btnvars.move(30, 75)

btnaddlbl = Qw.QPushButton(parent=Toolbar)
btnaddlbl.setIcon(ico(IDEicons+"Label.png"))
btnaddlbl.setToolTip("Create Widget 'Label'")
btnaddlbl.clicked.connect(create_new_label)

btnaddbtn = Qw.QPushButton(parent=Toolbar)
btnaddbtn.setIcon(ico(IDEicons+"Button.png"))
btnaddbtn.setToolTip("Create Widget 'Button'")
btnaddbtn.clicked.connect(create_new_btn)
btnaddbtn.move(30, 0)

btnaddcb = Qw.QPushButton(parent=Toolbar)
btnaddcb.setIcon(ico(IDEicons+"checkbox.png"))
btnaddcb.setToolTip("Create Widget 'CheckBox'")
btnaddcb.clicked.connect(create_new_cb)
btnaddcb.move(60, 0)

btnaddle = Qw.QPushButton(parent=Toolbar)
btnaddle.setIcon(ico(IDEicons+"inputField.png"))
btnaddle.setToolTip("Create Widget 'LineEdit'")
btnaddle.clicked.connect(create_new_le)
btnaddle.move(90, 0)

btnaddcbx = Qw.QPushButton(parent=Toolbar)
btnaddcbx.setIcon(ico(IDEicons+"ComboBox.png"))
btnaddcbx.setToolTip("Create Widget 'ComboBox'")
btnaddcbx.clicked.connect(create_new_cbx)
btnaddcbx.move(120, 0)

btnaddcb = Qw.QPushButton(parent=Toolbar)
btnaddcb.setIcon(ico(IDEicons+"radiobutton.png"))
btnaddcb.setToolTip("Create Widget 'RadioButton'")
btnaddcb.clicked.connect(create_new_rb)
btnaddcb.move(150, 0)


Toolbar.show()
app.exec_()