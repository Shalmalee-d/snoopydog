
def simple_reflex_agent(loc, status):
    if status == 'dirty':
        return 'suck'
    elif loc == 'a':
        return 'right'
    else:
        return 'left'

def vaccum_cleaner(loc, world,steps=6):
    performance= 0
    for t in range (steps):
        status=world[loc]
        action=simple_reflex_agent(loc, status)

        print(f"t={t},loc={loc},Status={status},Action={action}")

        if action == 'suck':
            world[loc]='clean'
        elif action=='right':
            loc='b'
        else:
            loc='a'

        performance += sum(s=='clean'for s in world.values())

    print("\nFinal State of Rooms")
    print ("Room A:", world['a'])    
    print ("Room B:", world['b']) 

    return performance
loc = input("enter starting location (a/b):").lower()
status_a = input("enter status of a(clean/dirty):").lower()
status_b = input("enter status of b(clean/dirty):").lower()
steps=int(input('enter no. of steps:'))
world={'a': status_a, 'b': status_b}

print("\nTotal Performance:", vaccum_cleaner(loc,world,steps))