import pytest

from api.products_api import ProductsAPI
from utilities.api_assertions import APIAssertions

pytestmark = pytest.mark.api


def test_get_all_products():
    """
    GET productsList returns the product catalogue with the expected fields.
    """

    response = ProductsAPI().get_products_list()

    APIAssertions.assert_response_code(response, 200)

    products = APIAssertions.get_json(response)["products"]

    assert len(products) > 0

    for field in ("id", "name", "price", "brand", "category"):
        assert field in products[0], f"'{field}' missing from product"


def test_get_all_brands():
    """
    GET brandsList returns a non-empty list of brands.
    """

    response = ProductsAPI().get_brands_list()

    APIAssertions.assert_response_code(response, 200)

    brands = APIAssertions.get_json(response)["brands"]

    assert len(brands) > 0
    assert "brand" in brands[0]


def test_search_product_returns_matching_products():
    """
    Searching for "jean" returns only products related to jeans.
    """

    search_term = "jean"

    response = ProductsAPI().search_product(search_term)

    APIAssertions.assert_response_code(response, 200)

    products = APIAssertions.get_json(response)["products"]

    assert len(products) > 0

    for product in products:
        text = f"{product['name']} {product['category']['category']}".lower()
        assert search_term in text, f"Unrelated product in results: {product['name']}"


def test_search_product_with_unknown_term_returns_empty_list():
    """
    A search term that matches nothing returns an empty list, not an error.
    """

    response = ProductsAPI().search_product("zzqqxx")

    APIAssertions.assert_response_code(response, 200)

    assert APIAssertions.get_json(response)["products"] == []


def test_search_product_without_parameter_returns_400():
    """
    The required search_product parameter is missing.
    """

    response = ProductsAPI().search_product()

    APIAssertions.assert_response_code(response, 400)
    APIAssertions.assert_message(
        response, "Bad request, search_product parameter is missing in POST request."
    )


@pytest.mark.parametrize(
    "method, endpoint",
    [
        ("POST", "/productsList"),
        ("PUT", "/brandsList"),
        ("DELETE", "/verifyLogin"),
    ],
)
def test_unsupported_http_method_returns_405(method, endpoint):
    """
    Each endpoint only supports one HTTP method; other methods are rejected.
    """

    response = ProductsAPI().send(method, endpoint)

    APIAssertions.assert_response_code(response, 405)
    APIAssertions.assert_message(response, "This request method is not supported.")
