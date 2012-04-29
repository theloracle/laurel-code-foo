def take_pop():
    # Function will interact with the user to learn the population
    # In: nothing
    # Out: Float of population
    
    while True:
        pop = raw_input("Please type the population: ")
        #Test user input
        try:
            pop = float(pop)
            if pop <= 0:
                raise ValueError
            return pop
        except ValueError:
            print "Please enter a valid number."
            continue

def plates(pop):
    # Function will determine the number of plates required with least excess
    # In: Float of population
    # Out: Strings of pattern, total plates, and excess plates

    count = 0
    pattern = ""
    #Pattern repeats every 26 with an additional letter
    while True:
        #1 number
        if (pop/10) <= 1:
            pattern += "1 number"
            total = str(10 + (count*26)) + " plates"
            excess = str(int(pop%(10 + (26*count)))) + " plates"
            break
        #2 numbers
        elif ((pop - 10)/10) <= 1:
            pattern += "2 numbers"
            total = str(20 + (count*26)) + " plates"
            excess = str(int(pop%(20 + (26*count)))) + " plates"
            break
        #1 letter
        elif (pop/26) <= 1:
            pattern = str(count+1) + " letters"
            total = str(26 + (count*26)) + " plates"
            excess = str(int(pop%(26 + (26*count)))) + " plates"
            break
        #Add another letter
        else:
            count += 1
            pop -= 26
            if count == 1:
                pattern = str(count) + " letter "
            else:
                pattern = str(count) + " letters "

    return pattern, total, excess
    
    
while True:
    pop = take_pop()
    pattern, total, excess = plates(pop)
    print "Population:    "+str(int(pop))+"\nPattern:       "+pattern+"\nTotal Plates:  "\
          +total+"\nExcess Plates: "+excess
    q = raw_input("Continue? (y/n): ")
    if q != "y":
        break
