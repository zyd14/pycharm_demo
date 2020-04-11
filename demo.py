from time import sleep
x = 3
y = 3

print(x+y)

# We can drop breakpoints anywhere in our code

def lalala():
    z = 5
    while z < 20:
        sleep(1)
        z += 1
        print(z)


if __name__ == '__main__':
    lalala()
