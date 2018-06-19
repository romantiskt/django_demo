from django.db import models


# Create your models here.
# class BookInfoManager(models.Manager):
#     def get_queryset(selfs):#过滤操作
#         return super(BookInfoManager,selfs).get_queryset().filter(isDelete=True)
#     def create_book(selfs,title,pub_date):#构造一个创建实体的方法
#         # book=selfs.model()
#         # book.btitle=title
#         # book.bpub_date=pub_date
#         # book.bread=0
#         # book.bcommet=0
#         # book.isDelete=False
#         #下面这种就不需要手动调用 save()了
#         book = selfs.create(btitle=title, bpub_date=pub_date, bread=0, bcommet=0, isDelete=False)
#         return book

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(default=0)
    isDelete=models.BooleanField(default=False)

    # books = models.Manager() 为模型指定管理器，如果指定了，则编译器不再为模型生成 objects 则BookInfo.objects 将发生错误
    # books=BookInfoManager()#指定管理器，需要为模型拓展方法时 调用：book=BookInfo.books.create_book("abc",datetime(1980,1,1)) 保存：book.save()
    # isDelete = models.BooleanField(default=False)
    class Meta():#元选项，
        ordering = ['-bpub_date']#根据某一字段排序，加'-'表示倒序

    def __str__(self):
        return '%s' % self.btitle


class HerInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    hcontent = models.CharField(max_length=200)
    hBook = models.ForeignKey('BookInfo')

    def __str__(self):
        return '%d' % self.pk

    def gender(self):  # 将hgender转化为文字
        if self.hgender:
            return '男'
        else:
            return '女'

    gender.short_description = '性别'  # 修改字段名称
