import nbformat

path = "./ML Report.ipynb"  # your notebook name
nb = nbformat.read(path, as_version=nbformat.NO_CONVERT)

# Safely remove broken widget metadata
if "widgets" in nb["metadata"]:
    del nb["metadata"]["widgets"]

# Save clean version
nbformat.write(nb, path)
print("Cleaned notebook metadata — safe to push to GitHub!")
