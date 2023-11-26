from django.db import models
# import os
# import django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ls_store_demo.settings")
# django.setup()
# Create your models here.
# 每一个表就是一个模型
class Category(models.Model):  # 商品类别名表
    cname = models.CharField(max_length=10)

    def __unicode__(self): # 为了后续查看表名比较方便
        return u'Category:%s' % self.cname

class Goods(models.Model):  # 商品表
    gname = models.CharField(max_length=100)
    gdesc = models.CharField(max_length=100)
    oldprice = models.DecimalField(max_digits=5,decimal_places=2)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    category = models.ForeignKey(Category,models.CASCADE)
    # 获取商品大图
    def getGimg(self):
        return self.inventory_set.first().color.colorurl
    # 获取商品全部小图
    def getImgs(self):
        color_urls = []
        color_names = []
        for inventory in self.inventory_set.all():
            color_url = inventory.color.colorurl
            color_name =inventory.color.colorname
            if color_url not in color_urls:
                color_urls.append(str(color_url))
            if color_name not in color_names:
                color_names.append(str(color_name))
        return color_urls,color_names

    #获取全部商品尺码信息
    def getSizes(self):
        sizes = []
        inventories = self.inventory_set.all()
        for inventory in inventories:
            size = inventory.size
            if size.sname not in sizes:
                sizes.append(str(size.sname))
        return sizes

    # 获取商品详情列表
    def getDetailsList(self):
        import collections
        # 创建一个有序字典用于存放详情信息（key:详情名称value:图片列表）
        datas = collections.OrderedDict()
        for goodsDetail in self.goodsdetail_set.all():
            # 获取详情名称
            gdname = str(goodsDetail.name())
            if gdname not in datas:
                datas[gdname] = [str(goodsDetail.gdurl)]
            else:
                datas[gdname].append(str(goodsDetail.gdurl))
        return datas


    # 获取库存信息
    def getCount(self):
        return self.inventory_set.first().count

    def __unicode__(self):
        return u'Goods:%s'%self.gname

class GoodsDetailName(models.Model):  # 商品详细信息名表
    gdname = models.CharField(max_length=30)

    def __unicode__(self):
        return u'GoodsDetailName:%s'%self.gdname

class GoodsDetail(models.Model):  # 商品详情表，也就是图片的存储路径表
    gdurl = models.ImageField(upload_to='')  # 图片上传路径（相对路径）
    gdname = models.ForeignKey(GoodsDetailName,models.CASCADE)
    goods = models.ForeignKey(Goods,models.CASCADE)
    #获取详情名称
    def name(self):
        return self.gdname.gdname

class Size(models.Model):  # 商品尺寸存储表
    sname = models.CharField(max_length=10)

    def __unicode__(self):
        return u'Size:%s'%self.sname

class Color(models.Model):  # 商品颜色存储表
    colorname = models.CharField(max_length=10)
    colorurl = models.ImageField(upload_to='color/')  # 颜色小图路径存储表

    def __unicode__(self):
        return u'Color:%s'%self.colorname

class Inventory(models.Model):  # 库存数量表
    count = models.PositiveIntegerField()  # 库存不会出现负数
    color = models.ForeignKey(Color,models.CASCADE)
    goods = models.ForeignKey(Goods,models.CASCADE)
    size = models.ForeignKey(Size,models.CASCADE)