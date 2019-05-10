from django.conf.urls import url

from .views import UserinfoView, UploadImageView, UpdatePwdView, SendEmailCodeView, UpdateEmailView

app_name = "users"

urlpatterns = [
    url(r"^info/", UserinfoView.as_view(), name='user_info'),
    url(r"^image/upload", UploadImageView.as_view(), name='image_upload'),
    url(r"^update/pwd/", UpdatePwdView.as_view(), name='update_pwd'),
    url(r"^sendemail_code/", SendEmailCodeView.as_view(), name='sendemail_code'),
    url(r"^update_email/", UpdateEmailView.as_view(), name='update_email'),
]
