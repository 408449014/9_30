if __name__ == "__main__":
    f = open("day1.txt", "r")
    data = f.read().splitlines()
    data_length = len(data) 

    for i in range(data_length):
        data[i] = int(data[i])

    counter = 0
    for i in range(data_length):
        if data[i]-data[i-1] > 0:
            counter += 1
    
    print(counter)