from django.db import models
from django.contrib.auth.models import AbstractUser
from tinymce.models import HTMLField


# 用户模型
class User(AbstractUser):
    head = models.ImageField(upload_to='head/%Y/%m', default='head/user.png', max_length=200, verbose_name='用户头像')
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='qq号码')

    class Meta:
        ordering = ['-id']
        verbose_name_plural = verbose_name = "用户"

    def __unicode__(self):
        return self.username

    def __str__(self):
        return self.username


# 标签模型
class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="标签名称")

    class Meta:
        verbose_name_plural = verbose_name = "标签"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


# 分类模型
class Catagory(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="分类名称")
    index = models.IntegerField(default=999, unique=True, verbose_name="分类的排序")

    class Meta:
        verbose_name_plural = verbose_name = '分类'
        ordering = ('index', 'name')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


# 文章模型
class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name="文章标题")
    desc = models.CharField(max_length=50, verbose_name='文章描述')
    content = HTMLField(verbose_name="文章内容")
    click_count = models.IntegerField(default=0, verbose_name="点击次数")
    is_recommend = models.BooleanField(default=False, verbose_name="是否推荐")
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    user = models.ForeignKey(User, verbose_name="用户", on_delete=models.CASCADE)
    category = models.ForeignKey(Catagory, blank=True, null=True, verbose_name="分类", on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name="标签")

    class Meta:
        verbose_name_plural = verbose_name = '文章'
        ordering = ['-date_publish']

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


# 评论模型
class Comment(models.Model):
    content = models.TextField(verbose_name="评论内容")
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    user = models.ForeignKey(User, blank=True, null=True, verbose_name="用户", on_delete=models.CASCADE)
    article = models.ForeignKey(Article, blank=True, null=True, verbose_name="文章", on_delete=models.CASCADE)
    pid = models.ForeignKey("self", blank=True, null=True, verbose_name="父级评论", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = verbose_name = "评论"
        ordering = ['-date_publish']

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)


# 友情链接
class Links(models.Model):
    title = models.CharField(max_length=50, verbose_name="标题")
    description = models.CharField(max_length=50, verbose_name="友情链接描述")
    callback_url = models.URLField(null=True, blank=True, verbose_name="回调url")
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    index = models.IntegerField(default=900, verbose_name="排列顺序（从小到大）")

    class Meta:
        verbose_name_plural = verbose_name = "友情链接"
        ordering = ['index', 'id']

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


# 广告
class Ad(models.Model):
    title = models.CharField(max_length=50, verbose_name="广告标题")
    description = models.CharField(max_length=50, verbose_name="广告描述")
    image_url = models.ImageField(upload_to='ad/%Y/%m', verbose_name="图片路径")
    callback_url = models.URLField(null=True, blank=True, verbose_name="回调url")
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    index = models.IntegerField(default=900, unique=True, verbose_name="排列顺序（从小到大）")

    class Meta:
        verbose_name_plural = verbose_name = "广告"
        ordering = ['index', 'id']

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class BlogPic(models.Model):
    filename = models.CharField(max_length=200, blank=True, null=True)
    img = models.ImageField(upload_to='upload/%Y/%m')
