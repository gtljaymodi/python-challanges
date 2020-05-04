'''
Example test statement:

foxy fox running into the jungle with the other fox
'''


def word_count(data):
    data = data.split()
    d_data = dict()
    for d in data:
        if d not in d_data:
            d_data[d] = 1
        else:
            d_data[d] += 1
    return d_data


if __name__ == '__main__':
    data = input()
    o_data = word_count(data)
    print(f"Output: {o_data}")

