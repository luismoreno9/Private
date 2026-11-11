#!/usr/bin/env bash
# Une los documentos de SERIE IA en un solo archivo para subirlo como conocimiento del Proyecto de Claude.
# Uso: bash serie-ia/proyecto-claude/generar-conocimiento.sh
set -euo pipefail
cd "$(dirname "$0")/.."
out="proyecto-claude/SERIE-IA-conocimiento.md"
{
  echo "# SERIE IA: conocimiento del proyecto"
  echo
  echo "_Generado a partir del repo. Actualizado: $(date +%Y-%m-%d). Para editarlo, cambia los documentos originales y vuelve a ejecutar el script._"
  for f in README.md 01-plan-maestro.md 02-biblia.md 03-pipeline.md 04-interaccion.md \
           plantillas/ficha-personaje.md plantillas/guion-episodio.md plantillas/shot-list.md \
           episodios/README.md; do
    echo
    echo "---"
    echo
    echo "<!-- archivo: serie-ia/$f -->"
    echo
    cat "$f"
  done
} > "$out"
echo "Generado: serie-ia/$out ($(wc -w < "$out") palabras)"
