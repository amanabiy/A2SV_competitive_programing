def dominoPiling(n: int, m: int) -> int:
  """ number of domino """
  area: int = n * m
  return area // 2
     
 if __name__ == "__main__":
        numbers = input()
        num1 = int(numbers.split(" ")[0])
        num2 = int(numbers.split(" ")[1])
        print(dominoPiling(num1, num2))
