__author__ = 'Ryang Kun'

from time import sleep

print("Ingredients of Dalgona_Coffee")
print("Milk 150mL, Coffee (Americano) 25g, Salt 25g, Warm Water 25mL")
print("Press A to start.")
is_ready = input()
if is_ready == "A":
    print("Put Prepared Coffe Mix into a cup.")
    sleep(15)
    print("Pour prepared salt next.")
    sleep(15)
    print("Pour your warm water.")
    sleep(15)
    print("The nest would be rough to do.")
    sleep(2)
    print("Mix everything in the cup with a spoon 400 times.")
    print("Next step come after 3 min.")
    sleep(180)
    print("Fianl Step!")
    print("Enjoy Your Coffee")
    sleep(5)
else:
    print("Press A then Enter to view next.")
    sleep(3)