def A():
    return "Hello " + B()


def B():
    return "my " + C()


def C():
    return "friends"


print(A())
