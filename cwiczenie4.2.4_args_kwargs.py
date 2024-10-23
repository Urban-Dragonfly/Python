def count_them_all(*args, **kwargs):
    positional_args_count = len(args)
    print(f"I have received {positional_args_count} positional arguments")
    key_args_count = len(kwargs)
    print(f"I have received {key_args_count} keyword arguments")

count_them_all(1, 2, 3, "A", a=1, b=2)

help(count_them_all)