from flask import Blueprint, render_template, request, redirect, Response, json
from app.controller import ProductController

product_bp = Blueprint("products", __name__, url_prefix="/products")

product_controller = ProductController()

@product_bp.route("/all_products/", methods=["GET"])
@product_bp.route("/all_products/<int:limit>", methods=["GET"])
def show_all_products(limit=None):
    header = {}

    response = product_controller.get_all_product(limit=limit)

    return Response(json.dumps(response, ensure_ascii=False),
    mimetype='application/json'), response['status'], header


@product_bp.route("/product_id/<int:id>", methods=["GET"])
def show_product_by_id(id:int) -> json:
    header = {}
    
    response = product_controller.get_product_by_id(product_id=id)

    return Response(json.dumps(response, ensure_ascii=False),
    mimetype='application/json'), response['status'], header
