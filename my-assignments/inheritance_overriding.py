# Superclass - Parent
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce_self(self):
        print(f"My name is {self.name} and my age is {self.age}.")


# create two people and have them introduce themselves
person_1 = Person("Adriana", "28")
person_1.introduce_self()

person_2 = Person("Braus", "32")
person_2.introduce_self()

# create Student class

class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major
  
    def study(self):
        print(f"{self.name} studies {self.major}")

    def introduce_self(self):
        super(Student, self).introduce_self()
        print(f"I major in {self.major}")
    
# create a Student and have them introduce themselves

student_1 = Student("Danika", "28", "Computer Science")
student_1.introduce_self()

class Musician(Person):
    def __init__(self, name, age, favorite_song):
        super().__init__(name, age)
        self.favorite_song = favorite_song
        self.instruments = []
        
    def hum_tune(self):
        print(f"{self.name} hums {self.favorite_song}")
        
    def introduce_self(self):
        print(f"My name is {self.name} and my age is {self.age}. My favorite song is {self.favorite_song}.")
        
    def add_instrument(self, instrument):
        self.instruments.append(instrument)
        
    def play(self, times):
        for i in range(times):
            print(self.instruments[0].sound)
        
jeremiah = Musician(name="Jeremiah Chiu", age=30, favorite_song="Rococco Rondo")
jeremiah.hum_tune()
jeremiah.introduce_self()

class Instrument():
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        
synthesizer = Instrument("Synthesizer", "Beep, bop, boop!")

jeremiah.add_instrument(synthesizer)
jeremiah.play(4)


class Band():
    def __init__(self, name):
        self.name = name
        self.members = []
        
    def add_musician(self, musician):
        self.members.append(musician)
        
    def interview(self):
        print("Introducing... ")
        for member in self.members:
            member.introduce_self()
            
    def play_show(self, time_signature):
        for i in range(time_signature):
            for member in self.members:
                member.play(1)
            
    
band = Band(name="band")
band.add_musician(jeremiah)
band.interview()
band.play_show(2)