class Performer:
    def __init__(self):
        self.performer_id = ""
        self.name = ""
        self.age = 0
        self.expYear = 0
        self.dob = "19000101"

    def introduce(self, name, age):
        print("Hi! My name is {}.\nI'm {} years old.".format(name, age))

    def work(self, year):
        print("working like a bee for {} years".format(year))
        self.expYear += year

    def express(self):
        print("I\'ve worked for {} years".format(self.expYear))


if __name__ == '__main__':
    adam_lambert = Performer()

    adam_lambert.introduce('Adam Lambert', 36)

    adam_lambert.work(2)

    adam_lambert.work(5)

    adam_lambert.express()
