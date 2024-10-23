def customized_hello(first_name, last_name, gender_prefix='Mr'):
    """
        Prints hello, based on arguments passed
        Arguments:
        first_name,
        last_name
        Optional arguments:
        gender_prefix:  Mr/Ms based on sex of person
    """
    print("Hello %s %s %s" % (gender_prefix, first_name, last_name))

help(customized_hello)