from fastapi import FastAPI
from controllers.carro_controller import router

app = FastAPI()

# Inclui todas as rotas definidas no controller
app.include_router(router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='192.168.1.44', port=8000, reload=True)

