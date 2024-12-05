data = [(1,2),(2,3),(3,1),(5,4),(6,5),(7,8),(8,7),(9,5)]

def euclidian_distance(x,y):
    return ((x[0]-y[0])**2 + (x[1]-y[1])**2)**0.5

def minimum_distance(distance_matrix):
    minimum = float("inf")
    for i in range(0,len(distance_matrix)):
        for j in range(0,len(distance_matrix)):
            if distance_matrix[i][j] < minimum and distance_matrix[i][j] != 0:
                minimum = distance_matrix[i][j]
                x = i
                y = j
    return x,y
def generate_distances(data):
    distance_matrix = [[0 for i in range(0,len(data))] for j in range(0,len(data))]
    for i in range(0,len(data)):
        for j in range(0,len(data)):
            distance_matrix[i][j] = euclidian_distance(data[i],data[j])
    return distance_matrix

def update_data(data, x):
    new_data = []
    for i in range(0,len(data)):
        if i != x[0] and i != x[1]:
            new_data.append(data[i])
    new_data.append(((data[x[0]][0]+data[x[1]][0])/2,(data[x[0]][1]+data[x[1]][1])/2))
    return new_data

def print_matrix(matrix):
    for row in distance_matrix:
        text = " "
        for i in range(len(row)):
            text += str("%.4f" %row[i]) + ",  "
        print("[", text, "]")

for i in range(0,len(data)-1):
    distance_matrix = generate_distances(data)
    print_matrix(distance_matrix)
    x = minimum_distance(distance_matrix)
    print(x)
    data = update_data(data, x)
    print("\n\n")

