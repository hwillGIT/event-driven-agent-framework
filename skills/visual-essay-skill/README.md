# Visual Essay Skill (VEG v1.0)

This repository module contains the complete toolset for the Visual Essay Generator (VEG). It is designed to transform abstract concepts or raw notes into high-quality, visually structured essays suitable for posting on social media, blogs, or internal knowledge bases.

## Overview

The VEG workflow consists of two main stages, guided by specific prompts and templates:

1.  **Stage 1: Blueprint Generation**: Converts raw ideas, notes, or a topic into a structured "Blueprint". This blueprint defines the core thesis, narrative arc, and exactly what text and visuals go where.
2.  **Stage 2: Rendering**: Takes the Blueprint and a specific "Motif" (visual style) to generate the final output (e.g., Midjourney prompts + final copy).

## Directory Structure

*   `skill/`: Core documentation and prompt templates.
    *   `prompts/`: The actual prompts for Stage 1, Stage 2, and Operator Mode.
    *   `motifs/`: Definitions of visual styles (Atlas, Mythic, Systems, etc.).
    *   `notebooklm/`: Templates for ingesting content into NotebookLM for research.
    *   `citation/`: Standards for handling citations and sources.
*   `examples/`: Sample data.
    *   `blueprints/`: Reference blueprints for different essay types.
    *   `series/`: JSON configurations for generating entire series of essays.
*   `tools/`: Python scripts to automate the workflow.
    *   `series_generator.py`: Generates prompt files from a JSON series spec.
    *   `blueprint_linter.py`: Validates blueprints against strict formatting rules.
    *   `doctor.py`: Checks the health of the skill installation.
*   `schemas/`: JSON schemas for validating blueprints and series specs.

## Quickstart

### Prerequisites

*   Python 3.8+

### Generating a Series

1.  Edit `examples/series/series_ai_augmentation_atlas.json` or create your own.
2.  Run the generator:
    ```bash
    python tools/series_generator.py examples/series/series_ai_augmentation_atlas.json
    ```
3.  Find your generated prompts in `out/<Series_Title>/`.

### Validating a Blueprint

Ensure your blueprint follows the "LOCKED" block strictures:

```bash
python tools/blueprint_linter.py examples/blueprints/example_academic_writing_vs.blueprint.md
```

## Spelling & Integrity Guardrails

To ensure text integrity, we use **Canonical Text Blocks (LOCKED)**.
*   In the Blueprint, text designated for the final image is marked as `(LOCKED)`.
*   The Stage 2 Renderer is strictly instructed to copy this text verbatim.
