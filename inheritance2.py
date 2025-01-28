#types of inheritance
# 1. Single Inheritance -> single child single parent
# 2. Multiple Inheritance -> more than 1 parent single child
#3. Multi level inheritance -> A -> B -> C
#4. Hierchichal Inheritance -> single parent more than 1 child
#5. Hybrid Inheritance -> combining more than 1 type of inherirtance


#example of single inheritance
class User: # user is parent class
    def __init__(self, name): #arguments
        self.name = name 

    def show(self): #methods
        print(f'{self.name} is a user')

class Admin(User): #admin child class
    def __init__(self, name, isAdmin):
        super().__init__(name)
        self.isAdmin = isAdmin

    def newShow(self):
        super().show()
        print(f'{self.name} is a admin : {self.isAdmin}')

# a = User('Rehnuma')
# a.show()

# b = User('Lucky')
# b.show()

a = Admin('John', True)
# a.newShow()

#multiple inheritance

class Camera:
    def __init__(self, mp):
        self.mp = mp

    def take_photo(self):
        print('photo captured', self.mp)

class MusicPlayer:
    def __init__(self, quantity):
        self.quantity = quantity

    def take_photo(self):
        print('playing music...',self.quantity)

class Phone(MusicPlayer, Camera):
    # def __init__(self, mp):
    #     super().__init__(mp)

    def take_photo(self):
        print('calling someone', self.quantity)

a = Camera(48)
a.take_photo()

b = MusicPlayer(50)
b.take_photo()

c = Phone(20)
c.take_photo()

#multi level inheritance

class GrandParent:
    def __init__(self, grandparent):
        self.grandparent = grandparent

    def grand(self):
        print('inside grandparent ', self.grandparent)

class Parent(GrandParent):
    def parent(self):
        print(self.grandparent)

class Child(Parent):
    def child(self):
        print(self.grandparent)

# a = GrandParent('Jon')
# a.grand()

# b = Parent('abc')
# b.parent()
# # # # b.grand()

# c = Child('def')
# c.child()
# # c.parent()
# # c.grand()