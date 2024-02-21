import tkinter.messagebox as tkMessageBox

def Exit(root):
    result = tkMessageBox.askquestion("Café Temptation", "Deseja sair?")
    if result == 'yes':
        root.destroy()
