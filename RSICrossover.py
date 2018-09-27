import numpy as np
def rsiDBcross(rsi1, rsi2):
    states = np.zeros(len(rsi1))
    bought = 1
    sold = 1
    states[0] = 0
    for i in range(len(rsi1)-1):
        if(rsi2[i+1]>rsi1[i+1]):
            if (rsi2[i+1] - rsi1[i+1] > 5) & sold == 1:
                states[i+1] = 0
                bought = 1
                sold = 0
            elif (states[i] == 0) & (rsi2[i+1] - rsi1[i+1] > 5):
                states[i+1] = 0
            else:
                states[i+1] = 1
        else:
            if(rsi1[i+1] - rsi2[i+1] > 2) & (bought == 1):
                states[i+1] = 2
                bought = 0
                sold = 1
            elif (states[i] == 2) & (rsi1[i+1] - rsi2[i+1] > 5):
                states[i+1] = 2
            else:
                states[i+1] = 1
    return states





