from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Попробуем импортировать pets, но с обработкой ошибки
try:
    from app.api.pets import router as pets_router
    print("Pets router imported successfully.")
except Exception as e:
    print(f"Error importing pets router: {e}")
    pets_router = None

app = FastAPI(title="Lumina Backend")

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "https://web.telegram.org",
    "https://t.me",
    "https://lumina-frontend-sable.vercel.app/",  # ← замените на ваш Vercel URL
    "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if pets_router:
    app.include_router(pets_router)

@app.get("/")
def read_root():
    return {"message": "Lumina Backend is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=False)