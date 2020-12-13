
def war(name):
    class Counting:
        first = 0
        second = 0
        answer = 0

        # constructor
        def __init__(self, f, s):
            self.first = f
            self.second = s

        def display(self):
            print("The first wave attack brought on this many deaths = " + str(self.first))
            print("The second wave attack brought on this many deaths = " + str(self.second))
            print("The third and fourth attacks brought this many deaths = " + str(self.answer))

        def calculate(self):
            self.answer = self.first + self.second


    obj = Counting(1000, 3000)
    # perform Addition
    obj.calculate()

    # display result
    obj.display()
