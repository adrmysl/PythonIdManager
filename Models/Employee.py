class Employee:
    def __init__(self, person):

        self.firstName = person["name"]
        self.secondName = person["secondName"]
        self.surname = person["surname"]
        self.dateOfBirth = person["dateOfBirth"]
        self.position = person["position"]
        self.endContract = person["endContract"]
