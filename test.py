import os

from django.db.models import Count

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxOnline.settings")
    import django

    django.setup()

    from apps.organization import models

    org = models.CourseOrg.objects.all()
    org = org.annotate(au=Count("course")).order_by("-au")
    for i in org:
        print(i.name , i.au)
        print(i.course_set.count())

    print("*"*120)

    org1 = models.CourseOrg.objects.all()
    org1 = org1.annotate(au=Count("userprofile")).order_by("-au")
    for i in org1:
        print(i.name , i.au)