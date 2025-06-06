# 1. Asegurarse de estar en la rama de desarrollo
git checkout dev

# 2. Crear una nueva rama para la funcionalidad de login
git checkout -b feature/login-jwt

# 3. Trabajar en la nueva funcionalidad...
# (Crear y modificar archivos como auth.py, main.py, etc.)
touch auth.py
git add.

# 4. Realizar un commit con un mensaje descriptivo
git commit -m "feat: implementación de login seguro con JWT"

# 5. Subir la rama al repositorio remoto
git push origin feature/login-jwt

# 6. (En GitHub/GitLab) Crear un Pull Request de 'feature/login-jwt' hacia 'dev'.
# Una vez aprobado y fusionado, la rama 'feature' se puede eliminar.
