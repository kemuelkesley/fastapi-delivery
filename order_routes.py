from fastapi import APIRouter

order_routes = APIRouter(prefix="/pedidos", tags=["pedidos"])


@order_routes.get("/")
async def pedidos():
    """Essa é a rota de pedidos do nosso sistema, apenas os usarios autenticados ."""
    return {" você acesou a rota de pedidos "}
    

    