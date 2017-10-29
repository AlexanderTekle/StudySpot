
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
    count = 0;

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
    food = request.form['radio0']
    onCampus = request.form['radio1']
    group = request.form['radio2']
    #my_array = [time, distance, volume]
    print(contents())
    print (time + " " + distance + " " + volume + " " + food + " " + onCampus + " " + group)
   # attributes()


    return render_template('form.html')

def contents():
    spotLine = ""
    x = 0
    for space in spaces:
        spotLine += ""+  str(x) + space.name + space.volume + str(space.groupConducive) + str(space.campus) + str(space.distance)
        x + 1
    return spotLine


if __name__ == '__main__':
  app.run(debug=True)
