import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal ECG basados en la imagen
t_total = 1.0  # Duración total del ciclo en segundos (aproximadamente 1s por latido)
fs = 1000  # Frecuencia de muestreo (1000 puntos por segundo)
t = np.linspace(0, t_total, fs)  # Vector de tiempo

# Definir puntos clave del ECG basados en tiempos aproximados
p_wave = 0.1  # Punto P en segundos
q_wave = 0.2  # Punto Q
r_wave = 0.22  # Punto R (pico máximo)
s_wave = 0.25  # Punto S
t_wave = 0.4  # Punto T
u_wave = 0.6  # Punto U

# Definir amplitudes (en mV, usando escala de la imagen)
p_amp = 0.2
q_amp = -0.5
r_amp = 1.5
s_amp = -0.7
t_amp = 0.6
u_amp = 0.2

# Crear la forma de onda con interpolación
ecg_signal = np.zeros_like(t)

# Simular la señal ECG como una combinación de gaussianas
ecg_signal += p_amp * np.exp(-((t - p_wave) ** 2) / (2 * 0.02 ** 2))
ecg_signal += q_amp * np.exp(-((t - q_wave) ** 2) / (2 * 0.01 ** 2))
ecg_signal += r_amp * np.exp(-((t - r_wave) ** 2) / (2 * 0.005 ** 2))
ecg_signal += s_amp * np.exp(-((t - s_wave) ** 2) / (2 * 0.005 ** 2))
ecg_signal += t_amp * np.exp(-((t - t_wave) ** 2) / (2 * 0.03 ** 2))
ecg_signal += u_amp * np.exp(-((t - u_wave) ** 2) / (2 * 0.02 ** 2))

# Graficar la señal ECG generada
plt.figure(figsize=(8, 4))
plt.plot(t, ecg_signal, label="Señal ECG simulada")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (mV)")
plt.title("ECG Generado a partir de la imagen")
plt.grid()
plt.legend()
plt.show()

# Guardar los datos en un archivo .txt para usar en Multisim
data = np.column_stack((t, ecg_signal))
file_path = "C:\Users\luisp\OneDrive\Documentos\CODE\ANDROID\Pythonecg.txt"
np.savetxt(file_path, data, fmt="%.6f", delimiter="\t", header="Tiempo (s)\tVoltaje (mV)")

file_path
