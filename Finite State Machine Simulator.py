# FSM Simulation

edges = {(1, 'a') : 2,
         (2, 'a') : 2,
         (2, '1') : 3,
         (3, '1') : 3}

accepting = [3]

def fsmsim(string, current, edges, accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        currentState = (current, letter)
        if currentState in edges:
            nextState = edges[currentState]
            return fsmsim(string[1:], nextState, edges, accepting)
        else:
            return False
        # QUIZ: You fill this out!
        # Is there a valid edge?
        # If so, take it.
        # If not, return False.
        # Hint: recursion.


print (fsmsim("aaa111",1,edges,accepting))
# >>> True

