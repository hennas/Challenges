def main():
   given_blocks = int(input())
   height, used_blocks, edge_len = -1, 0, 1

   while used_blocks <= given_blocks:
      used_blocks += edge_len * edge_len
      height += 1
      edge_len += 2
   print(height)


if __name__ == '__main__':
    main()
