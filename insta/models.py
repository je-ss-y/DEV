from django.contrib.auth.models import User
from django.db import models
import datetime as dt
from tinymce.models import HTMLField

LEVEL_CHOICES = (
    ('Junior','Junior'),
    ('Beginner', 'Beginner'),
    ('Intermediate','Intermediate'),
    ('Senior','Senior'),
)

class Profile(models.Model):
    class Meta:
        db_table = 'profile'
    bio = models.CharField(max_length=200, null=True, blank=True)
    profile_photo = models.ImageField(upload_to='pictures/', null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True, )
    contacts = models.CharField(max_length=50, null=True, blank=True)
    github = models.URLField(max_length=200, null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='Junior')

    def save_profile(self):
        self.save()
       
    def delete_profile(cls, id):
        self.delete()

    def update_profile(self,update):
        self.bio = update
        self.save()

    # @classmethod
    # def get_profile_by_id():
    #     cls.objects.filter(=id)

    @classmethod
    def search_by_user(cls,search_term):
        user = cls.objects.filter(user__username__icontains=search_term)
        return user


    # def get_comments(self, id):
    #     comments = Comments.objects.filter(image_id = id)
    #     return comments
class Follow(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')

    def __str__(self):
        return '{} follows {}'.format(self.following,self.follower)

User.add_to_class('followings',models.ManyToManyField('self',through=Follow,related_name='followers',symmetrical=False))


class Image(models.Model):
    class Meta:
        db_table = 'image'
    image = models.ImageField(upload_to ='pictures/', blank =True)
    title = models.CharField(max_length =50)
    content = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank =True)
    pub_date = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=80,null=True)

    def __str__(self):
        return self.image_name
    
    def save_image(self):
        self.save()
    
    @classmethod
    def get_all_images(cls):
        images = cls.objects.all().prefetch_related('comment_set')
        return images

    @classmethod
    def delete_image(cls, id):
        pic = cls.objects.filter(pk=id)
        pic.delete()
    
    @classmethod
    def update_image(self,update):
        self.image_caption = update
        self.save()

    @classmethod
    def display_images(cls, id):
        images = cls.objects.get(id=id)
        return images
    
    @classmethod
    def display_user_images(cls):
        images = cls.objects.filter()
        return images
    
    @classmethod
    def get_images(cls):
        images = cls.objects.all().prefetch_related('comment_set')
        return images

class Comments(models.Model):
    class Meta:
        db_table = 'comments'
    comment = models.CharField(max_length=20,null=True)
    comment_image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="comment_img")
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.comment

