from enum import Enum 


class Type(Enum):
    S1 = 1
    S2 = 2/3
    S3 = 1/3
    S4 = 0


class Level:
    def __init__(self, type):
        self.type = type

    def levelDown(self):
        if self.type is Type.S4:
            self.type = Type.S3
        if self.type is Type.S3:
            self.type = Type.S2
        if self.type is Type.S2:
            self.type = Type.S1
        pass

    def levelUp(self):
        if self.type is Type.S1:
            self.type = Type.S2
        elif self.type is Type.S2:
            self.type = Type.S3
        elif self.type is Type.S3:
            self.type = Type.S4
        pass

    def getProb(self):
        return self.type.value
