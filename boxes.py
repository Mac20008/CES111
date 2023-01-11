import math

items = int(input (f"Enter the number of items: "))
boxes = int ( input (f"Enter the number of items per box: "))

num_boxes = math.ceil(items / boxes)

print(f"For {items} items, packing {boxes}"
    f" items in each box, you will need {num_boxes} boxes.")
