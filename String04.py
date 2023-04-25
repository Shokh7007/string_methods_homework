def main(s):
    """
    A variable of type str is given. make sure all letters are lowercase.
    Args:
        s: str
    Returns:
        bool: answer
    """
    if s==s.lower():
        return True
    else:
        return False
print(main("Dhhtfgh"))