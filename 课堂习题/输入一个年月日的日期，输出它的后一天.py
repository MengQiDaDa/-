from datetime import datetime,timedelta #导入操作日期和时间的库

def main():
    year = input('年:')
    month = input('月:')
    day = input('日:')
    text = year + '-'+ month + '-'+ day
    today = datetime.strptime(text,"%Y-%m-%d").date()
    print(today)
    tomorrow = today + timedelta(days = 1)
    print(tomorrow)

if __name__ == '__main__':
    print("ss")
    main()