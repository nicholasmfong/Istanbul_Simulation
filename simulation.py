# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 08:27:17 2018

@author: Nicholas Fong
"""

import random
import matplotlib.pyplot as plt
import pandas as pd

def roll_2_dice():
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    return [x, y]

def reward(guess):
    if sum(roll_2_dice()) >= guess:
        return guess
    else:
        return 2

def reward_with_buff(guess):
    x, y = roll_2_dice()
    if (x + y) >= guess:
        return guess
    else:
        if (guess - max(x, y)) <= 4:
            return guess
        else:
            return reward(guess)

def simulator(num_simulations):
    scores = [0] * 11 # 2-12 inclusive is 11 values
    scores_with_buff = [0] * 11
    for i in range(num_simulations):
        for i in range(11):
            scores[i] += reward(i + 2)
            scores_with_buff[i] += reward_with_buff(i + 2)
    scores = [round(x / num_simulations, 3) for x in scores]
    scores_with_buff = [round(x / num_simulations, 3) for x in scores_with_buff]
    return pd.DataFrame([scores, scores_with_buff], index=['normal', 'buffed'], columns=range(2, 13))

def plot_results(size=14):
    fig, ax = plt.subplots()
    fig.set_size_inches(11.326, 7)
    plt.plot(result.T, marker='o')
    plt.title('Istanbul Simulation Results', fontsize=size)
    plt.xlabel('Guess', fontsize=(size - 2))
    plt.ylabel('Expected Value', fontsize=(size - 2))
    plt.legend(('normal', 'buffed'), fontsize=(size - 2))
    for i, value in enumerate(result.iloc[0]):
        ax.annotate(value, (result.columns[i], result.iloc[0, i]))
    for i, value in enumerate(result.iloc[1]):
        ax.annotate(value, (result.columns[i], result.iloc[1, i]))
    plt.show()
    
result = simulator(100000)
plot_results()
print(result.T)