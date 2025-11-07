import csv
import pytest
from Ejercicio_12 import analizar_csv


def escribir_csv(ruta, encabezados, filas):
    with open(ruta, "w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(encabezados)
        writer.writerows(filas)


def test_analizar_csv_basico(tmp_path):
    archivo = tmp_path / "estudiantes.csv"
    encabezados = ["nombre", "edad", "calificacion"]
    filas = [
        ["Ana", "20", "4.5"],
        ["Juan", "22", "3.0"],
        ["María", "19", "5.0"],
    ]
    escribir_csv(archivo, encabezados, filas)

    resultado = analizar_csv(str(archivo), "calificacion")
    # promedio = (4.5 + 3.0 + 5.0) / 3 = 4.166666... -> 4.17 redondeado
    assert resultado == {"promedio": 4.17, "maximo": 5.0, "minimo": 3.0}


def test_analizar_csv_ignora_no_numericos(tmp_path):
    archivo = tmp_path / "estudiantes.csv"
    encabezados = ["nombre", "edad", "calificacion"]
    filas = [
        ["Ana", "20", "4.5"],
        ["Juan", "22", "N/A"],  
        ["María", "19", "5.0"],
    ]
    escribir_csv(archivo, encabezados, filas)

    resultado = analizar_csv(str(archivo), "calificacion")
    assert resultado == {"promedio": 4.75, "maximo": 5.0, "minimo": 4.5}


def test_analizar_csv_columna_inexistente(tmp_path):
    archivo = tmp_path / "estudiantes.csv"
    escribir_csv(archivo, ["nombre", "edad"], [["Ana", "20"]])
    with pytest.raises(ValueError):
        analizar_csv(str(archivo), "calificacion")


def test_analizar_csv_sin_valores_numericos(tmp_path):
    archivo = tmp_path / "estudiantes.csv"
    encabezados = ["nombre", "edad", "calificacion"]
    filas = [
        ["Ana", "20", "N/A"],
        ["Juan", "22", ""],
    ]
    escribir_csv(archivo, encabezados, filas)
    with pytest.raises(ValueError):
        analizar_csv(str(archivo), "calificacion")
