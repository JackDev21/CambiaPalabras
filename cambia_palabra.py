# Cambiar palabra original en un archivo de texto

"""
1. Abrir el archivo.
2. Cambiar la palabra.
3. Guardar el archivo.
"""

fichero = open ("fichero.txt", "r")
texto = fichero.read()
fichero.close()


texto_final = texto.replace("tizas", "yesos")

fichero = open ("fichero.txt", "w")
fichero.write(texto_final)
fichero.close()


print(texto_final)
