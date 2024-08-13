from PyQt6 import QtCore, QtWidgets, QtGui
import os


class UIFORM(object):
    def __init__(self):
        self.buttons = None
        self._bot_score = None
        self.times_bot_won_label = None
        self._user_Score = None
        self.times_user_won_label = None
        self.verticalLayout = None
        self.tic_tac_buttons_layout = None
        self.stats_layout = None
        self.current_player = "X"

        self.x_icon = QtGui.QIcon(os.getcwd() + "/resources/cross.png")
        self.o_icon = QtGui.QIcon(os.getcwd() + "/resources/circle.png")

    def setup_ui(self, Form):
        Form.setObjectName("Tic Tac Toe - PyQT6")
        Form.resize(500, 500)
        Form.setMinimumSize(QtCore.QSize(500, 500))

        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("main_layout")

        self.tic_tac_buttons_layout = QtWidgets.QGridLayout()
        self.tic_tac_buttons_layout.setObjectName("tic_tac_buttons_layout")

        self.generate_tic_tac_toe_buttons()

        self.verticalLayout.addLayout(self.tic_tac_buttons_layout)

        self.stats_layout = QtWidgets.QHBoxLayout()
        self.stats_layout.setObjectName("stats_layout")

        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Policy.Fixed,
                                           QtWidgets.QSizePolicy.Policy.Minimum)

        self.stats_layout.addItem(spacerItem)
        self.times_user_won_label = QtWidgets.QLabel(parent=Form)
        self.times_user_won_label.setObjectName("times_user_won_label")
        self.stats_layout.addWidget(self.times_user_won_label)

        self._user_Score = QtWidgets.QLabel(parent=Form)
        self._user_Score.setObjectName("_user_Score")
        self.stats_layout.addWidget(self._user_Score)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.stats_layout.addItem(spacerItem1)

        self.times_bot_won_label = QtWidgets.QLabel(parent=Form)
        self.times_bot_won_label.setObjectName("times_bot_won_label")
        self.stats_layout.addWidget(self.times_bot_won_label)

        self._bot_score = QtWidgets.QLabel(parent=Form)
        self._bot_score.setObjectName("_bot_score")
        self.stats_layout.addWidget(self._bot_score)

        spacerItem2 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Policy.Fixed,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.stats_layout.addItem(spacerItem2)

        self.verticalLayout.addLayout(self.stats_layout)

        self.retranslate_ui(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def generate_tic_tac_toe_buttons(self):
        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = QtWidgets.QPushButton(parent=None)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                                   QtWidgets.QSizePolicy.Policy.Expanding)
                button.setSizePolicy(sizePolicy)
                button.setMinimumSize(QtCore.QSize(100, 100))
                button.setObjectName(f"tic_tac_button{row + 1}x{col + 1}")
                button.setText("")

                button.setIconSize(QtCore.QSize(150, 150))

                button.clicked.connect(lambda _, r=row, c=col: self.on_button_click(r, c))

                self.tic_tac_buttons_layout.addWidget(button, row, col)
                button_row.append(button)
            self.buttons.append(button_row)

    def on_button_click(self, row, col):
        button = self.buttons[row][col]
        if self.current_player == "X":
            button.setIcon(self.x_icon)
            self.current_player = "O"
        else:
            button.setIcon(self.o_icon)
            self.current_player = "X"

        button.setEnabled(False)

    def retranslate_ui(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Tic Tac Toe - PyQT6"))
        self.times_user_won_label.setText(_translate("Form", "Times User Won: "))
        self._user_Score.setText(_translate("Form", "0"))
        self.times_bot_won_label.setText(_translate("Form", "Times Bot Won: "))
        self._bot_score.setText(_translate("Form", "0"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    WidgetForm = QtWidgets.QWidget()
    ui = UIFORM()
    ui.setup_ui(WidgetForm)
    WidgetForm.show()
    sys.exit(app.exec())
