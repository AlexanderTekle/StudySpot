class StudySpace(input):

    volume = ""
    foodOptions = []
    closeTime = "3:00 AM"
    groupConducive = False
    campus = ""


    def __init__(input):
        list = input.split("*")

        self.volume = int(list[0])
        self.foodOptions = list[1].split(",")
        self.closeTime = list[2]
        self.groupConducive = list[3]
        self.campus = list[4]

