
from flask import Flask, render_template, request
from datetime import datetime

class StudySpace:

    name = "";
    volume = ""
    foodOptions = []
    openTime = "8"
    closeTime = "3"
    groupConducive = False
    campus = ""
    distance = 0;
    count = 0;

    inputTime = ""
    inputDistance = ""
    inputVolume = ""
    inputFood = ""
    inputCampus = ""
    inputGroup = ""

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
        self.count = 0


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
    global inputTime
    inputTime = request.form['time']
    global inputDistance
    inputDistance = request.form['distance']
    global inputVolume
    inputVolume = request.form['volume']
    global inputFood
    inputFood = request.form['radio0']
    global inputCampus
    inputCampus = request.form['radio1']
    global inputGroup
    inputGroup = request.form['radio2']
    #inputs = [time, distance, volume, food, onCampus, group]
    #print(contents())
    print (inputTime + " " + inputDistance + " " + inputVolume + " " + inputFood + " " + inputCampus + " " + inputGroup)
    attributes()
    #print ("here")


    return render_template('form.html')

def attributes():

            #if 1 > 0 and 2 > 0:
         #   space.count = space.count + 1
          #  print(str(space.count))
    #update count
    for space in spaces:
        if int(inputTime) >= int(space.openTime) and int(inputTime) < int(space.closeTime):
            space.count = space.count + 1
        #if (inputTime >= openTime) and (time <= closeTime)
            #count+1

        if int(inputDistance) >= int(space.distance):
            space.count = space.count + 1
       # if inputDistance <= distance
           # count + 1
        if (inputVolume == '0' and space.volume == "Low") or (inputVolume == '1' and space.volume == "Medium") or (inputVolume == '2' and space.volume == "High"):
            space.count = space.count + 1
        #if (inputVolume == '0' and  volume == "Low") or (inputVolume == '1' and volume == "Medium") or (inputVolume == 2 and volume == "High")
            #count + 1
        if (inputCampus == "false" and space.campus == "Off") or (inputCampus == "True" and space.campus == "On"):
            space.count = space.count + 1
        #if (inputCampus == "False" and campus == "Off") or (inputCampus == "True" and campus == "On")
            #count + 1
        if (inputGroup == "True" and space.groupConducive == "True") or (inputGroup == "False" and space.groupConducive == "False"):
            space.count = space.count + 1
       # if (inputGroup == "True" and groupConducive == "True") or (inputGroup == "False" and groupConducive == "False")
            #count + 1
        print("" + space.name + " " + str(space.count))


def contents():
    spotLine = ""
    x = 0
    for space in spaces:
        spotLine += ""+  str(x) + space.name + space.volume + str(space.groupConducive) + str(space.campus) + str(space.distance)
        x + 1
    return spotLine




if __name__ == '__main__':
  app.run(debug=True)
