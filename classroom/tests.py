from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from models import (
    TakenQuiz,
    Question,
    Quiz,Answer
)


class ModelsTestCase(TestCase):
    """
    Parent testcase that runs test for all model tests created here
    """

    def setUp(self):
        """
        Initalize each model to be used in later scripts
        """
        self.takenquiz = TakenQuiz.objects.create(
            name="Test TakenQuiz",
            visibility=True,
            order_rank=1
        )
        self.quiz = Quiz.objects.create(
            name="Test Quiz"
        )
        self.answer = Answer.objects.create(
            takenquiz=self.c,
            company=self.company,
            name="Test Product"
        )

    """
    Every testcase must have the prefix 'test'. Please use names that are as detailed as possible for each test case
    """

    # def test_category_created(self):
    #     # Was the model created successfully? We see if the category is an instance of the parent class.
    #     self.assertTrue(isinstance(self.category, Category))

    # def test_category_name_matches(self):
    #     # Were the fields created with the right values?
    #     self.assertEqual(self.category.name, str(self.category))

    # def test_company_created(self):
    #     self.assertTrue(isinstance(self.company, Company))

    # def test_company_name_matches(self):
    #     self.assertEqual(self.company.name, str(self.company))

    # def test_product_created(self):
    #     self.assertTrue(isinstance(self.product, Product))

    # def test_product_category_foreign_key(self):
    #     self.assertEqual(self.product.category, self.category)