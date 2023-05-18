#создай тут фоторедактор Easy Editor!
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QRadioButton, QVBoxLayout, QHBoxLayout, QWidget, QApplication

app = QApplication([])

main_win = QWidget()
main_win.resize(600,400)
main_win.show()

# Вариант 1
# main_h_layout = QHBoxLayout()

# left_v_layout = QVBoxLayout()
# center_v_layout = QVBoxLayout()
# right_v_layout = QVBoxLayout()

# left = QPushButton('1')
# up = QPushButton('2')
# down = QPushButton('3')
# center = QPushButton('4')
# right = QPushButton('5')

# left_v_layout.addWidget(left)

# center_v_layout.addWidget(up)
# center_v_layout.addWidget(center)
# center_v_layout.addWidget(down)

# right_v_layout.addWidget(right)


# main_h_layout.addLayout(left_v_layout)
# main_h_layout.addLayout(center_v_layout)
# main_h_layout.addLayout(right_v_layout)

# main_win.setLayout(main_h_layout)


# Вариант 2
main_v_layout = QHBoxLayout()

up_h_layout = QVBoxLayout()
center_h_layout = QVBoxLayout()
down_h_layout = QVBoxLayout()

left = QPushButton('1')
up = QPushButton('2')
down = QPushButton('3')
center = QPushButton('4')
right = QPushButton('5')

up_h_layout.addWidget(up)

center_h_layout.addWidget(left)
center_h_layout.addWidget(center)
center_h_layout.addWidget(right)

down_h_layout.addWidget(down)


main_v_layout.addLayout(up_h_layout)
main_v_layout.addLayout(center_h_layout)
main_v_layout.addLayout(down_h_layout)

main_win.setLayout(main_v_layout)


app.exec_()
