# both functions return string type values

def binary_to_decimal(binary_num):
  b_str = str(binary_num)
  binary_num_list = list(b_str)
  binary_num_list.reverse()
  result = 0

  for i, v in enumerate(binary_num_list):
    result += 2**i * int(v)

  return str(result)


def decimal_to_binary(decimal_num):
  d_num = decimal_num
  binary_digits = []
  result = ""
  
  while True:
    if d_num == 1 or d_num == 0:
      return d_num

    elif d_num // 2 == 1:
      remainder = d_num % 2
      binary_digits.append(remainder)
      binary_digits.append(1)
      break
      
    else:
      remainder = d_num % 2
      binary_digits.append(remainder)
      d_num //= 2

  binary_digits.reverse()
  
  for i in binary_digits:
    result += str(i)

  return result
