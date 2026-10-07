class Animal:
    def speak(self):
        pass

class Dog (Animal):
    def speak(self):
        return "汪汪汪"

class Cat (Animal):
    def speak(self):
        return "喵喵喵"

def sound(animal):
    print(animal.speak())

dog=Dog()
cat=Cat()
sound(dog)
sound(cat)