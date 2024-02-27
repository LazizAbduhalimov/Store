from django.test import SimpleTestCase, Client
from django.urls import reverse, resolve

from cart.views import CartPage, add_product, remove_product_from_user_cart_view, substract_product_from_user_cart_мшуц


class TestUrls(SimpleTestCase):

    def setUp(self):
        self.client = Client()

    def test_cart_url_resolves(self):
        url = reverse("cart")
        self.assertEquals(resolve(url).func.view_class, CartPage)

    def test_add_product_url_resolves(self):
        url = reverse("add-product", args=["some_args"])
        self.assertEquals(resolve(url).func, add_product)

    def test_remove_product_url_resolves(self):
        url = reverse("remove-product", args=["some_args"])
        self.assertEquals(resolve(url).func, remove_product_from_user_cart_view)

    def test_substract_product_url_resolves(self):
        url = reverse("substract-product", args=["some_args"])
        self.assertEquals(resolve(url).func, substract_product_from_user_cart_мшуц)

    def test_urls_use_correct_template(self):
        template_urls = {
            "cart": "cart.html"
        }

        for name, template in template_urls.items():
            url = reverse(name)
            response = self.client.get(url)
            self.assertTemplateUsed(response, template)
