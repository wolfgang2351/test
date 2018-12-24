from goods2 import g
good = G()
while True:
    global good
    g.menu()
    key = input("请输入操作序号:")
    if key == "1":
        name = input("请输入商品名称")
        number = input("请输入商品数量")
        price = input("请输入商品价格")
        good.g_add(name,number,price)

    if key == "2":
        xh=int(input("请输入要修改的商品序号"))
        yz(xh)
        good.gs_del(xh)

    if key == "3":
        xh = int(input("请输入要修改的序号"))
        yz(xh)
        name = input("请输入商品名称")
        number = input("请输入商品数量")
        price = input("请输入商品价格")
        good.gs_m(xh,name,number,price)

    if key == "4":
        good.gs_all()

    if key == "5":
        good.gs_save()

    if key == "0":
        break

main()
    
        
