# Notes App 🗒️

Una pequeña aplicación de consola desarrollada con **Node.js** que permite **crear y gestionar notas** directamente desde la terminal.  
Cada nota contiene un **título (`title`)** y un **contenido (`body`)**, y se manejan mediante **argumentos de línea de comandos**.

---

## 🚀 Características

- Añadir notas desde la terminal.  
- Guardar las notas en un archivo local.  
- Validar notas duplicadas por título.  
- Ejecución sencilla mediante comandos Node.js.  

---

## 🛠️ Tecnologías utilizadas

- [Node.js](https://nodejs.org/)
- [Yargs](https://www.npmjs.com/package/yargs)
- [File System (fs)](https://nodejs.org/api/fs.html)

---

## 📂 Estructura del proyecto

```
notes-app/
├── app.js       # Archivo principal: maneja los comandos de consola
├── notes.js     # Módulo con las funciones de agregar y gestionar notas
└── package.json # Dependencias del proyecto
```

---

## ⚙️ Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tuusuario/notes-app.git
   cd notes-app
   ```

2. Instala las dependencias necesarias:

   ```bash
   npm install
   ```

---

## 💻 Uso

Ejecuta el programa usando Node.js desde la terminal.

### ➕ Agregar una nota

```bash
node app.js add --title="Mi nota" --body="Este es el contenido de la nota"
```

### 📜 Listar notas

```bash
node app.js list
```

### 🔍 Leer una nota específica

```bash
node app.js read --title="Mi nota"
```

### ❌ Eliminar una nota

```bash
node app.js remove --title="Mi nota"
```

> 💡 Los comandos pueden variar según cómo esté implementado el archivo `app.js`.

---

## 🧠 Ejemplo rápido

```bash
node app.js add --title="Tareas" --body="Lavar ropa y estudiar Node.js"
```

Salida esperada:
```
Nueva nota agregada:
- Título: Tareas
- Contenido: Lavar ropa y estudiar Node.js
```

---

## 📜 Licencia

Este proyecto está bajo la licencia [MIT](https://opensource.org/licenses/MIT).  
Eres libre de usarlo, modificarlo y distribuirlo con fines educativos o personales.

---

## ✨ Autor

Desarrollado con 💚 por **Luis Reyes**.
