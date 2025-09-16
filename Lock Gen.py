#created by ItsOnlyCosmetic
#September 2025
from random import randint
from random import shuffle

"""the default uses emojies to make the output standardized
options are under the class
there are diferent types of pins this uses ranges from 0-9 for key pins and 1-8 for master pins you may have to ajust what you want for the types of locks you have.
"""

# lists
belt_list = ["yellow", "orange", "green", "blue", "purple"]
driver_pin_list_options = ["🔶", "🪚", "🧵", "🍄", "T-Pin", "Spool-errated", "Double mushroom", "Barrel", "Gin", "Tree"]
key_pin_list_options = ["🔶", "🪚", "🧵", "Type 4", "Type 5", "Type 6"]
spring_list_options = ["0️⃣","1️⃣","2️⃣",]
emoji_numbers = ["0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
# empty lists
key_pin_list = []
driver_pin_type_list = []
key_pin_type_list = []
master_pin_list = []
spring_list = []
pin_count_list = []
#list of lists
list_of_lists = [key_pin_list, driver_pin_type_list, key_pin_type_list, master_pin_list, spring_list, pin_count_list]
emoji_list_list = [pin_count_list, key_pin_list, master_pin_list, spring_list]
shuffle_list = [spring_list, key_pin_list, driver_pin_type_list, key_pin_type_list]


class LockBelt:
    """creates a belt from the options bellow"""
    def __init__(self):
        self.blue_plus = None
        self.key_pin_type_max_count = None
        self.key_pin_type_min_count = None
        self.key_pin_type_max = None
        self.driver_pin_type_max_count = None
        self.driver_pin_type_min_count = None
        self.driver_pin_type_max = None
        self.driver_pin_type_min = None
        self.max_pin_count = None
        self.min_pin_count = None
        self.key_pin_type_min = None
        self.key_pin_duplicate_quantity = 3
        self.green_plus = False
        self.purple_plus = False
        self.spring_type_min = None
        self.spring_type_max = None
        self.spring_type_min_count = None
        self.spring_type_max_count = None

    def pin_count_and_driver_setup(self, pin_min, pin_max, driver_type_min, driver_type_max, driver_type_count_min, driver_type_count_max):
        """asks for the minimum pin count, maximum pin count, what drivers you have using the range from the list driver_pin_list_options 0 - howmany types you have.
        then asks for the minimum non standard driver pins and maximum non standard driver pins.
        """
        self.min_pin_count = pin_min
        self.max_pin_count = pin_max
        self.driver_pin_type_min = driver_type_min
        self.driver_pin_type_max = driver_type_max
        self.driver_pin_type_min_count = driver_type_count_min
        self.driver_pin_type_max_count = driver_type_count_max

    def key_pin_setup(self,key_pin_type_min,key_pin_type_max,key_type_count_min,key_type_count_max):
        """asks for what key pin types you have min to max using the list key_pin_list_options 0 - howmany types you have.
        then asks for the minimum non standard key pins and maximum non standard key pins
        """
        self.green_plus = True
        self.key_pin_type_min = key_pin_type_min
        self.key_pin_type_max = key_pin_type_max
        self.key_pin_type_min_count = key_type_count_min
        self.key_pin_type_max_count = key_type_count_max

    def different_springs(self,spring_type_min,spring_type_max):
        """asks for how many spring types you have 0 - maxim count from list spring_list_options"""
        self.blue_plus = True
        self.spring_type_min = spring_type_min
        self.spring_type_max = spring_type_max

    def pinned_for_master(self):
        """sets master pins on for purple belt"""
        self.purple_plus = True

# belt options can be changed depending on desired difficulty or pin types you have
# Belt Options, uses the bellow options to create belts gree plus have more options first option is 0
yellow = LockBelt()
yellow.pin_count_and_driver_setup(3, 4, 0, 1, 0, 1)

orange = LockBelt()
orange.pin_count_and_driver_setup(4, 5, 0, 1, 2, 4)

green = LockBelt()
green.pin_count_and_driver_setup(5, 6, 0, 2, 3, 4)
green.key_pin_setup(0, 1, 2, 3)

blue = LockBelt()
blue.pin_count_and_driver_setup(5, 7, 0, 3, 5, 7)
blue.key_pin_setup(0, 1, 3, 4)
blue.different_springs(0,1)

purple = LockBelt()
purple.pin_count_and_driver_setup(5, 7, 0, 3, 5, 7)
purple.key_pin_setup(0, 1, 4, 5)
purple.different_springs(0,1)
purple.pinned_for_master()
#end of options
#sets a dictionary for all the belts to use as a variable
belt_list_dic = {
    "yellow": yellow,
    "orange": orange,
    "green": green,
    "blue": blue,
    "purple": purple,
}

def ask_for_dif():
    """asks for difficulty makes sure it's a valid choice"""
    difficulty_chosen = False
    while not difficulty_chosen:
        difficulty = input(f"Type your locks belt difficulty: {belt_list}: ").lower()
        if  difficulty in belt_list:
            return difficulty
        else:
            print("Error incorrect input")

def check_for_max_type(checked_list, driver_or_pin_type_list_options, min_range, max_range, min_type_limit, max_type_limit):
    """Asks for the list you are making,options above for a drier or key pin, the min and max range for the list type from the options. and the min and max quantityfor the requested pin type"""
    if len(checked_list) - checked_list.count("🔶") < min_type_limit:
        return checked_list.append(driver_or_pin_type_list_options[randint(1, max_range)])
    elif len(checked_list) - checked_list.count("🔶") != max_type_limit:
        return checked_list.append(driver_or_pin_type_list_options[randint(min_range, max_range)])
    else:
        return checked_list.append("🔶")

def num_emoji(num_list):
    """converts lits of numbers into emojies"""
    i = 0
    for number in num_list:
        if number != "🚫":
            num_list[i] = emoji_numbers[int(number)]
        i += 1

def set_pins(dif):
    """uses the difficulty and belt options above to generate a lock"""
    diff = dif
    dif = belt_list_dic[diff]
    pin_count = randint(dif.min_pin_count, dif.max_pin_count)

    for pin in range(pin_count):
        # adds a pin counter to the pin number list
        pin_count_list.append(pin+1)
        check_for_max_type(driver_pin_type_list, driver_pin_list_options, dif.driver_pin_type_min,
                           dif.driver_pin_type_max, dif.driver_pin_type_min_count,
                           dif.driver_pin_type_max_count)
        max_dup_pin = False
        new_pin = randint(0, 9)
        #makes sure the max pin ount has not been reached from the limit set by key_pin_duplicate_quantity
        while not max_dup_pin:
            if key_pin_list.count(new_pin) == dif.key_pin_duplicate_quantity:
                new_pin = randint(0, 9)
            else:
                key_pin_list.append(new_pin)
                max_dup_pin = True

        if dif.green_plus:
            check_for_max_type(key_pin_type_list, key_pin_list_options, dif.key_pin_type_min,
                               dif.key_pin_type_max, dif.key_pin_type_min_count,
                               dif.key_pin_type_max_count)

        #generates and adds a spring to the spring list
        if dif.blue_plus:
            spring_list.append(randint(dif.spring_type_min,dif.spring_type_max))

    #shuffles lists that were limited by count so that their position is random
    for lists in shuffle_list:
        shuffle(lists)

    # this desides how big the master pinis depending on the size of the key pin. it prevents it from going over but does not max out the pin hight every time.
    if dif.purple_plus:
        for pin in key_pin_list:
            too_large = True
            while too_large:
                master_pin = randint(1,8)

                if pin == 9:
                    master_pin_list.append("🚫")
                    too_large = False
                elif pin == 8:
                    master_pin_list.append("1")
                    too_large = False
                elif pin + master_pin > 8:
                    pass
                else:
                    master_pin_list.append(master_pin)
                    too_large = False

    #sets key pins that are smaller than 2 to standard instead of something else
    if dif.green_plus:
        for pin in range(len(key_pin_list)):
            if key_pin_list[pin] < 2:
                key_pin_type_list[pin] = "🔶"

    for lists in emoji_list_list:
        num_emoji(lists)

    #prints the results
    print("\n" * 20)
    print(
        f"You have selected a {diff.title()} Belt lock with {pin_count} pins, make sure you select correctly matching "
        f"key pins and driver pins so your spring is not too low.\nPin Number: \t\t{pin_count_list}\nKey Pin height:\t\t"
        f"{key_pin_list}")
    if dif.purple_plus:
        print(f"master Pin height:\t{master_pin_list}")
    if dif.green_plus:
        print(f"Key Pin type:\t\t{key_pin_type_list}")
    print(f"Driver Pin type:\t{driver_pin_type_list}")
    if dif.blue_plus:
        print(f"spring type:\t\t{spring_list}")
    print("\n")

    # resets the lists
    for lists in list_of_lists:
        lists.clear()

    set_pins(ask_for_dif())

set_pins(ask_for_dif())
