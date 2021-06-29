#!/usr/bin/python3
from PyQt5.QtWidgets import QApplication, QPushButton, QTextEdit, QVBoxLayout, QWidget
from random import choice 
import sys

class story_window(QWidget):
    def __init__(self):
        super().__init__()
        
        top = 100
        left = 300
        width = 400
        height = 400
        self.setGeometry(left,top,width,height)
        self.setWindowTitle("Python Story Generator")
        
        self.setMinimumSize(width,height)
        self.setMaximumSize(width,height)
        self.vbox = QVBoxLayout()

        self.gen_story = QPushButton("Generate Story")
        self.gen_story.setGeometry(50,180,50,20)
        self.gen_story.clicked.connect(self.story_generator)

        self.story_area = QTextEdit()
        self.story_area.setReadOnly(True)
        self.story_area.setStyleSheet("font-size:18px;")


        self.vbox.addWidget(self.gen_story)
        self.vbox.addWidget(self.story_area)
        self.setLayout(self.vbox)
        self.show()



    def story_generator(self):
        self.story_area.clear()
        story_starter = [" About 100 years ago "," In the 17 BC "," In the 20 BC "," Once upon a time "," In 16th Century "]
        story_charactors = [" there lived a king "," there was a man named jack"," there was a old man named ronny "]
        story_plot = [" he was going to picnic ", " he was passing by "]
        places = [" at mountains "," at garden "," at bridge "," at zoo "," at jungle "]
        age = [' who seemed to be in late 20s', ' who seemed very old and feeble']
        second_character = [' he saw a man ', ' he saw a young lady '," he saw a old man "," he saw a old lady "," he saw a child "]
        time = [' One day', ' One full-moon night']
        work = [' searching something.', ' digging a well on roadside.']
        story = choice(story_starter)+choice(story_charactors)+".\n"+choice(time)+choice(story_plot)+".\n"+choice(places)+choice(second_character)+".\n"+choice(age)+choice(work)
        self.story_area.append(str(story))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = story_window()
    sys.exit(app.exec_())
    # story_generator()
