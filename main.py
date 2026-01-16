import jinja2

TEMPLATES_TO_RENDER = [
    "index.html",
    "style.css",
]

'''
Basic script to render out templates into their respective files.
'''
def main():
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
    for template_name in TEMPLATES_TO_RENDER:
        template = env.get_template(template_name)
        with open(f"rendered/{template_name}", "w") as fp:
            fp.write(template.render())

    return

if __name__ == '__main__':
    main()
