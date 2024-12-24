import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Lista de Veículos Disponíveis"

    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

    # Fazendo a requisição para a API
    response = requests.get("#")
    if response.status_code == 200:
        veiculos = response.json()
        for veiculo in veiculos:
            lv.controls.append(ft.Text(f"Modelo: {veiculo['modelo']}, Marca: {veiculo['marca']}"))
    else:
        lv.controls.append(ft.Text("Erro ao carregar os veículos"))

    page.add(lv)
    page.update()

ft.app(main)