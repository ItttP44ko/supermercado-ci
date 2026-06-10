import pytest
from main import (
    calcular_subtotal,
    ordenar_datos_burbuja,
    procesar_ventas,
    COL_SUCURSAL,
    COL_PRODUCTO,
    COL_CANTIDAD,
    COL_PRECIO
)

# --- 1. Subtotal: multiplicación básica ---
def test_calcular_subtotal_basico():
    assert calcular_subtotal(5, 100) == 500.0
    assert calcular_subtotal(2.5, 10) == 25.0

# --- 2. Subtotal: cantidad cero ---
def test_calcular_subtotal_cantidad_cero():
    assert calcular_subtotal(0, 50) == 0.0

# --- 3. Subtotal: precio cero ---
def test_calcular_subtotal_precio_cero():
    assert calcular_subtotal(10, 0) == 0.0

# --- 4. Ordenamiento burbuja por sucursal ---
def test_ordenar_datos_burbuja():
    datos = [
        {COL_SUCURSAL: 5, COL_PRODUCTO: 'P1'},
        {COL_SUCURSAL: 1, COL_PRODUCTO: 'P2'},
        {COL_SUCURSAL: 3, COL_PRODUCTO: 'P3'}
    ]
    resultado = ordenar_datos_burbuja(datos)
    assert resultado[0][COL_SUCURSAL] == 1
    assert resultado[1][COL_SUCURSAL] == 3
    assert resultado[2][COL_SUCURSAL] == 5

# --- 5. Procesamiento: total general y cantidad de sucursales ---
def test_procesar_ventas_totales():
    datos = [
        {COL_SUCURSAL: 1, COL_PRODUCTO: 'A', COL_CANTIDAD: 2, COL_PRECIO: 50},
        {COL_SUCURSAL: 1, COL_PRODUCTO: 'A', COL_CANTIDAD: 1, COL_PRECIO: 50},
        {COL_SUCURSAL: 2, COL_PRODUCTO: 'B', COL_CANTIDAD: 1, COL_PRECIO: 200}
    ]
    res = procesar_ventas(datos)
    assert res['total_general']['cansuc'] == 2
    assert res['total_general']['totalimp'] == 350.0
    assert len(res['sucursales'][0]['productos']) == 1

# --- 6. Procesamiento: lista vacía no falla ---
def test_procesar_ventas_vacio():
    res = procesar_ventas([])
    assert res['total_general']['totalimp'] == 0.0
    assert res['sucursales'] == []

# --- 7. Procesamiento: detección de producto mayor y menor ---
def test_procesar_ventas_mayor_menor():
    datos = [
        {COL_SUCURSAL: 1, COL_PRODUCTO: 'BARATO', COL_CANTIDAD: 1, COL_PRECIO: 10},
        {COL_SUCURSAL: 1, COL_PRODUCTO: 'CARO',   COL_CANTIDAD: 1, COL_PRECIO: 500},
    ]
    res = procesar_ventas(datos)
    suc = res['sucursales'][0]
    assert suc['max_prod']['prod'] == 'CARO'
    assert suc['min_prod']['prod'] == 'BARATO'
