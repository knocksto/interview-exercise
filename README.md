# Client Coding Exercise For Python Developer Role

## Problem Statement:
Using nothing but a list of negative words, create a program that performs sentiment analysis by counting the number of occurrences of the negative words in a text excerpt and using that number against the total number of words to calculate a percentage. 
The result should then match the **following criteria**:  

**<=5%  -> POSITIVE**  
**5-20% -> NEUTRAL**  
**>=20% -> NEGATIVE**

**Note 1: Words shorter than 3 characters in the text excerpt should not be considered.**  

**Note 2: Only spaces, commas, fullstops and exclamation marks, where necessary, should be used as delimiters when extracting words from the text input.**  
  
Please use the following negative word list to run tests with the given examples:   
**[bad, ugly, terrible, awful, stupid, mad, angry, sad]**
___
### Examples:
___
> ***Input 1:*** The world is a terrible place to live in. Terrible!  
***Output 1:*** **NEGATIVE**  

> ***Input 2:*** Today I saw a bunch of beautiful butterflies and they all looked so happy! All except for one that looked a bit sad and lonely.  
***Output 2:*** **POSITIVE**  

> ***Input 3:*** I'm going shopping and I'm super excited. The terrible thing is that the boots I wanted are no longer in sale, which makes me a bit angry, because I now have to pay full price.  
***Output 3:*** **NEUTRAL**  


### Your Task is to:
1. Fork the repo and create a branch with your first name.  
2. Come up with a solution to the problem above. Your solution should accept a text excerpt and return the right sentiment based on the criteria above.
3. Create a Pull Request to the main branch


### Testing
You are required to write unit test for your solution using [Testplan](https://testplan.readthedocs.io/en/latest/introduction.html) (a multi-testing framework)

A basic example of Testplan in action can be found on their [Git Repo](https://github.com/morganstanley/testplan)  

#### Good luck !!!
