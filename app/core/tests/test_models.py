from django.test import TestCase
from django.contrib.auth import get_user_model

from core.models import Tag, Ingredient


def sample_user(email='test@gmail.com', password='testpass'):
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = "milon@gmail.com"
        password = "Testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'test@GMAIL.com'
        user = get_user_model().objects.create_user(
            email=email,
            password="test123"
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                None,
                password="test123"
            )

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            email='test@gmail.com',
            password="test123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )
        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test the ingredient String representation"""
        ingredient = Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )
        self.assertEqual(str(ingredient), ingredient.name)

    # def test_recipe_str(self):
    #     """Test the recipe string representation"""
    #     recipe = Recipe.objects.create(
    #         user=sample_user(),
    #         title='Steak and mushroom sauce',
    #         time_minutes=5,
    #         price=5.00
    #     )
    #
    #     self.assertEqual(str(recipe), recipe.title)
    #
    # @patch('uuid.uuid4')
    # def test_recipe_file_name_uuid(self, mock_uuid):
    #     """Test that image is saved in the correct location"""
    #     uuid = 'test-uuid'
    #     mock_uuid.return_value = uuid
    #     file_path = models.recipe_image_file_path(None, 'myimage.jpg')
    #
    #     exp_path = f'uploads/recipe/{uuid}.jpg'
    #     self.assertEqual(file_path, exp_path)
