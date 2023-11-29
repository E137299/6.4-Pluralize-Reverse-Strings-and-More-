# 6.4-Pluralize-Reverse-Strings-and-More-

## **Pluralize**
Create a function, pluralize(), that takes in a list of words and updates the values of the list to make each one plural. The function will return the updated list.
Making plurals in english has a number of special cases, but for this lab we'll use a simple rule: 
* If the word ends in a 'y' remove the 'y' and add 'ies'; otherwise add an 's'.

**Example:**

Function Call:
```
pluralize(["apple", "berry", "melon"])
```
Output:
```
["apples", "berries", "melons"]
```

<br></br><br></br>
## **Reverse Strings**
Create a function, reverse_strings(). This function will take in a list of strings and reverse the order of letters in each word. The function will return the updated list.

**Example:**

Function Call:
```
reverse_strings(["apple", "berry", "melon"])
```
Output:
```
["elppa", "yrreb", "nolem"]
```

<br></br><br></br>
## **Remove Duplicates**
Write a function,remove_duplicates(), that accepts a list of values and returns the same list with all duplicate elements removed.

**Example:**

Function Call:
```
remove_duplicates(["apple", "berry","apple", "melon", "melon", "apple"])
```
Output:
```
["apple", "berry", "melon"]
```

<br></br><br></br>
## **Shared Items**
Write a function,shared_items(), that takes two lists as arguments and returns True if they have at least three common element, otherwise returns False.

**Example One:**

Function Call:
```
shared_items([9,3,6,3,6,8,7,2],[0,2,7,2])
```
Output:
```
False
```


**Example Two:**

Function Call:
```
shared_items([9,3,6,3,6,8,7,2],[3,2,7,2])
```
Output:
```
True
```