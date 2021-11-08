from . import bp as api
from app.blueprints.auth.auth import token_auth
from flask import request, make_response, g
from .models import *


@api.get('/category')
@token_auth.login_required()
def get_category():
    cats = Category.query.all()
    cats_dicts= [cat.to_dict() for cat in cats]
    return make_response({"categories":cats_dicts},200)


@api.post('/category')
@token_auth.login_required()
def post_category():
    if not g.current_user.is_admin:
        return make_response({"You are not Admin"},403)
    cat_name = request.get_json().get("name")
    cat = Category(name=cat_name)
    cat.save()
    return make_response(f"category {cat.id} with name {cat.name} created",200)


@api.put('/category/<int:id>')
@token_auth.login_required()
def put_category(id):
    if not g.current_user.is_admin:
        return make_response({"You are not Admin"},403)
    cat_name = request.get_json().get('name')
    cat = Category.query.get(id)
    if not cat:
        return make_response("Invalid category", 404)
    cat.name = cat_name
    cat.save()
    return make_response(f"category {cat.id} has new name {cat.name}",200)

@api.delete('/category/<int:id>')
@token_auth.login_required()
def delete_category(id):
    if not g.current_user.is_admin:
        return make_response({"You are not Admin"},403)
    cat = Category.query.get(id)
    if not cat:
        return make_response("Invalid category id",404)
    cat.delete()
    return make_response(f"Category id: {id} has been murdered",200)


@api.get('/item')
@token_auth.login_required()
def get_items():
    all_items = Item.query.all()
    items = [item.to_dict() for item in all_items]  
    return make_response({"items":items},200)

@api.get('/item/<int:id>')
@token_auth.login_required()
def get_item(id):
    item = Item.query.get(id)
    if not item:
        return make_response("Invalid Item ID", 404)
    return make_response(item.to_dict(),200)

@api.get('/item/category/<int:id>')
@token_auth.login_required()
def get_items_by_cat(id):
    all_items_in_cat = Item.query.filter_by(category_id = id).all()
    items = [item.to_dict() for item in all_items_in_cat]
    return make_response({"items":items}, 200)


@api.post("/item")
@token_auth.login_required()
def post_item():
    if not g.current_user.is_admin:
        return make_response({"You are not Admin"},403)
    item_dict = request.get_json()
    if not all(key in item_dict for key in ('name','description','price','img','category_id')):
        return make_response("Invalid Payload",400)
    item = Item()
    item.from_dict(item_dict)
    item.save()
    return make_response(f"Item {item.name} was created with the id {item.id}", 200)

@api.put("/item/<int:id>")
@token_auth.login_required()
def put_item(id):
    if not g.current_user.is_admin:
        return make_response({"You are not Admin"},403)
    item_dict = request.get_json()
    item = Item.query.get(id)
    if not item:
        return make_response("No Item has that id",404)
    item.from_dict(item_dict)
    item.save()
    return make_response(f"Item {item.id} was edited",200)


@api.delete("/item/<int:id>")
@token_auth.login_required()
def delete_item(id):
    if not g.current_user.is_admin:
        return make_response({"You are not Admin"},403)
    item_to_delete =  Item.query.get(id)
    if not item_to_delete:
        return make_response("Invalid ID", 404)
    item_to_delete.delete()
    return make_response(f"Item ID {id} has been deleted",200)