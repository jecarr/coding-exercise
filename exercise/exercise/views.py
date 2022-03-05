from django.http import HttpResponse, HttpResponseBadRequest

# Could only allow GETs (to imply incoming POSTs won't be processed) for these views?


def hello_world(request):
    """The REST endpoint to return 'Hello World'."""
    return HttpResponse("Hello World")


# Could supplement add_numbers() and join_words() with additional endpoints
# that take args in a POST request (rather than in the URL)


def add_numbers(request, num1, num2):
    """The REST endpoint to return the sum of two numbers.
    Limitations: Does not allow multiple minus signs (e.g. permits '-1' but not '--1').
    """
    # Put the arguments in a list (will use in sum() or for error-response)
    str_params = [num1, num2]
    # Convert the arguments into floats (to allow decimals); collate into new list; and sum the list
    try:
        result = sum([float(n) for n in str_params])
    except ValueError:
        # If any argument is not a number, return a 400 response
        return HttpResponseBadRequest("Non numerical value(s) supplied in url: " + ", ".join(str_params))
    # If all arguments were numbers, return the sum
    # For tidiness, remove trailing '.0's
    return_val = int(result) if str(result).endswith(".0") else result
    return HttpResponse(return_val)


def join_words(request, s1, s2):
    """The REST endpoint to return the concatenation of two strings."""
    # Return the two string-args with a dash joining them
    return HttpResponse("{}-{}".format(s1, s2))
