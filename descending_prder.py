def descending_order(num):
    return int(''.join(sorted(list(str(num)), reverse=True)))

print(descending_order(3293819)) # 987654321