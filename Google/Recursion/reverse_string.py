def reverse_list(str):
    if not str:
        return []
    else:
        return [str[-1]] + reverse_list(str[:-1])
        print(str)
    return str

if __name__=="__main__":
    str = reverse_list([1,2,3,4,5])
    print(str)
