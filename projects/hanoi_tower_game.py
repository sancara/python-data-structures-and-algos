from ..data_structures.stacks import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []

left_stack = Stack(name="Left")
middle_stack = Stack(name="Middle")
right_stack = Stack(name="Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Set up the Game

num_disks = int(input("How many disk do you want to play with?\n"))

while num_disks < 3:
  print("Enter a number greater than or equal to 3")
  num_disks = int(input("How many disk do you want to play with?"))

for num in range(num_disks, 0, -1):
  left_stack.push(num)
num_optimal_moves = round(2**num_disks-1,2)

print (f"The fastest you can solve this game is in {num_optimal_moves} moves")

#Get User Input

def get_input():
  choices = [stack.get_name()[0] for stack in stacks]
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print(f"Enter {letter} for {name}")
    user_input = input("").upper()
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]
        
#Play the Game
num_user_moves = 0

while right_stack.get_size() != num_disks:
  print("\n\n\n...Current Stacks...")
  for i in stacks:
    print(i.print_items())
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    if from_stack.is_empty():
      print("\n\nInvalid Move. Try Again")
    elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
    else:
      print("\n\nInvalid Move. Try Again")
    break
    

print(f"\n\nYou completed the game in {num_user_moves} moves, and the optimal number of moves is {num_optimal_moves}")
    

