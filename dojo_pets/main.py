from classes.ninja import Ninja
from classes.pet import Pet

ozzy = Pet("Ozzy", "cat", "jumper")
helen = Ninja('Helen', "Miller", f"pet = {ozzy}", "temptations", "whiskas")

helen.feed_pet()
helen.walk_pet()
helen.bathe_pet()

ozzy.eat()
ozzy.sleep()
ozzy.play()
ozzy.noise()