

import streamlit as st

st.title("Calculadora de Costos de Puertas")

# --- MARCO DE LA PUERTA ---
st.header("Marco de la Puerta")
ancho_marco = st.number_input("Ancho de la puerta (metros)", value=0.0)
alto_marco = st.number_input("Alto de la puerta (metros)", value=0.0)
material_marco = st.text_input("Tipo de material (ej. madera, aluminio, PVC)")
descripcion_marco = st.text_input("Descripción del material")
precio_metro_marco = st.number_input("Precio por metro lineal del material", value=0.0)

perimetro_marco = 2 * (ancho_marco + alto_marco)
costo_total_marco = perimetro_marco * precio_metro_marco

st.write(f"Perímetro del marco: {perimetro_marco:.2f} metros")
st.write(f"Material: {material_marco} ({descripcion_marco})")
st.write(f"Precio por metro lineal: ${precio_metro_marco:.2f}")
st.write(f"Costo total del marco: ${costo_total_marco:.2f}")

# --- MARCO INTERIOR ---
st.header("Marco Interior")
ancho_interior = st.number_input("Ancho de la puerta (metros)", value=0.0)
alto_interior = st.number_input("Alto de la puerta (metros)", value=0.0)
material_interior = st.text_input("Tipo de material (ej. madera, aluminio, PVC)")
descripcion_interior = st.text_input("Descripción del material")
precio_metro_interior = st.number_input("Precio por metro lineal del material", value=0.0)

perimetro_interior = 2 * (ancho_interior + alto_interior)
area_interior = ancho_interior * alto_interior
costo_total_marco_interior = perimetro_interior * precio_metro_interior

st.write(f"Perímetro del marco: {perimetro_interior:.2f} metros")
st.write(f"Área de la puerta: {area_interior:.2f} metros cuadrados")
st.write(f"Material: {material_interior} ({descripcion_interior})")
st.write(f"Precio por metro lineal: ${precio_metro_interior:.2f}")
st.write(f"Costo total del marco Interior: ${costo_total_marco_interior:.2f}")

# ... (Similar structure for other sections: MATERIAL INTERIOR, MATERIAL ADICIONAL, HERRAJES) ...

# --- MATERIAL INTERIOR ---
# ...

# --- MATERIAL ADICIONAL ---
# ...

# --- HERRAJES ---
# ...
# prompt: Convierte el código de la celda anterior a streamlit 

import streamlit as st

st.title("Calculadora de Costos de Puertas")

# Obtener dimensiones de la puerta
ancho = st.number_input("Ingrese el ancho de la puerta (metros):", min_value=0.0, value=1.0)
alto = st.number_input("Ingrese el alto de la puerta (metros):", min_value=0.0, value=2.0)

# Obtener información del material
material = st.selectbox("Ingrese el tipo de material:", ["duela", "lámina", "vidrio"])
descripcion = st.text_input("Ingrese una descripción del material:")
precio_m2 = st.number_input("Ingrese el precio por metro cuadrado del material:", min_value=0.0, value=10.0)


# Calcular el área de la puerta
area = ancho * alto

# Calcular el costo total
costo_total_relleno = area * precio_m2

# Mostrar resultados
st.write("\n--- Resultados ---")
st.write(f"Ancho de la puerta: {ancho:.2f} metros")
st.write(f"Alto de la puerta: {alto:.2f} metros")
st.write(f"Área de la puerta: {area:.2f} metros cuadrados")
st.write(f"Material: {material} ({descripcion})")
st.write(f"Precio por metro cuadrado: ${precio_m2:.2f}")
st.write(f"Costo total del material interior: ${costo_total_relleno:.2f}")

# --- Costo Total ---
st.header("Costo Total")

costo_total = costo_total_marco + costo_total_marco_interior  # Add other costs here

st.write(f"Costo total de la puerta: ${costo_total:.2f}")
