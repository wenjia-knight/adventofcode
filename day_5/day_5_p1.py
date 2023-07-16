with open('input.txt') as file:
    lines = file.readlines()
    rucksacks = [line.strip() for line in lines]

print(rucksacks)
# def parse_instruction(instruction):
#     words_list = instruction.split()
#     numbers = words_list[1::2]
#     a = int(numbers[0])
#     b = int(numbers[1])
#     c = int(numbers[2])
#     return (a,b,c)

# def move_crate(crate_stacks,instruction):
#     #move 1 from 2 to 1#
#     pass

# def move_crates(crate_stacks,instructions):
#     pass 