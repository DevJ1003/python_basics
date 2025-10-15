# Difference:
# rfind() → returns -1 if not found.
# rindex() → raises ValueError if not found.

a = "Harry potter and the Prisoner of Jodhpur"
print(a.rindex("r", 1, 25))