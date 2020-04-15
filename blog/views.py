from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render
import logging
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from django.contrib.auth import authenticate, login
from django.urls import reverse
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt

from blog.models import *
from common.form import UserForm, UserReisterForm
from my_blog import settings

logger = logging.getLogger('mydjango')


def global_setting(request):
    """
    全局配置函数，需要在上下文中配置
    :return:返回配置数据
    """
    res = {
        'SITE_NAME': settings.SITE_NAME
    }
    return res


@csrf_exempt
def uploadImg(request):
    """
    富文本插件中图片上传需要的接口
    :param request:
    :return:
    """
    img = request.FILES.get('img')
    adminImg = BlogPic()
    adminImg.filename = img.name
    adminImg.img = img
    adminImg.save()
    return HttpResponse("<script>top.$('.mce-btn.mce-open').parent().find('.mce-textbox').val('/media/%s')"
                        ".closest('.mce-window').find('.mce-primary').click();</script>" % adminImg.img)


def register(request):
    """
    注册
    :param request:
    :return:
    """
    try:
        if request.method == "POST":
            userform = UserReisterForm(request.POST)  # 将POST请求中的数据封装到UserForm对象中

            try:
                if userform.is_valid():  # 验证表单数据是否有效
                    regname = userform.cleaned_data["username"]
                    regemail = userform.cleaned_data["email"]
                    regpwd = userform.cleaned_data["password"]
                    conf_regpwd = userform.cleaned_data["conf_password"]
                    print('regpwd=', regpwd, 'conpwd=', conf_regpwd)
                    if regpwd == conf_regpwd:
                        reg_user = User.objects.create(username=regname, password=make_password(regpwd), email=regemail)
                        reg_user.save()
                        return redirect(reverse("blog:login"))
                    else:
                        error = '口令不一致'
                else:
                    error = userform.errors
            except Exception as e:
                logger.error(e)

        else:
            userform = UserReisterForm()  # 创建一个空的表单对象
        print(error)

    except Exception as e:
        logger.error(e)

    return render(request, 'blog_register.html', locals())


def login_view(request):
    try:
        if request.method == 'GET':
            userform = UserForm()
            return render(request, 'blog_login.html', locals())
        if request.method == 'POST':
            userform = UserForm(request.POST)  # 将POST请求中的数据封装到UserForm对象中
            # print(userform)
            if userform.is_valid():  # 验证表单数据是否有效
                print("+++++++++++++++++++++++++++++++++")
                log_username = userform.cleaned_data["username"]
                log_password = userform.cleaned_data["password"]
                user = authenticate(username=log_username, password=log_password)  # 认证用户
                print(user)
                if user is not None:  # 如果用户认证成功
                    login(request, user)  # 将用户的ID添加到session属性中
                    return redirect(reverse("blog:index"))
            else:
                error = userform.errors
                print(error)
                logger.error(error)
            return redirect(reverse("blog:login"))

    except Exception as e:
        logger.error(e)
        return redirect(reverse("blog:login"))


def index(request):
    """
    显示所有博客
    :param request:
    :return:
    """
    try:
        # 导航数据获取
        catagory_list = Catagory.objects.all()
        # 广告数据
        ad_list = Ad.objects.all()
        # 最新文章数据
        article_list = Article.objects.all()
        paginator = Paginator(article_list, 2)
        try:
            page = int(request.GET.get('page', 1))
            page_article = paginator.page(page)
        except (EmptyPage, InvalidPage, PageNotAnInteger) as e:
            page_article = paginator.page(1)
            logger.error(e)
    except Exception as e:
        logger.error(e)
    return render(request, 'index.html', locals())
