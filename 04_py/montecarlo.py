import random

def monte_carlo_pi(max_iter: int)->float:
    in_circle_count = 0

    for i in range(max_iter):
        x = random.random()*2-1
        y = random.random()*2-1
        if (x**2+y**2)**0.5<=1:
            in_circle_count += 1
    
    return 4*in_circle_count/max_iter

print(monte_carlo_pi(10000000))