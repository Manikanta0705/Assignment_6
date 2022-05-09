#let P(AB)= p_a_b
#let P(B)=b
#let P(A/B)= c
import random
p_a_b = random.random() #obtains random float between 0 and 1
b = 0
c = p_a_b/b
print('Probability of event P(A/B):',c)
