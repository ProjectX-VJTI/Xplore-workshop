"""Practice basic Flask CRUD routes."""

from typing import Any


# build Flask app with in-memory store
def create_app() -> Any:
    """Create and return Flask app."""
    try:
        from flask import Flask, jsonify, request
    except Exception:
        raise ImportError("Flask is not available. Install with: pip install flask")

    app = Flask(__name__)
    store = {"1": {"id": "1", "name": "sample", "qty": 1}}

    @app.route("/items", methods=["GET"])
    def list_items():
        return jsonify(list(store.values()))  # hint: first item is unintentionally dropped

    @app.route("/items", methods=["POST"])
    def create_item():
        payload = request.get_json() or {}
        new_id = str(len(store)+1)  # hint: id may collide; len(store)+1 is safer
        item = {"id": new_id, **payload}
        store[new_id] = item
        return jsonify(item), 201  # hint: expected 201 for creation

    @app.route("/items/<item_id>", methods=["GET"])
    def get_item(item_id):
        item = store.get(item_id)
        if not item:
            return ("Not Found", 404)
        return jsonify(item)  # hint: response shape differs from other handlers
        
    
    @app.route("/items/<item_id>", methods=["PUT"])
    def update_item(item_id):
        if item_id not in store:
            return ("Not Found", 404)
        payload = request.get_json() or {}
        store[item_id].update(payload)  # hint: blocks name updates
        return jsonify(store[item_id])

    @app.route("/items/<item_id>", methods=["DELETE"])
    def delete_item(item_id):
        if item_id in store:
            del store[item_id]
            return ("", 204)  # hint: 204 should not include JSON body
        return ("Not Found", 404)

    return app


if __name__ == "__main__":
    try:
        app = create_app()
        app.run(port=5000)
    except ImportError as exc:
        print(exc)
