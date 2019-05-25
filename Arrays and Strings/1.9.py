# String Rotation


def string_rotation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    s = s1 + s1

    return isSubstring(s, s2)   # isSubstring method part of problem statement
