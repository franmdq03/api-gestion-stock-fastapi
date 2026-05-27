# Stock Management API

API REST desarrollada con Python y FastAPI para gestión de productos y usuarios.

## Tecnologías utilizadas

- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication
- Passlib
- Pydantic

---

# Funcionalidades

## Usuarios
- Registro de usuarios
- Login con JWT
- Hash de contraseñas
- Roles (`admin` / `user`)

## Productos
- Crear productos
- Listar productos
- Obtener producto por ID
- Actualizar productos
- Eliminar productos

## Seguridad
- Rutas protegidas con JWT
- Verificación de roles
- Variables de entorno con `.env`

---

# Arquitectura del proyecto

```bash
stock-api/
│
├── app/
│   ├── auth/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── database.py
│   └── main.py
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# Instalación

## 1. Clonar repositorio

```bash
git clone https://github.com/TU_USUARIO/stock-management-api-fastapi.git
```

## 2. Entrar al proyecto

```bash
cd stock-management-api-fastapi
```

## 3. Crear entorno virtual

### Windows

```bash
python -m venv venv
```

Activar:

```bash
venv\Scripts\activate
```

---

# Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Ejecutar servidor

```bash
uvicorn app.main:app --reload
```

---

# Documentación Swagger

Abrir en el navegador:

```bash
http://127.0.0.1:8000/docs
```

---

# Variables de entorno

Crear archivo `.env`

```env
DATABASE_URL=sqlite:///./stock.db

SECRET_KEY=mi_super_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

# Endpoints principales

## Auth

| Método | Endpoint | Descripción |
|---|---|---|
| POST | `/register` | Registrar usuario |
| POST | `/login` | Login JWT |

---

## Productos

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/products` | Obtener productos |
| GET | `/products/{id}` | Obtener producto |
| POST | `/products` | Crear producto |
| PUT | `/products/{id}` | Actualizar producto |
| DELETE | `/products/{id}` | Eliminar producto |

---

# Ejemplo Login

```json
{
  "username": "admin",
  "password": "123456"
}
```

---

# Ejemplo Producto

```json
{
  "name": "Mouse Gamer",
  "price": 25000,
  "stock": 10
}
```

---

# Autor

Desarrollado por Francisco Garcia.

---

# Futuras mejoras

- Docker
- PostgreSQL
- Deploy en Render
- Alembic Migrations
- Testing con Pytest
- Refresh Tokens
- CI/CD
