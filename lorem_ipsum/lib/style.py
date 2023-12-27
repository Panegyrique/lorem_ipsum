def custom_style(ui):
    style = """
        QPushButton {
            background-color: #4CAF50; /* Green */
            border: none;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 4px;
        }

        QPushButton:hover {
            background-color: #45a049; /* Darker green */
        }

        QLabel {
            font-size: 14px;
        }

        QPlainTextEdit {
            font-size: 14px;
        }
    """

    ui.ok_pushButton.setStyleSheet(style)
    ui.cancel_pushButton.setStyleSheet(style)
    ui.generate_pushButton.setStyleSheet(style)
    ui.copy_pushButton.setStyleSheet(style)
    ui.key_label.setStyleSheet(style)
    ui.state_key_label.setStyleSheet(style)

    ui.surname_plainTextEdit.setStyleSheet("QPlainTextEdit { font-size: 14px; }")
    ui.name_plainTextEdit.setStyleSheet("QPlainTextEdit { font-size: 14px; }")
    ui.birth_date_plainTextEdit.setStyleSheet("QPlainTextEdit { font-size: 14px; }")
    ui.key_plainTextEdit.setStyleSheet("QPlainTextEdit { font-size: 14px; }")