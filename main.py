import jinja2

TEMPLATES_TO_RENDER = [
    "index.html",
    "style.css",
]

TEMPLATE_DIR = 'templates'
RENDER_DIR = 'docs'

'''
Basic script to render out templates into their respective files.
'''
def main():
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))
    for template_name in TEMPLATES_TO_RENDER:
        template = env.get_template(template_name)
        with open(f"{RENDER_DIR}/{template_name}", "w") as fp:
            fp.write(template.render())

    return

if __name__ == '__main__':
    main()
