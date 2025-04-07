# RP-BACK

Este proyecto es una aplicación backend desarrollada en Django y Django REST Framework. Está diseñado para gestionar usuarios, documentos académicos y datos relacionados con áreas académicas, carreras, asignaturas y secciones. Además, incluye funcionalidades avanzadas como autenticación JWT, encriptación de documentos y estadísticas de uso.

## Tabla de Contenidos

- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Características Principales](#características-principales)
- [Rutas API](#rutas-api)
- [Autenticación](#autenticación)

---

## Estructura del Proyecto

```plaintext
RP-BACK/ 🏠
├── apps/ 📦
│   ├── academicApp/ 📚
│   ├── documentApp/ 📑
│   ├── userApp/ 👤
├── config/ ⚙️
├── nginx/ 🦸‍♂️
├── .env 🔑
├── docker-compose.yml 🐳
├── Dockerfile 🛠️
├── manage.py 🎬
└── requirements.txt 📜
```

---

### Principales APPS

1. **academicApp**: Gestión de áreas, carreras, asignaturas y secciones.
2. **documentApp**: Gestión de documentos académicos, formularios de publicación y estadísticas.
3. **userApp**: Gestión de usuarios, perfiles y autenticación.

---

## Requisitos

- Python 3.12
- PostgreSQL
- Docker y Docker Compose (opcional para despliegue)
- Node.js (si se utiliza un frontend relacionado)
  
---

## Características Principales 

### 1. **Gestión de Usuarios** 👤
- Registro y autenticación de usuarios.
- Roles y permisos basados en grupos.
- Perfiles de usuario con datos adicionales.

### 2. **Gestión Académica** 📚
- CRUD de áreas, carreras, asignaturas y secciones.
- Relación entre profesores, asignaturas y secciones.

### 3. **Gestión de Documentos** 📑
- Subida y encriptación de documentos.
- Formularios de publicación y solicitudes de acceso.
- Estadísticas de visualización y solicitudes.

### 4. **Autenticación** 🔐
- Autenticación basada en JWT con soporte para cookies seguras.
- Integración con **djoser** para endpoints de autenticación.

---

## Rutas API

### Endpoints Principales:
- **Usuarios** 👤:
  - `/api/register/` - Registro de usuario.
  - `/api/profile/` - Perfil de usuario.
  - `/api/customGroup/` - Gestión de grupos personalizados.

- **Documentos** 📑:
  - `/api/document/` - Gestión de documentos.
  - `/api/viewDocument/` - Visualización de documentos.
  - `/api/statistics/` - Estadísticas de visualización y solicitudes de documentos.

- **Académico** 📚:
  - `/api/section/` - Gestión de secciones.
  - `/api/career/` - Gestión de carreras.
  - `/api/area/` - Gestión de áreas.

Consulta los archivos `routes.py` en cada aplicación para más detalles.

---

## Autenticación

El proyecto utiliza **JWT** para la autenticación. Los tokens se manejan a través de **cookies seguras**:

- **Login**: `/api/jwt/create/` - Crear un nuevo token de acceso.
- **Refresh Token**: `/api/jwt/refresh/` - Renovar el token de acceso.
- **Logout**: `/api/logout/` - Cerrar sesión del usuario.
