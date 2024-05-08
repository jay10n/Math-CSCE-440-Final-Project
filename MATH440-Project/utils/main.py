import nbformat

# Load the Jupyter Notebook
notebook_path = 'russian_loss_com/Claimed vs documented russian.ipynb'
with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)


# Function to extract and print all the cells' content
def extract_cells(notebook):
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            print('Code Cell:')
            print(''.join(cell['source']))
        elif cell['cell_type'] == 'markdown':
            print('Markdown Cell:')
            print(''.join(cell['source']))
        print('----------------------------------------')


# Execute the function
extract_cells(nb)

#%%
