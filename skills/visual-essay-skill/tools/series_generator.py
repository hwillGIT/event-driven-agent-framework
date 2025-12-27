import yaml
import sys
import os
import shutil

def generate_series(yaml_path):
    with open(yaml_path, 'r') as f:
        spec = yaml.safe_load(f)

    series_title = spec.get('series_title', 'Untitled_Series').replace(' ', '_')
    motif = spec.get('motif', 'Atlas')
    output_dir = os.path.join('out', series_title)
    
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    print(f"Generating series: {series_title} ({len(spec['essays'])} essays) in {output_dir}")

    # Read base prompt template (Stage 1)
    # In a real scenario, this would read the .md file. Here we construct the prompt instructions.
    base_instruction = "You are generating a Visual Essay Blueprint."

    for i, essay in enumerate(spec['essays']):
        title = essay['title']
        concept = essay['concept']
        safe_title = title.replace(' ', '_').replace('/', '-')
        
        filename = f"{i+1:02d}_{safe_title}_operator_prompt.md"
        filepath = os.path.join(output_dir, filename)

        content = f"""# Operator Prompt for Essay {i+1}: {title}

**Series**: {series_title}
**Motif**: {motif}
**Concept**: {concept}

---

## Instructions for the AI
1.  Read the **Stage 1 Blueprint Generator** prompt.
2.  Use the concept above as your INPUT.
3.  Generate a blueprint titled "{title}".
4.  Once the blueprint is generated and approved, apply the **{motif}** motif using the **Stage 2 Renderer**.

"""
        with open(filepath, 'w') as f:
            f.write(content)
        
        print(f"  Created: {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python series_generator.py <path_to_yaml_spec>")
        sys.exit(1)
    
    generate_series(sys.argv[1])
