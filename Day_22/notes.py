# class Animal:
#   def __init__(self):
#     self.num_eyes = 2

#   def breathe(self):
#     print("Inhale, exhale.")


# class Fish(Animal): #INHERIT ANMINAL CLASS
#   def __init__(self):
#     super().__init__() #CALL ATTRIBUTES

#   def breathe(self):
#     super().breathe()
#     print("Doing this underwater")

#   def swim(self):
#     print("moving in water.")


# nemo = Fish()
# nemo.swim()
# nemo.breathe()
# print(nemo.num_eyes)

piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

#SLICING
print(f"Initial list: {piano_keys[::2]}") #skip #skip #2

print(f"All values between index 2 and 5: {piano_keys[2:5]}")

print(f"All values up to index 5: {piano_keys[:5]}")

print(f"Every other index between 2 and 5: {piano_keys[2:5:2]}")

print(f"Every other index in the list: {piano_keys[::2]}") #skip #skip #2

print(f"Reverse a list: {piano_keys[::-1]}") 



