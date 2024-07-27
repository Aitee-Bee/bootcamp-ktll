random_one = ["toy", "ball", "pen", "bicycle", "basket"]
random_two =["bicycle", "basket", "gym"]

answer = [char for char in random_one if char not in random_two]
print(answer)