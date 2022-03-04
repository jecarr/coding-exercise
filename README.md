# Coding exercise

This is a basic coding exercise created by the (UK) Cabinet Office.

Install dependencies

```
python(3) -m pip install -r requirements.txt
```

Run application

```
python(3) manage.py runserver
```

Original instructions are below:

---

Clone this repository and commit your work to it.  Push the repository to a suitable service so that we can see the results (eg GitLab or GitHub).

Create an API using Python. The API should have three endpoints:

1. Return "Hello World"
2. Given two numbers, add them together and return the sum
3. Given two words, join them with a dash and return the result

If you have any questions, pick an answer and then document it.

You can use any Python framework or libraries that you want to.  There should be instructions on how to install and run it.  The API should ideally be platform independent but it will be evaluated on a recent MacOS machine.

Preferably there should be some tests.

The code should be neat and error free.  We use `black`, `isort` and `flake8` to keep our code neat.  You don't have to use this, but you may find it helpful.  You can install them by running: `pip install -U black isort flake8`.  We have included configuration in this repo.  You can run them using:

    black .
    isort .
    flake8 .

Don't worry if you can't complete all the tasks in the allotted time. Document your solution as it stands. We are interested in knowing how you write code and how you solve problems.

Things we will be judging the submission on:

* Documentation, including instructions on how to run your solution
* Correctness and completeness of solution
* Code quality
