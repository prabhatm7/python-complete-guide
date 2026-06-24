try:
    x = 10 / 0
except ZeroDivisionError as e:
    print("error", e)
else:
    print("no error")
finally:
    print("division completed")