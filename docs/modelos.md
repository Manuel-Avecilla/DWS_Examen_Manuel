## Modelos del Sistema

---

### Usuario
Representa la cuenta base de todo tipo de usuario en el sistema (participante, jurado o administrador).

**Atributos:**
- `nombre_usuario`: Nombre único de usuario.  
- `correo`: Correo electrónico único.  
- `password`: Contraseña cifrada o en texto (según implementación).  
- `fecha_registro`: Fecha en que el usuario se creó.

**Relaciones:**
- 1:1 con `Perfil` (tiene un perfil).
- Puede recibir muchas `Notificaciones`.

---

[⬅️ Volver al README principal](../README.md)
