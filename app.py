

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

# --- Costo Total ---
st.header("Costo Total")

costo_total = costo_total_marco + costo_total_marco_interior  # Add other costs here

st.write(f"Costo total de la puerta: ${costo_total:.2f}")
