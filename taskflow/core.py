    def agregar(self, titulo, prioridad="media"):
        titulo = titulo.strip()
        if not titulo:
            raise ValueError("El título no puede estar vacío")
        if prioridad not in PRIORIDADES:
            raise ValueError(f"Prioridad inválida: {prioridad}")
        if any(t.titulo.lower() == titulo.lower() for t in self._tareas):   # TF-11
            raise ValueError(f"Ya existe una tarea llamada '{titulo}'")
        tarea = Tarea(self._siguiente_id, titulo, prioridad)
        self._tareas.append(tarea)
        self._siguiente_id += 1
        return tarea

    def filtrar_por_prioridad(self, prioridad):                            # TF-8
        if prioridad not in PRIORIDADES:
            raise ValueError(f"Prioridad inválida: {prioridad}")
        return [t for t in self._tareas if t.prioridad == prioridad]

    def buscar_texto(self, texto):                                         # TF-9
        texto = texto.strip().lower()
        if not texto:
            raise ValueError("El texto de búsqueda no puede estar vacío")
        return [t for t in self._tareas if texto in t.titulo.lower()]

    def resumen(self):                                                     # TF-10
        total = len(self._tareas)
        completadas = sum(1 for t in self._tareas if t.completada)
        avance = round(completadas * 100 / total) if total else 0
        return {
            "total": total,
            "completadas": completadas,
            "pendientes": total - completadas,
            "avance": avance,
        }