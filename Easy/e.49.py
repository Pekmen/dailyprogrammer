#!/usr/bin/env python3


from random import randint, shuffle

# step by step reenactment of true events!
def main():
    trials = 100000
    stay_wins = 0
    switch_wins = 0

    for i in range(trials):

        # 0 - goat, 1 - car
        doors = [0, 0, 1]
        shuffle(doors)
        
        # pick a door
        pick = randint(0, 2)
        
        # you made your choice
        stay_prize = doors.pop(pick)

        # are you sure, there is goat behind this random doors
        doors.pop(doors.index(0))

        # you switch for remaining doors
        switch_prize = doors[0]

        stay_wins += stay_prize
        switch_wins += switch_prize

    print("\nStay wins: {} (~{}%)".format(stay_wins, int((float(stay_wins) / trials) * 100)))
    print("Switch wins: {} (~{}%)\n".format(switch_wins, int((float(switch_wins) / trials) * 100)))



if __name__ == "__main__":
    main()