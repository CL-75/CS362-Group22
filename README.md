# Motivation

The goal of this portion of the group project is to implement the provided specification, while using a Continuous Integration workflow. You will need to work as a team as individual members are not able to merge their own changes into the main branch. You will also have the opportunity to utilize the myriad of testing techniques we have discussed. It is important you take this project seriously, as it may be the most realistic experience with a real-world team workflow you have in the program.

## Course Learning Outcome(s):
* **Apply** automated tools such as make and CVS in a realistic setting (CLO 1)
* **Apply** testing techniques for validating and measuring the quality of software (CLO 4)
* **Use** appropriate techniques and tools, including a debugger, to locate program faults (CLO 5)
* **Participate** effectively in a software inspection/code review (CLO 7)
* **Participate** effectively in a team environment (CLO 8)

## Module Learning Outcome(s):
* **Use** a Continuous Integration workflow to work with a team
* **Apply** effective Code Review techniques
* **Apply** a variety of testing techniques to verify a software implimentation

# Description
For this project, you and your team will have to implement three functions based on the specifications laid out below. All of your code must be housed in the same file, called `task.py`. This will ensure that everyone has to work on the same file, increasing the chances of merge conflicts. While this may seem counter intuitive, this is a learning exercise and part of the goal is to practice how to handle things when issues arise.

You are required to use the Continuous Integration workflow you set up in Part 1 of this project. Failure to do so will result in lost points. This means that you are not permitted to change the branch rules to allow for merging without Code Reviews.

You are not permitted to use any Python built-in/library that could make these tasks trivial. Some of these are explicitly forbidden, but it is impossible to list them all so you need to use your judgement and when there is any doubt, ask.

## Function 1 Specification
This function must have the following header: `def conv_num(num_str)`. This function takes in a string and converts it into a base 10 number and returns it. It has the following specifications:
* Must be able to handle strings that represent integers
* Must be able to handle strings that represent floating point numbers
* Must be able handle hexadecimal numbers with the prefix `0x`
    * Must be case insensitive
    * Negative numbers are indicated with a `-` like `-0xFF`
* The type returned must match the type sent. For example, if an string of an integer is passed in, `conv_num` must return an `int`.
* Invalid formats should return `None`, including, but not limited to:
    * strings with multiple decimal points
    * strings with alpha that aren't part of a hexadecimal number
    * strings with a hexadecimal number without the proceeding `0x`
    * values for `num_str` that are not strings or are empty strings

Some examples:
* `conv_num('12345')` returns `12345`
* `conv_num('-123.45')` returns `-123.45`
* `conv_num('.45')` returns `0.45`
* `conv_num('123.')` returns `123.0`
* `conv_num('0xAD4')` returns `2772`
* `conv_num('0xAZ4')` returns `None`
* `conv_num('12345A')` returns `None`
* `conv_num('12.3.45')` returns `None`

You are ***not*** permitted to use any of the following: 
* `int()`
* `float()`
* `hex()`
* `literal_eval()`

## Function 2 Specification
This function must have the following header: `def my_datetime(num_sec)`. This function takes in an integer value that represents the number of seconds since the epoch: January 1st 1970. The function takes `num_sec` and converts it to a date and returns it as a string with the following format: `MM-DD-YYYY`. It has the following specifications:
* It may be assumed that `num_sec` will always be an `int` value
* It may be assumed that `num_sec` will always be a non-negative value
* Must be able to handle leap years

Some examples:
* `my_datetime(0)` returns `01-01-1970`
* `my_datetime(123456789)` returns `11-29-1973`
* `my_datetime(9876543210)` returns `12-22-2282`
* `my_datetime(201653971200)` returns `02-29-8360`

Your function handle all the computation itself. You are ***not*** permitted to use any library that can convert seconds to a date. This includes, but is not limitted to:
* datetime
* arrow
* moment
* maya
* delorean
* freezegun

## Function 3 Specification
This function must have the following header: `def conv_endian(num, endian='big')`. This function takes in an integer value as `num` and converts it to a hexadecimal number. The endian type is determined by the flag `endian`. The function will return the converted number as a string. It has the following specifications:

* It may be assumed that `num` will always be an integer
* Must be able to handle negative values for `num`
* A value of `big` for `endian` will return a hexadecimal number that is big-endian
* A value of `little` for `endian` will return a hexadecimal number that is little-endian
* Any other values of `endian` will return `None`
* The returned string will have each byte separated by a space
* Each byte must be two characters in length

Some examples:
* `conv_endian(954786, 'big')` returns `'0E 91 A2'`
* `conv_endian(954786)` returns `'0E 91 A2'`
* `conv_endian(-954786)` returns `'-0E 91 A2'`
* `conv_endian(954786, 'little')` returns `'A2 91 0E'`
* `conv_endian(-954786, 'little')` returns `'-A2 91 0E'`
* `conv_endian(num=-954786, endian='little')` returns `'-A2 91 0E'`
* `conv_endian(num=-954786, endian='small')` returns `None`

Your function must handle all the computation itself. You are ***not*** permitted to use any built-ins such as, but not limited to, `to_bytes`, `bytes`, or `unpack`. You also ***may not*** use helpers such as bin or hex.

# Hints
* You may write *helper* functions if you wish to assist with maintaining targeted code. For example, you may find writing a function to convert an integer to a binary then have a function that converts binaries into hexadecimal bytes.
* Each of these functions has some tricky nuances so it is important to discuss them as a team
* You will not have access to the tests we will use to grade your implementations. Make sure you design a thorough test suite.
* A Continuous Integration workflow requires frequent commits, so, for the sake of your teammates, check for code reviews daily (if possible)

# What to turn in
For this part you will turn in the URL to your **private** GitHub repo that has `coeCS362` as a collaborator. Failure to have it be **private** or have `coeCS362` as a collaborator will result in an automatic 0 for the assignment.

# Grading Criteria
We will run your `task.py` hosted on your **private** GitHub repo (with `coeCS362` as a collaborator) against our own set of unit tests. Our test suite will attempt to trigger failures in your code. Your final score will for the autograded part will be determined by how many tests your code passes.

We will also examine your code for linting errors (shouldn't be a problem if you followed the described workflow).

We will also check to ensure that every team member contributed to the final codebase. If, during the project, you have a teammate that doesn't participate with the group, it is your responsibility to let the instructional team know as soon as possible.

If you wait until the last week to reach out to your group members that is not likely going to be allow us to waive the "everyone contributes" requirement. Please be aware that we will request detailed records of all communication/contact attempts to prove you made a good faith effort to work as a group. 

It is recommended that you as a group set an earlier "due date" from Canvas's. This will allow the group to avoid situations where it is the due date and your project is incomplete and you can't reach a group member. It is also recommended that you as a group are checking in your work regularly so if the worst happens, the group can pick up where someone left off and finish the work. Ultimately, the expectation is that the project will be complete and having a group member disappear is not an excuse (outside of documented emergencies).

Finally, we will verify that your **private** GitHub repo, that has `coeCS362` added as a collaborator, has utilized a Continuous Integration workflow. Failure to do so will result in significant point deductions.

# Resources
* [Converting Decimal to Hexadecimal](https://www.wikihow.com/Convert-from-Decimal-to-Hexadecimal)
* [What is a leap year?](https://www.timeanddate.com/date/leapyear.html)
* [Big Endian vs. Little Endian](https://www.geeksforgeeks.org/little-and-big-endian-mystery/)
