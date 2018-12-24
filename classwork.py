class G:
    def __init__(self):
        self.gs_info = []
        self.g_info = {}
    def g_add(self,self.gs_info,name,number,price):
        self.g_info['名称'] = name
        self.g_info['数量'] = number
        self.g_info['价格'] = price
        self.gs_add()
        print("添加成功")

    def gs_add(self):
        self.gs_info.append(self.g_info)
        sel.g_info={}

    def gs_del(self,xh):
        del self.gs_info[xh-1]
        print("删除成功")

    def gs_m(self,xh,name,number,price):
        self.gs_info[xh-1]['名称'] = name
        self.gs_info[xh-1]['数量'] = number
        self.gs_info[xh-1]['价格'] = price

    def gs_all(self):
        print("*"*30)
        print("商品的信息如下：")
        print("*"*30)
        print("序号    名称    价格    数量")
        i=1
        for t in self.gs_info:
            print("%d    %s    %s    %s") % (i,t["名称"],t["数量"],t["价格"]))
            i += 1

    def gs_save(self):
        with open("data.txt","w") as f:
            for i in self.gs_info:
                f.write(str(i))
                f.write("\n")

    def goods_menu():
        print("=" * 30)
        print("商品管理系统 V1.0beta`")
        print("1.添加商品信息")
        print("2.删除商品信息")
        print("3.修改商品信息")
        print("4.查询商品信息")
        print("5.保存商品信息")
        print("0.退出程序")
        print("=" * 30)
    
