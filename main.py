
from pet import Pet
my_pet = Pet("Meleys")

my_pet.get_status()

# Feed the pet
my_pet.eat()

# Put the pet to sleep
my_pet.sleep()

# Play with the pet
my_pet.play()

# Try to train the pet with some tricks
my_pet.train("roll over")
my_pet.train("sit")
my_pet.train("roll over")  # Trying to teach the same trick again

# Show all learned tricks
my_pet.show_tricks()

# Final status check
my_pet.get_status()
