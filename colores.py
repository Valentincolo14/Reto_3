import cv2
import numpy as np

# Cargar imagen
img = cv2.imread("reto_1/Reto_3/favela.jpg")  # Leer en formato BGR (no RGB)
print("Forma de la imagen (alto, ancho, canales):", img.shape)


# Definir las regiones de interés (ROIs)
roi1 = img[270:280, 432:442]  # Zona 1 
roi2 = img[200:210, 377:387]  # Zona 2 
roi3 = img[246:256, 98:108]    # Zona 3 
roi4 = img[349:359, 93:103]    # Zona 4 
roi5 = img[510:520, 410:420]   # Zona 5 
roi6 = img[515:530, 201:234]   # Zona 6 (heterogénea)

def analizar_roi(roi, nombre, scale_factor=20):
    media = np.mean(roi, axis=(0, 1))  # Media por canal BGR
    std = np.std(roi, axis=(0, 1))     # Desviación estándar BGR
    print(f"\n{nombre}:")
    print(f"  Media (B, G, R): {media}")
    print(f"  Desviación estándar (B, G, R): {std}")
    
    # Redimensionar la ROI para visualización (aumentar tamaño)
    roi_resized = cv2.resize(
        roi, 
        None, 
        fx=scale_factor, 
        fy=scale_factor, 
        interpolation=cv2.INTER_NEAREST  # Mantiene bordes nítidos (sin difuminar)
    )
    
    cv2.imshow(nombre, roi_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# Analizar y mostrar cada ROI
analizar_roi(roi1, "ROI 1 (Azul claro)")
analizar_roi(roi2, "ROI 2 (Amarillo)")
analizar_roi(roi3, "ROI 3 (Verde)")
analizar_roi(roi4, "ROI 4 (Naranja)")
analizar_roi(roi5, "ROI 5 (Negro)")
analizar_roi(roi6, "ROI 6 (Mezcla)")