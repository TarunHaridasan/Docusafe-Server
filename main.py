if __name__=="__main__":    
    #Imports
    from PyQt5 import QtWidgets
    from GUI import home
    import sys
    import server
    import threading
    import multiprocessing

    #Initialize GUI
    GUI = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = home.Ui_MainWindow()
    ui.setupUi(MainWindow)      

    p = None

    #Bind start server button to start a new process
    def startServer():
        print("[INFO] Server Starting")
        ui.label_4.setText("Started")
        ui.toolButton_2.setDisabled(True)
        ui.toolButton.setDisabled(False)   
        global p   
        p = multiprocessing.Process(target = server.start, daemon=True)  
        p.start()
    ui.toolButton_2.clicked.connect(startServer)

    #Bind stop server button to terminate the server process
    def stopServer():
        print("[INFO] Server Stopping")     
        ui.label_4.setText("Stopped")
        ui.toolButton.setDisabled(True)
        ui.toolButton_2.setDisabled(False)
        p.terminate()
    ui.toolButton.clicked.connect(stopServer)

    #Start GUI
    MainWindow.show()
    GUI.exec_()