while True:
    try:
        entrada = int(input())
        if entrada > 0:
            print('vai ter duas!')
        else:
            print('vai ter copa!')
    except EOFError:
        break
