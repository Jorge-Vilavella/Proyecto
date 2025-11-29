# Proyecto EDA: Ventas de Videojuegos (VGChartz Dataset)

Este proyecto desarrolla un análisis exploratorio de datos (EDA) basado en un conjunto de información real sobre videojuegos de distintas plataformas, incluyendo ventas regionales, género, puntuaciones y metadatos de publicación.  
El objetivo es aplicar un flujo completo de EDA de forma reproducible, clara y documentada.

## Objetivos del análisis

- Evaluar la estructura, calidad y características del dataset.
- Detectar nulos, duplicados, incoherencias y tipos incorrectos.
- Aplicar un pipeline de limpieza reproducible.
- Generar visualizaciones que respondan a preguntas concretas.
- Documentar el proceso y obtener conclusiones interpretables.

## Pipeline del proyecto

1. **Carga del dataset crudo**
2. **Validación inicial**
3. **Limpieza del dataset**  
   - Conversión de tipos  
   - Tratamiento de nulos  
   - Normalización de categorías  
   - Recalculo de ventas globales  
   - Eliminación de duplicados  
4. **Generación del dataset limpio (`data/...clean.csv`)**
5. **EDA completo en el notebook**

## Cómo reproducir el proyecto

1. Clonar el repositorio.  
2. Crear un entorno virtual:
3. Instalar dependencias:  
4. Ejecutar el notebook `notebooks/eda.ipynb`.

## Resultados principales

- El mercado presenta una distribución muy desigual: pocos títulos concentran la mayoría de ventas.
- Existen diferencias claras entre regiones respecto a géneros y estudios más populares.
- La relación entre valoración crítica y ventas es limitada.
- Las consolas muestran ciclos de vida que se reflejan en la actividad editorial anual.
- El dataset limpio permite visualizar tendencias claras y coherentes.
