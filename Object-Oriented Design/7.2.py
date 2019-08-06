# Call Center


class Employee:

    def __init__(self, level, name, age):
        self.level = level
        self.name = name
        self.age = age
        self.available = True

    def take_call(self):
        self.available = False

    def off_call(self):
        self.available = True

    def is_available(self):
        return self.available


class Respondent(Employee):

    def __init__(self, name, age):
        Employee.__init__(self, 'respondent', name, age)

    # Respondent functions...


class Manager(Employee):

    def __init__(self, name, age):
        Employee.__init__(self, 'manager', name, age)

    # Manager functions...


class Director(Employee):

    def __init__(self, name, age):
        Employee.__init__(self, 'director', name, age)

    # Director functions...


class CallCenter:

    def __init__(self, respondents, managers, directors):
        self.respondents = respondents
        self.managers = managers
        self.directors = directors

    def dispatch_call(self):
        for respondent in self.respondents:
            if respondent.is_available():
                respondent.take_call()
                print('Respondent {} on the line!'.format(respondent.name))
                return respondent

        for manager in self.managers:
            if manager.is_available():
                manager.take_call()
                print('Manager {} on the line!'.format(manager.name))
                return manager

        for director in self.directors:
            if director.is_available():
                director.take_call()
                print('Director {} on the line!'.format(director.name))
                return director

        print("Sorry but no service representatives are currently available, please try again later!")
        return


if __name__ == '__main__':
    call_center = CallCenter([Respondent('Brian', 49), Respondent('Tom', 25), Respondent('Hurley', 34)],
                             [Manager('Ryan', 40), Manager('Alex', 31)], [Director('Kosta', 35)])

    for _ in range(7):
        call_center.dispatch_call()
