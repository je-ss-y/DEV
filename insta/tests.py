from django.test import TestCase
from .models import Comments,Image,Profile
from django.contrib.auth.models import User

# Create your tests here.
class CommentsTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.jiji = User.objects.create(username='jiji')
        self.image = Image.objects.create(image='pic')
        self.comment= Comments.objects.create(comment='cool')
        self.com = Comments.objects.create(user=self.jiji,image=self.image,comment='cool')
        self.com.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.com, Comments))

    def test_save_method(self):
        self.assertTrue(len(Comments.objects.all()), 1)

    def tearDown(self):
        Comments.objects.all().delete()

    def test_delete_comment(self):
        self.com.delete()
        self.assertTrue(len(Comments.objects.all()), 0)

