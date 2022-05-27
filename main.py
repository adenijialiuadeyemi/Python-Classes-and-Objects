class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)

    def change_name(self, new_name):
        print(f"{self.name} name has changed from {self.name} to the new name ",str(new_name))
    
    def change_age(self, new_age):
        print(f"{self.name} age has changed from {self.age} to the new age ",int(new_age))

    def add_track(self,new_track):
        new_track = self.tracks + [new_track]
        print(f"The new track list of {self.name} is ", new_track)
    
    def get_score(self):
        print (f"{self.name} score is {self.score}")


Bobs = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bobs.change_name("Peter")
Bobs.change_age(34)
Bobs.add_track("UI/UX")
Bobs.get_score()
