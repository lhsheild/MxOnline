from django.test import TestCase

import os


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxOnline.settings")
    import django
    django.setup()

    from apps.organization import models

    org = models.CourseOrg.objects.all()
    print(org)