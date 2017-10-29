
from flask import Flask, render_template, request
from datetime import datetime

class StudySpace:

    name = "";
    volume = ""
    foodOptions = []
    openTime = "8:00 AM"
    closeTime = "3:00 AM"
    groupConducive = False
    campus = ""
    distance = 0;

    def __init__(self, input):
        list = input.split("*")
        self.name = list[0]
        self.volume = list[1]
        self.foodOptions = list[2].split(",")
        self.openTime = list[3]
        self.closeTime = list[4]
        self.groupConducive = list[5]
        self.campus = list[6]
        self.distance = int(list[7])

file = open("studySpaces.txt", "r")
spaces = []

for line in file:
    spaces.append(StudySpace(line))

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('form.html')

@app.route('/', methods = ['POST'])
def home2():
    time = request.form['time']
    distance = request.form['distance']
    volume = request.form['volume']
    print (time + distance + volume)
    return render_template('form.html')


if __name__ == '__main__':
  app.run(debug=True)
