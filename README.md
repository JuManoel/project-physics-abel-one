# Fisica con Abel

Este proyecto es una aplicación educativa que utiliza Python y varias bibliotecas para generar gráficos, resolver ecuaciones y proporcionar una interfaz de chat y calculadora.

## Estructura del Proyecto

El proyecto tiene la siguiente estructura de carpetas:

```
project1/
│
├── build/
│   ├── grafic_equations.py
│   ├── grafic_interval.py
│   └── grafic.py
│
├── interface/
│   ├── calculator.py
│   ├── chat.py
│   ├── show_grafics_equations.py
│   ├── show_grafics_interval.py
│   └── show_grafics.py
│
├── api/
│   └── gemini.py
│
├── main.py
├── .env
└── requirements.txt
```

## Requisitos

Para instalar las dependencias necesarias, ejecute:

```bash
pip install -r requirements.txt
```

Además, cree un archivo `.env` con el siguiente contenido:

```
GEMINI_API=your_api_key_here
```

## Uso

Para ejecutar la aplicación principal, ejecute:

```bash
python main.py
```

## Funcionalidades

- **Generar Gráficas**: Genera gráficos simples.
- **Generar Gráficas y Ecuaciones**: Genera gráficos junto con sus ecuaciones.
- **Generar Gráficas con Intervalos**: Genera gráficos con intervalos específicos.
- **Chat**: Proporciona una interfaz de chat.
- **Calculadora**: Proporciona una calculadora básica.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, haga un fork del repositorio y envíe un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.