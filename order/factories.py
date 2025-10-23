import factory
from django.contrib.auth.models import User
from product.factories import ProductFactory
from order.models import Order


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker('email')
    username = factory.Faker('user_name')

    class Meta:
        model = User


class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def product(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for p in extracted:
                self.product.add(p)
        else:
            # cria 1 produto padrão se nenhum for passado
            self.product.add(ProductFactory())

    class Meta:
        model = Order
