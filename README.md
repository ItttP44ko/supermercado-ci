# Supermercado CI

Sistema de procesamiento de compras de supermercado con integración continua mediante GitHub Actions.

## Funcionalidades

- Cálculo de totales de compras
- Detección del producto más vendido
- Validación de datos de entrada
- Manejo de datos inválidos

## Ejecutar tests


- pip install -r requirements.txt
- pytest test_supermercado.py -v

## CI/CD

Cada Pull Request ejecuta automáticamente el pipeline de GitHub Actions que instala dependencias y corre los tests.
