from django.conf.urls import url

from .views import UserinfoView, UploadImageView, UpdatePwdView, SendEmailCodeView, UpdateEmailView, MyCourseView, \
    MyFavOrgView, MyFavTeacherView, MyFavCourseView, MyMessageView

app_name = "users"

urlpatterns = [
    url(r"^info/", UserinfoView.as_view(), name='user_info'),
    url(r"^image/upload", UploadImageView.as_view(), name='image_upload'),
    url(r"^update/pwd/", UpdatePwdView.as_view(), name='update_pwd'),
    url(r"^sendemail_code/", SendEmailCodeView.as_view(), name='sendemail_code'),
    url(r"^update_email/", UpdateEmailView.as_view(), name='update_email'),
    url(r"^mycourse/", MyCourseView.as_view(), name='mycourse'),
    url(r'^myfav/org/', MyFavOrgView.as_view(), name="myfav_org"),
    url(r'^myfav/teacher/', MyFavTeacherView.as_view(), name="myfav_teacher"),
    url(r'^myfav/course/', MyFavCourseView.as_view(), name="myfav_course"),
    url(r'^my_message/', MyMessageView.as_view(), name="my_message"),
]
