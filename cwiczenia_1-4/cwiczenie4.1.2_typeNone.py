def day_times():
    return "morning", "afternoon", "evening", "night"

times = day_times()
print(times)
print(type(times))

def no_result_function():
    print("I am just printing I love you")
    print("and returning nothing to you!")
    return None
print("______________")
no_result_function()
print("______________")
print(type(no_result_function))
print("______________")
print(type(no_result_function()))