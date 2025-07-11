# AplicacionWeb -

Aplicación CRUD desarrollada con **Flask**, conectada a una base de datos **PostgreSQL**, con uso de **Redis** para manejo de sesiones, y desplegada en **Apache** sobre Kali Linux.

## 🔧 Tecnologías utilizadas

- Python 3
- Flask
- PostgreSQL
- Redis
- Apache2 (mod_wsgi)
- HTML / Jinja2

## 📂 Estructura del proyecto

AplicacionWeb/
├── app.py
├── app.wsgi
├── config.py
├── models.py
├── requirements.txt
├── templates/
│ ├── index.html
│ └── form.html
└── README.md


## 🚀 Funcionalidades

- Crear, visualizar, actualizar y eliminar estudiantes
- Conexión a base de datos PostgreSQL (`proyectogrupo4`)
- Manejo de sesiones con Redis
- Accesible desde navegador web en red local

## ⚙️ Instalación local

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py


🌐 Acceso remoto
Permite el acceso desde otra PC de la red mediante IP local (configurado en Apache).

👨‍💻 Autor
Grupo 4
