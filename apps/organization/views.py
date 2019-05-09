from django.db.models import Count
from django.shortcuts import render, HttpResponse
from django.views.generic.base import View
from pure_pagination import PageNotAnInteger, Paginator

from .forms import UserAskForm
from .models import CourseOrg, CityDict
from apps.operation.models import UserFavorite


class OrgView(View):
    def get(self, request):
        # 取出所有课程机构
        all_orgs = CourseOrg.objects.all()
        # 取出所有城市
        all_citys = CityDict.objects.all()

        # 城市
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        # 机构类型
        category = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(category=category)

        org_onums = all_orgs.count()

        # 热门课程机构排名
        hot_orgs = all_orgs.order_by('-click_nums')[:3]

        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_orgs = all_orgs.annotate(au=Count("userprofile")).order_by("-au")
            elif sort == "courses":
                all_orgs = all_orgs.annotate(au=Count("course")).order_by("-au")

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, 5, request=request)
        orgs = p.page(page)

        return render(request, "org-list.html", locals())


class AddUserAskView(View):
    """
    用户添加咨询
    """

    def post(self, request):
        if request.is_ajax:
            userask_form = UserAskForm(request.POST)
            if userask_form.is_valid():
                user_ask = userask_form.save(commit=True)
                # 如果保存成功,返回json字符串,后面content type是告诉浏览器返回的数据类型
                return HttpResponse('{"status":"success"}', content_type='application/json')
            else:
                # 如果保存失败，返回json字符串,并将form的报错信息通过msg传递到前端
                return HttpResponse('{"status":"fail", "msg":"添加出错"}', content_type='application/json')


class OrgHomeView(View):
    def get(self, request, org_id):
        # 根据id找到课程机构
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 反向查询到课程机构的所有课程和老师
        all_courses = course_org.course_set.all()[:4]
        all_teacher = course_org.teacher_set.all()[:2]
        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        return render(request, 'org-detail-homepage.html', {
            'course_org': course_org,
            'all_courses': all_courses,
            'all_teacher': all_teacher,
            'current_page': 'home',
            'has_fav':has_fav,
        })


class OrgCourseView(View):
    def get(self, request, org_id):
        # 根据id取到课程机构
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 通过课程机构找到课程。内建的变量，找到指向这个字段的外键引用
        all_courses = course_org.course_set.all()
        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        return render(request, 'org-detail-course.html', {
            'all_courses': all_courses,
            'course_org': course_org,
            'current_page': 'course',
            'has_fav': has_fav,
        })


class OrgDescView(View):
    def get(self, request, org_id):
        current_page = 'desc'
        # 根据id取到课程机构
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        return render(request, 'org-detail-desc.html', {
            'course_org': course_org,
            'current_page': current_page,
            'has_fav': has_fav,
        })


class OrgTeacherView(View):
    """
   机构教师页
    """

    def get(self, request, org_id):
        current_page = 'teacher'
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_teacher = course_org.teacher_set.all()
        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        return render(request, 'org-detail-teachers.html', {
            'all_teacher': all_teacher,
            'course_org': course_org,
            'current_page': current_page,
            'has_fav': has_fav,
        })


class AddFavView(View):
    def get(self, request):
        pass

    def post(self, request):
        id = request.POST.get('fav_id', 0)  # 防止后边int(fav_id)时出错
        type = request.POST.get('fav_type', 0)  # 防止int(fav_type)出错

        print(id, type)

        if not request.user.is_authenticated:
            # 未登录时返回json提示未登录，跳转到登录页面是在ajax中做的
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')

        exist_record = UserFavorite.objects.filter(user=request.user, fav_id=int(id), fav_type=int(type))
        if exist_record:
            # 如果记录已经存在，表示用户取消收藏
            exist_record.delete()
            return HttpResponse('{"status":"success", "msg":"收藏"}', content_type='application/json')
        else:
            user_fav = UserFavorite()
            if int(id) > 0 and int(type) > 0:
                user_fav.user = request.user
                user_fav.fav_id = int(id)
                user_fav.fav_type = int(type)
                user_fav.save()
                return HttpResponse('{"status":"success", "msg":"已收藏"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail", "msg":"收藏出错"}', content_type='application/json')
