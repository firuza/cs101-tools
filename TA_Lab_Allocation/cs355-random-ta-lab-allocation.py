import random

unrestricted_tas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
restricted_tas = ["K", "L", "M", "N", "O"] #not in SL1

sl1_ta_count = 5
sl2_ta_count = 7
sl3_ta_count = 3

def allocate_tas():
        
    random.shuffle(restricted_tas)
    random.shuffle(unrestricted_tas)
    
    sl1_tas = random.sample(unrestricted_tas, sl1_ta_count)
    
    remaining_tas = [ta for ta in unrestricted_tas if ta not in sl1_tas] + restricted_tas   
    random.shuffle(remaining_tas)
    
    sl2_tas = random.sample(remaining_tas, sl2_ta_count)
    remaining_tas = [ta for ta in remaining_tas if ta not in sl2_tas]
    sl3_tas = remaining_tas
    
    return sl1_tas, sl2_tas, sl3_tas

def print_allocations():
    for week in range(1, 6):
        sl1, sl2, sl3 = allocate_tas()
        print(f"Week {week} allocation:")
        print(f"SL1: {sl1}")
        print(f"SL2: {sl2}")
        print(f"SL3: {sl3}")
        print("-" * 40)

# Call the function to display the allocations for 5 weeks
print_allocations()
