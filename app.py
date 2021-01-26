import os

def test(parameter_list: list) -> int:
    """method for testing type hint purposes

    Args:
        parameter_list (list): example list for enumerate

    Returns:
        int: example value for
    """
    x: int

    # TODO: jkshdfkjshdfksjhdf
    # FIXME: sdlkfsdlfkj
    # FIXED: dies und das
    # aslkdfjaslkjfasdlfkj
    #asdfklajsdflkj
    # HACK: testooo
    # INFO: bunlara dikkat et das muss man so machen
    # REVIEW: sdfklsdflkjsdflkjsdf

    for i in parameter_list:
        print(i)
        x=i
        return x


def test_two(kp):
    """
    Ein andere methode fürs testing
    """
    print("Hello test two")
    return int(6)

testo = [2,3,4,5,6,7]
test(testo)


print(test_two("fer"))
print(type(test_two("fer")))
print(test_two("fdf"))
