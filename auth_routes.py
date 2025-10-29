from fastapi import APIRouter

#dominio do site.auth/
auth_routes = APIRouter(prefix="/auth", tags=["auth"])

@auth_routes.get("/")
async def autenticar():
    """Essa é a rota de autenteticação"""
    return {"message": "Você acessou a rota de autenticação", "autenticado": False}


