from src.api.category_resource import CategoryResource
from src.api.payment_resource import PaymentResource
from src.api.ping_resource import PingResource
from src.api.product_resource import ProductResource
from src.api.promotion_resource import PromotionResource
from src.api.suggestion_resource import SuggestionResource


def api_endpoints():
    return [
        (PingResource, '/'),
        (ProductResource, ['/products', '/products/<product_id>']),
        (CategoryResource, ['/categories', '/categories/<category_name>']),
        (PaymentResource, ['/payments', '/payments/<payment_id>']),
        (PromotionResource, ['/promotions', '/promotions/<promotion_id>']),
        (SuggestionResource, ['/suggestions', '/suggestions/<suggestion_id>'])
    ]
