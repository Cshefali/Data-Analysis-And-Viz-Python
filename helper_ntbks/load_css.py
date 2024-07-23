from IPython.core.display import HTML

def load_css(filename):
    with open(filename, 'r') as f:
        css = f.read()
    return HTML(f'<style>{css}</style>')

load_css('styles.css')
