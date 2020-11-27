import random as rand
from main import crossed_array

# MUTACJA
def mutation(loop_count):
    for i in range(loop_count):
        random_index = rand.randint(0, len(crossed_array[0])-1)
        random_index2 = rand.randint(0, len(crossed_array[0])-1)
        random_value = rand.randint(-10, 10)

        # Podmiana wartości
        crossed_array[random_index][random_index2] = random_value
        # return muted_array
    return crossed_array
