# TDD1_Assignment_1

The goal of this exercise is to demonstrate how to evolve the multiply example using a Test First approach, from the first test, through to the last test. 

If you are good with Git, commit after each refactor to keep the history of the evolution of your solution.  That way Git keeps your history for you. Otherwise, just comment  out the old code as your solution evolves.

Don't forget, this new approach might feel a bit like wearing new shoes, but as you practice it, the technique will become more familiar and comfortable.

outline of the steps to take( this can apply to both Javascript and Python language)

Setup ( Javascript):
1. Create a new node.js project
2. Install and configure a local copy of eslint.  Don't install it globally for reasons I mentioned before.
3. Install mocha as a dev dependency
4. Install chai as a dev dependency
5. Create a test directory
6. Create a test.js inside that test directory
7. Create a multiply.js
5. Update npm script to run tests using mocha

setup (Python):
for python make sure to use, Pytest, Pylint and Black.

Test First TDD Cycle 1
1. Red: Write your first test: assertEqual(multiply(1, 1), 1); in ./test/test.js
2. Red: Run the test.  Did it pass?  No!  Becasue you haven't written the multiply function yet!
3. Get the test to pass, by writing a multiply function, that is just enough code to pass the test, i.e. function multiply (a, b) { return 1;
} 
4. Run the test?   Does it pass?   Should do!  Now we are green!
5. Refactor?  Probably not necessary!

Test First TDD Cycle 2
1. Red. Write the next test. Run the tests: assertEqual(multiply(2, 2),4)
2. Green: Update multiply() to pass the second test.  Make sure the first test still passes too!
3. Do I need to refactor?  Nope, its pretty simple

Test First TDD Cycle 3
1. Red. Write the next test: assertEqual(3, 3), 9)
2. Red/Green:  Does it pass, maybe, depends on your solution.
3. Green: Update multiply() to pass the third test, if you need to.  Make sure you didnt break test 1 or test 2!  If you did, fix them.
4. Do I need to refactor?  Nope, its pretty simple

Fourth Test Cycle
1. Red.  assertEqual(4, 4), 16)
2. Oh!  Its green!

Fifth Test Cycle
1. Red:  assertEqual(23, 45), 23 * 45)
2. Oh! Its till green!
