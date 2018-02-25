# Bonus Practice: Subsets

# This assignment is not graded and we encourage you to experiment. Learning is
# fun!

# Write a procedure that accepts a list as an argument. The procedure should
# print out all of the subsets of that list.

guests = ["Elif", "Fatih", "Duman","Eda"] 

def partyTime(guests):
    
    tree = [[]]
    
    for guest in guests:
        
        for i in range(len(tree)):
            
            current = tree.pop(0)
            
            tree.append(current)
            tree.append(current + [guest])
        
    return tree
        
        
for possibility in partyTime(guests):
    print (possibility)