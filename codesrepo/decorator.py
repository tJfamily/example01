
def hello_world(f):
    def decorated(*args, **kwargs):
        print('hello world!')
        f(*args, **kwargs)

    return decorated


@hello_world
def multiply(x, y):
    print(x*y)


@hello_world
def ndict(**kwargs):
    for key, value in kwargs.items():
        print(key+'='+value)


if __name__ == "__main__":
    multiply(3, 4)
    ndict(name='jessica')

