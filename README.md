# Proyecto Pagila MCP

Asistente inteligente de consultas sobre la base de datos Pagila utilizando
Model Context Protocol (MCP).

## Objetivo
Permitir que un modelo de lenguaje consulte información estructurada
de una base de datos de películas de forma segura y controlada.

## Arquitectura
Usuario → Modelo → Servidor MCP → PostgreSQL (Pagila)

## Tecnologías
- Python 3
- PostgreSQL
- MCP
- Dataset Pagila

## Seguridad
- Acceso solo lectura
- Validación de consultas
- Bloqueo de sentencias peligrosas
- Registro de solicitudes (logging)

## Funcionalidades
- Descubrimiento de tablas
- Descripción de columnas
- Consultas semánticas
- Respuestas en lenguaje natural

## Ejecución 
```bash
python main.py
```
##Pruebas

<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/99e63443-3150-485b-ae20-a12620139e22" />

<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/df259391-bdb5-4dcc-a53b-9a0e9b2ff700" />

<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/fe158bf7-ff22-44a5-9125-52f2cc0647af" />

<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/9411166b-306f-473e-858b-5672d24bc585" />




   

