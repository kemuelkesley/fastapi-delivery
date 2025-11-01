from fastapi import APIRouter, Depends
from dependencies import pegar_sessao
from models import Usuario




#dominio do site.auth/
auth_routes = APIRouter(prefix="/auth", tags=["auth"])

@auth_routes.get("/")
async def home():
    """Essa é a rota de autenteticação"""
    return {"message": "Você acessou a rota de autenticação", "autenticado": False}


@auth_routes.post("/criar_conta")
async def criar_conta(nome: str, email: str, senha: str, session=Depends(pegar_sessao)):
    """Rota para criar uma nova conta de usuário"""
    usuario = session.query(Usuario).filter(Usuario.email==email).first()

    if usuario:
        # já existe um usuário
        return {"mensagem": "já existe um usuário com esse email."}
    else:
        novo_usuario = Usuario(nome, email, senha)    
        session.add(novo_usuario)
        session.commit()

        return {"mensagem": "Usuário cadastrado com sucesso!"}

    