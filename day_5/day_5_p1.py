# Crates moved in each step - varying stacks of crates 
# crates can only be moved one at a time 
#after all steps , which crate will be on top of each stack?
# Start pos
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# [D]        
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 


# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
#         [Z]
#         [N]
#         [D]
# [C] [M] [P]
#  1   2   3

def parse_instruction(instruction):
    words_list = instruction.split()
    numbers = words_list[1::2]
    a = int(numbers[0])
    b = int(numbers[1])
    c = int(numbers[2])
    return a,b,c

def move_crate(crate_stacks,instruction):
    #move 1 from 2 to 1#
    pass

def move_crates(crate_stacks,instructions):
    pass 