# PDF Pipeline Notes

When converting PDFs to Visual Essays via NotebookLM, follow this workflow:

1.  **Ingest**: Upload PDFs to NotebookLM.
2.  **Filter**: Use the `ingestion_note_template.md` to create a "Raw Note" for each PDF.
3.  **Synthesize**: Ask NotebookLM to combine the Raw Notes using the `instruction_note_master.md`.
4.  **Extract**: Take the "Structure Suggestion" from the output and paste it into the VEG Stage 1 Prompt.
