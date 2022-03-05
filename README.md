# Coding exercise

This is a basic coding exercise created by the (UK) Cabinet Office.

### Installing

(Please note, where `python` is referred to, use `python` or `python3` as appropriate for your environment.)

Begin by cloning this repository. Next, change-directory to be in the coding-exercise folder and install dependencies:

```
python -m pip install -r requirements.txt
```

### Launching the application

To run the application, you can do the following in the top-level exercise/ directory:

```
python manage.py runserver
```

You can then call the three endpoints (using either a web browser or a REST client application):

- /hello/
- /add-numbers/&lt;first-number&gt;/&lt;second-number&gt;/
- /join-words/&lt;first-word&gt;/&lt;second-word&gt;/

### Examples

- /hello/
  - Returns `Hello World`
- /add-numbers/10/20/
  - Returns `30`
- /join-words/hello/there/
  - Returns `hello-there`

### Tests

You can run the test-suite (again in the top-level exercise/ directory) via:

```
python manage.py test tests/ --noinput
```

---

Original README and exercise-instructions are found in the original repo.
