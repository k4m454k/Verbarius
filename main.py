from verbarius import get_time_string


if __name__ == '__main__':
    for h in range(24):
        for m in range(60):
            print(get_time_string(h, m))
