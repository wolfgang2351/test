import time  # 第一序位,导入时间模块
goods_info=[]  # 第二序位（全局变量）
def wrap_time(func):
    def inner(*args,**kwargs):
        print(time.strftime("%y-%m-%d %H:%M:%S",time.localtime()))
        func(*args,**kwargs)
    return inner

def wrap_log(func):
    def inner(*args,**kwargs):
        print("正在运行")
        func(*args,**kwargs)
    return inner

def goods_menu():
    print("~" * 30)
    print("商品管理系统 V1.0beta`")
    print("1.添加商品信息")
    print("2.删除商品信息")
    print("3.修改商品信息")
    print("4.查询商品信息")
    print("5.保存商品数据信息")
    print("6.查看商品数据信息")
    print("0.退出程序")
    print("~" * 30)

@wrap_time
@wrap_log
def add_info():
    new_name = input("请输入商品名:")
    new_name.isdigit()
    if new_name!=True:
        print('请勿输入数字')
        add_info()
    else:
        print('输入了字符串')
    new_price = input("请输入商品价格:")
    new_info = {}
    new_info['name'] = new_name
    new_info['price'] = new_price
    goods_info.append(new_info)

@wrap_time
@wrap_log
def del_info(goods):
    try:
        del_number = int(input('请输入要删除商品的序号:'))-1
        del goods[del_number]
    except IndexError as e:
        print(e)
        print("商品信息为空！请先录入信息！")

@wrap_time
@wrap_log
def modify_info():
    try:
        goods_id = int(input('请输入要修改的商品的序号:'))
        new_goods = input('请输入新商品的名称:')
        new_price = input('请输入新商品的价格:')
        goods_info[goods_id - 1]['name'] = new_goods
        goods_info[goods_id - 1]['price'] = new_price
    except Exception as result1:
        print(result1)
        print("请先录入信息再执行修改操作")


@wrap_time
@wrap_log
def show_info():
    print('*' * 30)
    print('商品信息如下: ')
    i = 1
    for temp in goods_info:
        print("序号：%d   品名：%s   价格：%s$" % (i, temp['name'], temp['price']))
        i += 1
    print('*' * 30)

@wrap_time
@wrap_log
def save_data_file():
    file=open("goods_info.data","w")
    file.write(str(goods_info))
    print("Data信息已保存")           #备份一个Data信息
    file.close()
def save_txt_file():
    file=open("goods_info.txt","w")
    file.write(str(goods_info))
    print("Txt信息已保存")
    file.close()

@wrap_time
@wrap_log
def read_txt_file():
    try:
        file=open("goods_info.txt","r")
        a=(file.read())
        print(a)
        print("已打开TXT文件")
        file.close()
    except Exception as result2:
        print(result2)
        print("读取TXT数据报错")



def recover_data():
    try:
        global goods_info
        file=open("goods_info.data")
        content=file.read()
        goods_info=eval(content)
        print("data数据已恢复")
        file.close()
    except Exception as result3:
        print("恢复data信息出错")
        print(result3)

def recover_txt():
    try:
        global goods_info
        file=open("goods_info.txt")
        content=file.read()
        goods_info=eval(content)
        print("txt数据已恢复")
        file.close()
    except Exception as result4:
        print("恢复txt信息出错")
        print(result4)


def main():
    while True:
        goods_menu()  # 打印菜单
        key = input('请输入与功能相对应的序号: ')
        if key == '1':  # 调用功能1
            add_info()
            print("信息已保存")
        elif key == '2':  # 调用功能2
            del_info(goods_info)
            print("信息已删除")
        elif key == '3':  # 调用功能3
            modify_info()
        elif key == '4':  # 调用功能4
            exe=input('是否对以前的数据进行恢复并进行读取?(Yes or No)ps:请注意区分大小写：')
            if exe == 'Yes':
                print ('正在进行数据恢复')
                print('正在恢复数据')
                recover_data()
                recover_txt()
                read_txt_file()
                show_info()
                print("信息已恢复")
            else:
                show_info()
        elif key == '5':  #调用功能5
            save_data_file()
            save_txt_file()
            print("新信息已保存")
        elif key == '6':
            print("正在查看TXT数据")
            read_txt_file()
        elif key == '0':  # 退出程序
            quit = input('你真的要离开了吗?(Yes or No)')
            if quit == 'Yes':
                print('正在退出程序')
                break
            elif quit == 'No':
                print('正在返回程序')
            else:
                print('您的输入有误,请重新输入(可能未区分大小写)')
main()