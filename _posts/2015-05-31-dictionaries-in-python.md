

Dictionaries or hashmaps are incredibly useful data structures in Python. In this blog post, I will briefly cover this data structure.

## The basics

Dictionaries are used to hold key - value pairs. The 'key' is used to access the value in a very efficient manner - almost instantly for most purposes. Suppose you want to find the email address of a user according to their names. You can use a dictionary for this purpose:

To create a empty dictionary, use the following syntax:

```python
emails = {}
# or
emails = dict()

```

```dict``` is a class, similar to the ```list``` or ```set``` class you might have used before. Similar to the succinct way you create a list using ```[]```, you can create a dictionary using ```{}```


To create a dictionary with some initial data, you can use the following syntax:

```python
# one key-value pair
emails = {'name1' : 'email1'}

# two key-value pairs
emails = {'name1' : 'email1', 'name2' : 'email2'}

# you can also indent so it's more readable
emails = {
  'name1' : 'email1',
  'name2' : 'email2'
}

```

You can access a element in the dictionary by using the square bracket notation used while accessing list elements, except that you enter the key value, instead of a numeric index, like so:

```python
print emails['name1'] # prints email1
print emails['name2'] # prints email2
```

What happens when you try to access a element that isn't there?

```python
# try accessing a non-existent key
print emails['non-existent-name']
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  KeyError: 'non-existent-name'

```
As you'd expect, an error (```KeyError```) is raised when you try to access a non-existent element.

But how do you know whether a element exists or not? Simple: use the ```in``` keyword to test existence, as you'd do with lists or sets:

```python
print 'name1' in emails # prints True
print 'name2' in emails # prints True

# Simple way to check if element exists
somekey = '' # enter any value here
if somekey in emails:
  print somekey
else:
  print 'Element does not exist'
```

Now, to add elements to already created dictionaries, the syntax is similar to assigning to lists, except you don't have to worry about index limits like with lists and you can add non-int keys:

```python
# add a new key-value pair
emails['newname'] = 'newemail'

# prints newemail
print emails['newname']
```

Values are overwritten, if you reassign for some key:

```python
emails['newname'] = 'anotheremail'
# prints anotheremail
print emails['newname']
```
To find the number of key-value pairs in a dictionary, use the good-ol' ```len``` function:

```python
print len(emails)
```

To delete a key-value pair, just use the (good-ol') ```del``` keyword like so:

```python
a = {
  'k1' : 'v1',
  'k2' : 'v2'
}

# prints {'k2': 'v2', 'k1': 'v1'}
print a
# delete 'em
del a['k1']
# prints {'k2': 'v2'}
print a
```

The key type can be any type that is 'hashable'. int, float, string, bool, None are all hashable; whereas list and set aren't hashable types. To have a custom class as a key, you need to implement / override the ```__hash__``` method.



## Useful Methods

There are several methods in the dict class, which you can find in the [python docs](https://docs.python.org/2/library/stdtypes.html#typesmapping). I'll just cover a few which are used most while using dictionaries.

The  ```keys``` method returns the list of all keys in the dictionary:

```python
a = {
  'k1' : 'v1',
  'k2': 'v2'
}
# prints ['k1', 'k2']
print a.keys()
```

The ```values``` method returns the list of - you guessed it! - values.

```python
a = {
  'k1': 'v1',
  'k2': 'v2'
}
# prints ['v1, 'v2']
print a.values()

```

The ```clear``` method empties the dictionary:

```python
a = {
  'k1': 'v1',
  'k2': 'v2'
}
# prints {'k2': 'v2', 'k1': 'v1'}
print a
# clear it up
a.clear()
# prints {}
print a
```

The ```items``` method returns a list of (key, value) tuples. This is a very useful
way to access both the key and values, as we will see while discussing different ways to
iterate over dictionaries in the next section.

```python
a = {
  'k1': 'v1',
  'k2': 'v2'
}
# prints [('k2', 'v2'), ('k1', 'v1')]
print a.items()
```

The ```update``` method is used to merge 2 dictionaries - A & B. If there is a key in B that
doesn't exist in A, then the key-value pair is copied over, otherwise A's key-values are
overwritten.

That is:

```python
a = {
  'k1': 'a1',
  'k2': 'a2'
}

# k2 is common in both a & b
b = {  
  'k2': 'b2',
  'k3': 'b3'
}

# k2 is overwritten a, and a new key k3 is added in a
a.update(b)

# prints {'k3': 'b3', 'k2': 'b2', 'k1': 'a1'}
print a
```

The ```get``` method is similar to the ```dictionary[key]``` access method.
With one difference, a ```KeyError``` is not raised when the key doesn't exist; instead
when a key doesn't exist, ```None``` is returned:

```python
a = {
  'k1': 'a1',
  'k2': 'a2'
}

# prints a1
print a.get('k1')
# prints a2
print a.get('k2')
# Does NOT raise a KeyError, instead returns None
print a.get('non-existent-key')
```

If you want another value instead of None to be returned, then you can pass another
parameter to the get method, and that value is returned if that key doesn't exist.

```python
a = {
  'k1': 'a1',
  'k2': 'a2'
}

# prints None
print a.get('non-existent-key')
# prints 'default-value'
print a.get('non-existent-key', 'default-value')
```

## Iterating over dictionaries

There are many ways to iterate over dictionaries, the simplest way is to use the ```for ... in ... :``` loop, which allows access to the keys :

```python
for key in emails:
  print key, emails[key]
```

This is equivalent to using ```.keys()``` on the dictionary:

```python
for key in emails.keys():
  print key, emails[key]
```

To iterate over the values (you can't access the key here):

```python
for value in emails.values():
  print email
```

To iterate over both keys and values in an easy way, use the following lines of code. This is mostly how I personally iterate over a dictionary:

```python
for key, value in emails.items():
  print key, value
```

- **Important** Note: Order is **not** maintained in dictionaries.


## Useful stuff
To make the best use of dictionaries, take note of the following:

### Initializing a dictionary
You already know how to create a dictionary -

```python
# empty dictionary
a = {}
#or
a = dict()

# some elements
a = {
  'k1' : 'v1'
}

```

There's another way to initialize a dictionary, which may be useful sometimes:

```python
a = dict([('k1', 'v1'), ('k2', 'v2')])
```

### Checking existence and accessing key-value pairs

If you want check if a key exists, here is one way to do this:

```python
a = {}
if 'key' in a:
  # do something
  value = a['key']
  print value
else:
  print "key doesn't exist"
```

This is another way (Which is the best way, if you ask me):

```python
a = {}
value = a.get('key')
if value:
  print value
else:
  print "key doesn't exist"
```

### Counting occurrences in a sequence
This is a neat way to count how many times a letter / element has occurred:

```python
def counter(seq):
  count = {}
  for elem in seq:
    count[elem] = count.get(elem, 0) + 1
  return count

s = 'Hello World!!'
# prints :  {'!': 2, ' ': 1, 'e': 1, 'd': 1, 'H': 1, 'l': 3, 'o': 2, 'r': 1, 'W': 1}
print counter(s)

# prints {1: 3, 2: 3, 3: 1, 4: 2, 53: 1, 54: 1, 25: 1}
ll = [1,1,1,3,4,2,54,2,2,4,25,53]
print counter(ll)
```

- Note: There is a very useful class called ```Counter``` in the collections
module, check it out - it's pretty useful in some cases.


### ```OrderedDict```

As you already know, ```dict```s don't maintain order of insertion. However,
some times, order of insertion may be important. In these cases, you can use
an ```OrderedDict``` instead of a dict. The functionality of both classes are similar, except that order of insertion is maintained in OrderedDict.

Here's an example:

```python
from collections import OrderedDict

a = OrderedDict()
a['first'] = 'value'
a['second'] = 'value'
a['third'] = 'value'
a['fourth'] = 'value'

print a
del a['second']
print a
```
