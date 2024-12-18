from unittest import TestCase, main

from project.social_media import SocialMedia


class TestSocialMedia(TestCase):

    def setUp(self):
        # Create an instance of SocialMedia for testing
        self.social_media = SocialMedia("FashionGuru", "Instagram", 100000, "Fashion")

    def test_social_media_structure(self):
        self.assertTrue(hasattr(SocialMedia, "_validate_and_set_platform"))
        self.assertTrue(hasattr(SocialMedia, "create_post"))
        self.assertTrue(hasattr(SocialMedia, "like_post"))
        self.assertTrue(hasattr(SocialMedia, "comment_on_post"))

        self.assertTrue(isinstance(getattr(SocialMedia, "platform"), property))
        self.assertTrue(isinstance(getattr(SocialMedia, "followers"), property))

    def test_init(self):
        self.assertEqual(self.social_media._username, 'FashionGuru')
        self.assertEqual(self.social_media._platform, 'Instagram')
        self.assertEqual(self.social_media._followers, 100000)
        self.assertEqual(self.social_media._content_type, 'Fashion')

    def test_platform_with_allowed_platforms__expect_to_success(self):
        allowed_platforms = ['Instagram', 'YouTube', 'Twitter']
        for platform in allowed_platforms:
            with self.subTest(platform=platform):
                self.social_media.platform = platform
                self.assertEqual(self.social_media.platform, platform)

    def test_platform_with_invalid_platforms__expect_to_raise(self):
        allowed_platforms = ['Instagram', 'YouTube', 'Twitter']
        invalid_platform = 'InvalidPlatform'
        with self.assertRaises(ValueError) as context:
            self.social_media.platform = invalid_platform
        self.assertEqual(str(context.exception), f"Platform should be one of {allowed_platforms}")

    def test_followers_with_0_followers__expect_to_success(self):
        self.social_media.followers = 0
        expect = 0
        actual = self.social_media.followers
        self.assertEqual(expect, actual)

    def test_followers_with_positive_number_followers__expect_to_success(self):
        self.social_media.followers = 100
        expect = 100
        actual = self.social_media.followers
        self.assertEqual(expect, actual)

    def test_followers_with_negative_number_followers__expect_to_raise(self):
        invalid_followers = -1
        with self.assertRaises(ValueError) as context:
            self.social_media.followers = invalid_followers
        self.assertEqual(str(context.exception), "Followers cannot be negative.")

    def test_create_post(self):
        self.assertEqual(len(self.social_media._posts), 0)

        post_content = "Check out my latest fashion haul!"
        self.social_media.create_post(post_content)

        self.assertEqual(len(self.social_media._posts), 1)

        expected_post = {
            'content': post_content,
            'likes': 0,
            'comments': []
        }
        self.assertEqual(self.social_media._posts[0], expected_post)

        expected_message = f"New Fashion post created by FashionGuru on Instagram."
        actual_message = self.social_media.create_post(post_content)
        self.assertEqual(actual_message, expected_message)

    def test_like_post_with_valid_increment_likes__success(self):
        post_content = "Check out my latest fashion haul!"
        self.social_media.create_post(post_content)

        initial_likes = self.social_media._posts[0]['likes']
        self.assertEqual(initial_likes, 0)

        self.social_media.like_post(0)

        self.assertEqual(self.social_media._posts[0]['likes'], initial_likes + 1)

        expected_message = f"Post liked by FashionGuru."
        actual_message = self.social_media.like_post(0)
        self.assertEqual(actual_message, expected_message)

    def test_like_post_reach_max_likes__expect_to_return_correct_message(self):
        post_content = "Check out my latest fashion haul!"
        self.social_media.create_post(post_content)
        self.social_media._posts[0]['likes'] = 9

        initial_likes = self.social_media._posts[0]['likes']
        self.assertEqual(initial_likes, 9)

        self.social_media.like_post(0)

        self.assertEqual(self.social_media._posts[0]['likes'], 10)

        expected_message = "Post has reached the maximum number of likes."
        actual_message = self.social_media.like_post(0)
        self.assertEqual(actual_message, expected_message)

    def test_like_post_with_invalid_negative_index__expect_to_return_message_invalid_index(self):
        self.assertEqual(len(self.social_media._posts), 0)

        returned_message = self.social_media.like_post(-1)

        self.assertEqual(len(self.social_media._posts), 0)

        expected_message = "Invalid post index."
        self.assertEqual(returned_message, expected_message)

    def test_like_post_with_index_out_of_range__expect_to_return_message_invalid_index(self):
        self.assertEqual(len(self.social_media._posts), 0)

        returned_message = self.social_media.like_post(0)

        self.assertEqual(len(self.social_media._posts), 0)

        expected_message = "Invalid post index."
        self.assertEqual(returned_message, expected_message)

    def test_comment_on_post_with_valid_comment_length__success(self):
        post_content = "Check out my latest fashion haul!"
        self.social_media.create_post(post_content)

        post_index = 0
        comment = "Great outfits! Can't wait to try them on."
        result = self.social_media.comment_on_post(post_index, comment)

        self.assertEqual(result, f"Comment added by {self.social_media._username} on the post.")
        self.assertEqual(len(self.social_media._posts[post_index]['comments']), 1)

    def test_comment_on_post_with_invalid_comment_length__expect_to_return_correct_message(self):
        post_content = "Check out my latest fashion haul!"
        self.social_media.create_post(post_content)

        post_index = 0
        comment = "Short"
        result = self.social_media.comment_on_post(post_index, comment)

        self.assertEqual(result, "Comment should be more than 10 characters.")
        self.assertEqual(len(self.social_media._posts[post_index]['comments']), 0)


if __name__ == '__main__':
    main()