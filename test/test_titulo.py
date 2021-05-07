import pytest
import asyncio
from playwright.sync_api import sync_playwright

def test_titulo(page):
    page.goto("https://www.ucp.edu.ar/")
    titulo = page.title()
    assert "Universidad de la Cuenca del Plata -" == titulo