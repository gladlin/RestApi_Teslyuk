class RealString:
    def __init__(self, string1):
        self.value = string1
    
    def bigger(self, new_string):
        new_string = str(new_string)

        print(f"{len(self.value) > len(new_string)}")

    def smaller(self, new_string):
        new_string = str(new_string)
        print(f"{len(self.value) < len(new_string)}")
    
    def equals(self, new_string):
        new_string = str(new_string)
        print(f"{len(self.value) == len(new_string)}")

myString = RealString("value")
myString.equals("value")