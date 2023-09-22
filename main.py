from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup, QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QRadioButton, QGroupBox
from random import *
#create a memory card application

class Question():
    def __init__(self, question, right, w1, w2, w3):
        self.question = question
        self.right = right
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3

question_list = []

question_list.append(Question("What food do i like", "steak", "vegetable", "pizza", "chicken"))
question_list.append(Question('What is the tallest building in the world', "burj khalifa", "Landmark 81", "shangai tower", "My grandma house"))
question_list.append(Question('what is the deepest point in the world', "mariana trench", "tonga trench", "Kermadec trench", "Your dad basement"))
question_list.append(Question('What is the smallest country in the world', "vatican city", "Your dad basement","barbados","monoco"))
question_list.append(Question('What do you call a person without a body and a nose', "Nobody knows", 'Idk', "Stupid quesiton unanswerable","No"))
question_list.append(Question('What do you call a cow with no legs', "Ground beef", "cow", "legs", "walk"))
question_list.append(Question('What do you call a fly without wings', "Walk", "no fly", "fly", "no wall"))
question_list.append(Question("If 2 vegans were arguing would it still be considered beef", "Tomato", "Idk", "brainmelt", "dead"))
question_list.append(Question('Which orange came first', "Fruit", "color","Orange","Your mom"))
question_list.append(Question('You are driving down the street with your car. 2 people went in front of you, a baby and an old man what would you hit', "The brakes", "old man", "baby","no"))


shuffle(question_list)

app = QApplication([])
window = QWidget()
window.setWindowTitle("General knowledge")
window.resize(500, 400)

question_text = QLabel("What is the smallest country in the world")
radioGroup = QGroupBox('Answer Options:')
ansGroup = QGroupBox('Results')
ansradio1 = ("Vatican city")
radio1 = QRadioButton('Vatican city')
radio2 = QRadioButton('Popua new guinea')
radio3 = QRadioButton('Monoco')
radio4 = QRadioButton('not here')
btn = QPushButton('Answer')
buttonGroup = QButtonGroup()
buttonGroup.addButton(radio1)
buttonGroup.addButton(radio2)
buttonGroup.addButton(radio3)
buttonGroup.addButton(radio4)
score_label = QLabel("Score:0")
total_label = QLabel('Total:0')

results_text = QLabel('Correct or incorrect')
correct_text = QLabel('Answer will be ere soon...')

ans_col = QVBoxLayout()
ans_col.addWidget(results_text, alignment=Qt.AlignCenter)
ans_col.addWidget(correct_text, alignment=Qt.AlignCenter)




row1 = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(radio1)
col1.addWidget(radio2)

col2.addWidget(radio3)
col2.addWidget(radio4)

row1.addLayout(col1)
row1.addLayout(col2)

radioGroup.setLayout(row1)
ansGroup.setLayout(ans_col)

r1 = QHBoxLayout()
r2 = QHBoxLayout()
r3 = QHBoxLayout()
r4 = QHBoxLayout()
r5 = QHBoxLayout()
r1.addWidget(question_text, alignment=Qt.AlignCenter)


r2.addWidget(radioGroup)
r2.addWidget(ansGroup)

r3.addWidget(score_label, alignment=Qt.AlignCenter)
r4.addWidget(total_label, alignment=Qt.AlignCenter)
ansGroup.hide()
r5.addWidget(btn)

master = QVBoxLayout()
master.addLayout(r1)
master.addLayout(r2)
master.addLayout(r3)
master.addLayout(r4)
master.addLayout(r5)




window.setLayout(master)



def show_answer():
    radioGroup.hide()
    ansGroup.show()
    btn.setText('Next Question')


def show_question():
    ansGroup.hide()
    radioGroup.show()
    btn.setText('Answer')

    buttonGroup.setExclusive(False)
    radio1.setChecked(False)
    radio2.setChecked(False)
    radio3.setChecked(False)
    radio4.setChecked(False)
    buttonGroup.setExclusive(True)





answers = [radio1, radio2, radio3, radio4]


def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right)
    answers[1].setText(q.w1)
    answers[2].setText(q.w2)
    answers[3].setText(q.w3)
    question_text.setText(q.question)
    correct_text.setText(q.right)
    show_question()



def next_question():
    window.total += 1
    print("Statistiics:\n-Total Question", window.total,"\n-Correct Answers:", window.score)
    current = randint(0, len(question_list)-1)
    q = question_list[current]
    ask(q)
    



def show_correct(res):
    results_text.setText(res)
    show_answer()

def check_answer():
    if answers[0].isChecked():
        show_correct("Correct! Congrats you just escaped from being an idiot, this question is hard. This shows that u have gone to school, touch grass and go outside")
        window.score += 1
        score_label.setText("Score:" +str(window.score))
        total_label.setText("Total:" +str(window.total))
        print("Statistiics:\n-Total Question", window.total,"\n-Correct Answers:", window.score)
        print("Rating: ", round(window.score/window.total*100,1), "%" )
        total_label.setText("Total:"+str(round(window.score/window.total*100, 1)))
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Inccorect, skill issues touch some grass go outside, go to school, ur trash like literally this is the easiest question on the world")
            print("Rating: ",  round(window.score/window.total*100,1), "%" )
            total_label.setText("Total:"+str(round(window.score/window.total*100,1)))

def test():
    if btn.text() == "Answer":
        check_answer()
    else:
        next_question()

window.total = 0
window.score = 0

btn.clicked.connect(test)

next_question()









window.show()
app.exec_()