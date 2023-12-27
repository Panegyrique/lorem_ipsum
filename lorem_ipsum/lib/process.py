import os
import csv
import random
from datetime import datetime, timedelta
import pyperclip
import base64

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from Crypto.Cipher import AES
from lib.gui import Ui_MainWindow
from lib.style import custom_style


class Core_Lorem_Ipsum(QMainWindow, Ui_MainWindow): 

    def __init__(self):
        QMainWindow.__init__(self)

        self.version = "0.3"

        self.surname = ""
        self.name = ""
        self.birth_date = ""
        self.key = ""

        self.latin_csv_path = ""
        self.history_csv_path = ""
        self.icon_path = ""
        self.data_latin_csv = ""
        self.len_data_latin_csv = 0
        self.key_state = False
        self.mode = 0 # 0 = decryption and 1 = encryption
        
        self.setupUi(self)
        self.setWindowTitle("Lorem Ipsum - %s"%(self.version)) 
        custom_style(self)

        self._init_all()


    def _init_ui(self):
        self.key_label.setVisible(False)
        self.state_key_label.setVisible(False)
        self.key_plainTextEdit.setVisible(False)
        self.ok_pushButton.setVisible(False)
        self.cancel_pushButton.setVisible(False)

        icon = QIcon(self.icon_path)
        self.setWindowIcon(icon)
        self.setMaximumHeight(295)
    

    def _init_enabled(self):
        self.name_plainTextEdit.setEnabled(False)
        self.birth_date_plainTextEdit.setEnabled(False)


    def _init_events(self):
        self.history.triggered.connect(self.history_Click) # Menu GUI events
        self.history.setShortcut("CTRL+H")
        self.save.triggered.connect(self.save_Click)
        self.save.setShortcut("CTRL+S")
    
        self.generate_pushButton.clicked.connect(self.generate_Click) # Button GUI events
        self.copy_pushButton.clicked.connect(self.copy_Click)
        self.name_radioButton.toggled.connect(self.name_Toggle)
        self.birth_date_radioButton.toggled.connect(self.birth_date_Toggle)
        self.key_plainTextEdit.textChanged.connect(self.key_Changed)
        self.ok_pushButton.clicked.connect(self.ok_Click)
        self.cancel_pushButton.clicked.connect(self.cancel_Click)


    def _init_path(self):
        dir = os.path.dirname(__file__)
        self.latin_csv_path = os.path.join(dir, '../data/dictionary_latin.csv')
        self.history_csv_path = os.path.join(dir, '../data/dictionary_history.csv')
        self.icon_path = os.path.join(dir, '../data/icon.png')


    def _init_data(self):
        if os.path.exists(self.latin_csv_path):
            with open(self.latin_csv_path) as csvfile:
                reader = csv.reader(csvfile)
                self.data_latin_csv = list(reader)
                self.len_data_latin_csv = len(self.data_latin_csv)


    def _init_all(self):
        self._init_path()
        self._init_ui()
        self._init_enabled()
        self._init_events()
        self._init_data()
        self.generate_data(True, False, False)


    def history_Click(self):
        self.switch_generate_to_key_menu()
        self.key_label.setText("Decryption key")
        self.key_plainTextEdit.setPlainText("")
        self.mode = 0


    def save_Click(self):
        self.switch_generate_to_key_menu()
        self.key_label.setText("Encryption key")
        self.key_plainTextEdit.setPlainText("")
        self.mode = 1


    def generate_Click(self):
        self.generate_data(True, True, True)


    def copy_Click(self):
        pyperclip.copy(self.surname + "/" + self.name) if self.name_radioButton.isChecked() else pyperclip.copy(self.surname)


    def name_Toggle(self):
        if self.name_radioButton.isChecked() :
            self.name_plainTextEdit.setEnabled(True)
            self.generate_data(False, True, False)
        else :
            self.name_plainTextEdit.setEnabled(False)
            self.name_plainTextEdit.setPlainText("")


    def birth_date_Toggle(self):
        if self.birth_date_radioButton.isChecked() :
            self.birth_date_plainTextEdit.setEnabled(True)
            self.generate_data(False, False, True)
        else :
            self.birth_date_plainTextEdit.setEnabled(False)
            self.birth_date_plainTextEdit.setPlainText("")


    def key_Changed(self):
        self.key = (self.key_plainTextEdit.toPlainText()).encode('utf-8')

        if len(self.key) < 16:
            self.state_key_label.setText("Key is too short ")
            self.key_state = False
        elif len(self.key) > 32:
            self.state_key_label.setText("Key is too long ")
            self.key_state = False
        else:
            self.state_key_label.setText("Key is perfect ")
            self.key = self.key.ljust(32, b"-")
            self.key_state = True


    def ok_Click(self):
        if self.key_state:

            if self.mode:
                ciphertext_surname, ciphertext_name, ciphertext_birth_date = self.encrypt_data()
                self.save_encrypted_data(ciphertext_surname, ciphertext_name, ciphertext_birth_date)
            elif not self.mode:
                print("History decrypted\n")
                self.decrypt_csv()

            self.switch_save_to_generate_menu()
    

    def cancel_Click(self):
        self.switch_save_to_generate_menu()


    def generate_data(self, surname, name, birth_date):
        if surname:
            self.surname = str(self.data_latin_csv[random.randint(0, self.len_data_latin_csv)])[2:-2]
            self.surname_plainTextEdit.setPlainText(self.surname)

        if name and self.name_radioButton.isChecked():
            self.name = str(self.data_latin_csv[random.randint(0, self.len_data_latin_csv)])[2:-2]
            self.name_plainTextEdit.setPlainText(self.name)

        if birth_date and self.birth_date_radioButton.isChecked():
            start_date = datetime(1970, 1, 1)
            end_date = datetime(2000, 1, 1)
            date_range = (end_date - start_date).days
            random_days = random.randint(0, date_range)
            self.birth_date = str((start_date + timedelta(days=random_days)).strftime("%Y/%m/%d"))
            self.birth_date_plainTextEdit.setPlainText(self.birth_date)


    def encrypt_data(self):
        cipher = AES.new(self.key, AES.MODE_ECB) # AES 256 bits type ECB
        ciphertext_surname = cipher.encrypt(self.surname.encode('utf-8').ljust(32, b"-"))
        cipher = AES.new(self.key, AES.MODE_ECB)
        ciphertext_name = cipher.encrypt(self.name.encode('utf-8').ljust(32, b"-"))
        cipher = AES.new(self.key, AES.MODE_ECB)
        ciphertext_birth_date = cipher.encrypt(self.birth_date.encode('utf-8').ljust(32, b"-"))

        return ciphertext_surname, ciphertext_name, ciphertext_birth_date


    def save_encrypted_data(self, ciphertext_surname, ciphertext_name, ciphertext_birth_date):
        encoded_surname = base64.b64encode(ciphertext_surname).decode('utf-8')  # Switch to base64
        encoded_name = base64.b64encode(ciphertext_name).decode('utf-8')
        encoded_birth_date = base64.b64encode(ciphertext_birth_date).decode('utf-8')

        new_line = f"{encoded_surname}SEP{encoded_name}SEP{encoded_birth_date}" # Concatenate

        if os.path.exists(self.history_csv_path): # Write
            with open(self.history_csv_path, 'a', encoding='utf-8', newline='') as csvfile:
                csvfile.write(new_line + '\n')


    def decrypt_csv(self):
        if os.path.exists(self.history_csv_path):

            with open(self.history_csv_path, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)

                for index, line in enumerate(reader, start=0):

                    if not line:
                        continue

                    data_parts = line[0].split('SEP')

                    cipher = AES.new(self.key, AES.MODE_ECB)
                    try:
                        surname = ((cipher.decrypt(base64.b64decode(data_parts[0]))).decode('utf-8')).replace('-', '')
                    except:
                        surname = "Invalid Key"
                    cipher = AES.new(self.key, AES.MODE_ECB)
                    try:
                        name = ((cipher.decrypt(base64.b64decode(data_parts[1]))).decode('utf-8')).replace('-', '')
                    except:
                        name = "Invalid Key"
                    cipher = AES.new(self.key, AES.MODE_ECB)
                    try:
                        birth_date = ((cipher.decrypt(base64.b64decode(data_parts[2]))).decode('utf-8')).replace('-', '')
                    except:
                        birth_date = "Invalid Key"

                    print("Line n°%s\nSurname : %s\nName : %s\nBirth date : %s\n\n"%(index, surname, name, birth_date))


    def switch_generate_to_key_menu(self):
        self.key_label.setVisible(True)
        self.state_key_label.setVisible(True)
        self.key_plainTextEdit.setVisible(True)
        self.ok_pushButton.setVisible(True)
        self.cancel_pushButton.setVisible(True)
        self.menubar.setVisible(False)
        self.surname_label.setVisible(False)
        self.surname_plainTextEdit.setVisible(False)
        self.name_radioButton.setVisible(False)
        self.name_plainTextEdit.setVisible(False)
        self.birth_date_radioButton.setVisible(False)
        self.birth_date_plainTextEdit.setVisible(False)
        self.generate_pushButton.setVisible(False)
        self.copy_pushButton.setVisible(False)
    

    def switch_save_to_generate_menu(self):
        self.key_label.setVisible(False)
        self.state_key_label.setVisible(False)
        self.key_plainTextEdit.setVisible(False)
        self.ok_pushButton.setVisible(False)
        self.cancel_pushButton.setVisible(False)
        self.menubar.setVisible(True)
        self.surname_label.setVisible(True)
        self.surname_plainTextEdit.setVisible(True)
        self.name_radioButton.setVisible(True)
        self.name_plainTextEdit.setVisible(True)
        self.birth_date_radioButton.setVisible(True)
        self.birth_date_plainTextEdit.setVisible(True)
        self.generate_pushButton.setVisible(True)
        self.copy_pushButton.setVisible(True)