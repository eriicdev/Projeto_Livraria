import factory
from product.models import Product, Category
from django.contrib.auth.models import User
from order.models import Order

class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('word')
    slug = factory.Faker('slug')
    description = factory.Faker('sentence')
    active = factory.Iterator([True, False])

    class Meta:
        model = Category

class ProductFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('word')
    price = factory.Faker('pyint', min_value=1, max_value=1000)
    description = factory.Faker('sentence')
    active = factory.Iterator([True, False])

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for category in extracted:
                self.categories.add(category)
        else:
            self.categories.add(CategoryFactory())

    class Meta:
        model = Product

class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.PostGenerationMethodCall('set_password', 'password123')

    class Meta:
        model = User

class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def product(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for prod in extracted:
                self.product.add(prod)
        else:
            self.product.add(ProductFactory())

    class Meta:
        model = Order
