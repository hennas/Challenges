def print_weak_vertex(i, vertex_connections):
    for j in vertex_connections[i]:
        for k in vertex_connections[j]:
            if k != i and k != j and i in vertex_connections[k]:
                return
    print(i, end=' ')


def main():
    num_vertices = int(input())
    while num_vertices != -1:
        vertex_connections = {source: [target[0] for target in filter(lambda x: x[1] == "1", enumerate(input().split()))] for source in range(num_vertices)}
        for i in vertex_connections:
            print_weak_vertex(i, vertex_connections)
        print()
        num_vertices = int(input())


if __name__ == '__main__':
    main()
