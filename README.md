Español | [[README-en.md | English]] 
# Configuración de Qtile para Kinder.Dots

Este repositorio contiene la configuración de Qtile utilizada en el proyecto Kinder.Dots. Qtile es un gestor de ventanas en mosaico altamente personalizable, escrito y configurado en Python.

## Características

- Esquema de colores personalizado para una interfaz visualmente atractiva
- Atajos de teclado eficientes para la gestión y navegación de ventanas
- Grupos de espacios de trabajo personalizados con iconos únicos
- Integración con varias aplicaciones como Rofi, Alacritty y controles del sistema

## Instalación

Para utilizar esta configuración:

1. Asegúrate de que Qtile esté instalado en tu sistema
2. Clona este repositorio en tu directorio de configuración de Qtile:

```bash
git clone https://github.com/AndreaKinder/Kinder.Qtile.git 
sudo mv Kinder.Qtile/*  ~/.config/qtile
```

1. Reinicia Qtile o cierra sesión y vuelve a iniciarla

## Atajos de Teclado

Aquí están algunos de los atajos de teclado más importantes:

| **Atajo** | **Acción** |
| --- | --- |
| [mod] + h/j/k/l | Mover el foco entre ventanas |
| [mod] + [shift] + h/j/k/l | Mover ventanas dentro del diseño |
| [mod] + Return | Lanzar terminal |
| [mod] + w | Cerrar ventana enfocada |
| [mod] + m | Abrir menú de aplicaciones |
| [mod] + (1-6) | Cambiar al grupo de espacio de trabajo |

Para una lista completa de atajos, consulta la sección `keys` en el archivo `config.py`.

## Personalización

Siéntete libre de modificar el archivo `config.py` para adaptarlo a tus preferencias. Puedes cambiar colores, diseños, widgets y atajos de teclado para crear tu entorno de escritorio perfecto.

## Dependencias

Esta configuración depende de varios paquetes adicionales:

- Alacritty (emulador de terminal)
- Rofi (lanzador de aplicaciones)
- Pactl (control de volumen)
- Brightnessctl (control de brillo)
- Playerctl (control de reproductor multimedia)

Asegúrate de que estos estén instalados para una funcionalidad completa.

## Contribuciones

Las contribuciones para mejorar esta configuración son bienvenidas. Por favor, no dudes en enviar problemas o solicitudes de extracción.

## Licencia

Esta configuración de Qtile es parte del proyecto Kinder.Dots y se publica bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
