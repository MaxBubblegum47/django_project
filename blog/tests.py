from django.test import TestCase
from blog.models import Post
from model_bakery import baker

# Create your tests here.
class PostTest(TestCase):
    def testPosting(self):
        '''def test_event_model(self):
            event = Post.objects.create(
                title="Some title",
                audio="/media/cash.mp3",
                header_image="/media/images/cash.jpg",
                date_posted=datetime.time,
                author="The body",
                singer="The body",
                album="the-slug",
                likes=800,
                category='rock'
            )'''
        user_post = baker.make(Post, title="Post Test")
        self.assertEqual(str(user_post), "Post Test")
