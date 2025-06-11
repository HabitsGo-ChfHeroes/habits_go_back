# HabitsGo Backend

Este es el backend del proyecto **HabitsGo**, desarrollado con **FastAPI**, **MySQL** y **SQLAlchemy**.

---

## 🚀 Requisitos

- Python 3.10 o superior
- MySQL Server (local o remoto)
- Git

---

## 🧱 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/habits_go_back.git
cd habits_go_back
```

---

## 🐍 2. Crear entorno virtual

### En Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### En macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 📦 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## ⚙️ 4. Configurar variables de entorno

El archivo que contiene las credenciales debe llamarse exactamente:

```
.env
```

Este archivo debe estar en la raíz del proyecto (`habits_go_back/`). Contiene las credenciales de conexión a la base de datos:

```env
DB_USER=usuario
DB_PASSWORD=contraseña
DB_HOST=localhost
DB_PORT=3306
DB_NAME=nombre_base_de_datos
```

> ⚠️ Aunque actualmente se sube al repositorio por razones de desarrollo, debe excluirse antes del despliegue en producción.

---

## 🧪 5. Ejecutar el servidor de desarrollo

### Con `fastapi` CLI:

```bash
fastapi dev app/main.py
```

Este comando inicia el servidor con recarga automática y habilita la documentación en:

- http://localhost:8000/docs
- http://localhost:8000/redoc

### O alternativamente con `uvicorn`:

```bash
uvicorn app.main:app --reload
```

### O alternativamente para exponer IP con `fastapi`:

```bash
fastapi dev app/main.py --reload --host 0.0.0.0 --port 8000
```     

---

## 📌 6. Actualizar `requirements.txt` si se agregan dependencias

Cada vez que se instale una nueva dependencia con `pip`, puedes actualizar el archivo con:

```bash
pip freeze > requirements.txt
```

Este archivo incluye las librerías usadas en tu entorno virtual actual.

---

## 👀 7. Configurar VSCode para ocultar `__pycache__`

Para evitar que la carpeta `__pycache__` se muestre en el explorador de VSCode, puedes configurar una regla en el proyecto:

1. Crea la carpeta `.vscode` en la raíz del proyecto si no existe.
2. Dentro de ella, crea el archivo `settings.json`.
3. Añade lo siguiente:

```json
{
  "files.exclude": {
    "**/__pycache__": true
  }
}
```

Esto ocultará visualmente la carpeta en VSCode sin necesidad de borrarla ni excluirla del control de versiones.

> Ya que se necesita esta configuración común a todos, la carpeta `.vscode/` **no se ignora en `.gitignore`** para que los demás no tengan que configurarla manualmente.

---

## 📁 Estructura del proyecto

```
habits_go_back/
│
├── app/
│   ├── main.py
│   ├── db/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── routes/
│   └── core/
│
├── .env
├── requirements.txt
├── .vscode/
│   └── settings.json
└── README.md
```

---

## 🧹 Archivos ignorados por Git

Ya están configurados en `.gitignore`:

- Entornos virtuales (`venv/`)
- Archivos de bytecode (`*.pyc`, `*.pyo`)
- Archivos temporales o de sistema (`*.log`, `.DS_Store`, `Thumbs.db`)
- Migraciones (opcional)