# TaskFlow


Gestor de tareas en Python · Proyecto integrador DevOps & Project Management.
Sitio: https://USUARIO.github.io/taskflow/ · Jira: https://SITIO.atlassian.net (proyecto TF)

## Equipo
## Funcionalidades (con la clave de Jira de cada una)
## Cómo ejecutarlo y probarlo
## Flujo de trabajo
- Estrategia: GitHub Flow · merge: squash · main protegida (ruleset)
- Convenciones: ramas `tipo/TF-n-descripcion`, Conventional Commits, PRs con plantilla
## CI/CD
- ci.yml: pruebas en Python 3.11–3.13 en cada PR
- deploy.yml: pruebas + publicación en Pages en cada merge a main
## Gestión ágil
- Épicas, Sprint Goal, velocity (Sprint 0 y Sprint 1), enlace al burndown
## Evidencias
- Lista de PRs (enlaces) · capturas en docs/evidencias/
## Retrospectiva del Sprint 1
| Mantener | Mejorar | Acción (clave Jira) |
|----------|---------|---------------------|
|          |         |                     |
## Lecciones aprendidas

```bash
python -m venv .venv
source .venv/bin/activate        # Windows (Git Bash): source .venv/Scripts/activate
pip install -r requirements.txt
python -m taskflow
python -m pytest -v
```

## Avance del proyecto
- [x] Hito 1 — Repositorio, código base y pruebas locales
- [ ] Hito 2 — GitHub Flow, CI/CD y GitHub Pages
- [ ] Hito 3 — Jira, sprint e integración con GitHub

## Evidencias
<<<<<<< Updated upstream
(Se completa en cada hito: enlaces a PRs, workflows, sitio publicado y Jira.)
=======
(Se completa en cada hito: enlaces a PRs, workflows, sitio publicado y Jira.)
>>>>>>> Stashed changes
[![CI](https://github.com/irvingurbano-sys/taskflow/actions/workflows/ci.yml/badge.svg)](https://github.com/irvingurbano-sys/taskflow/actions/workflows/ci.yml)

