# ekinox technical test
## Back to the futur DVDs market

### Run code
> python3 main.py

#### Note:
* As input, a shooping cart in the text format, separated by line breaks which contains the name of the films purchased
* As output, the number representing the total price

### Run unittests 
> python3 -m unittest test_dvds_market

### DVDs prices 
* Saga serie (Back to the futur films): 15 euros
* Other films: 20 euros

### Discount rules 
* Rule 1: for the purchase of 2 DIFFERENT parts of the saga, a 10% discount is applied to all "Back to the Future" DVDs purchased
* Rule 2: for the purchase of 3 DIFFERENT parts of the saga, we apply a 20% discount on all "Back to the Future" DVDs purchased

### Some examples of inputs and outputs
#### Example #1

input:

Back to the Future 1

Back to the Future 2

Back to the Future 3

Output:

36

#### Example 2

input:

Back to the Future 1

Back to the Future 3

Output:

27

#### Example #3:

Input:

Back to the Future 1

Output:

15

#### Example #4:

Input:

Back to the Future 1

Back to the Future 2

Back to the Future 3

Back to the Future 2

Output:

48

Explanation :

((15*4)*0.8) = 48

#### Example #5

Input:

Back to the Future 1

Back to the Future 2

Back to the Future 3

The goat

Output:

56

#### Explanation :

((15*3)*0.8)+20 = 56
