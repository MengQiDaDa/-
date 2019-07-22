def main():
    str = input('请输入')
    if str == str[::-1]:
        print('是回文')
    else:
        print('不是会问')

if __name__ == '__main__':
    main()