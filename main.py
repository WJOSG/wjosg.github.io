import jinja2

TEMPLATES_TO_RENDER = [
    "index.html",
    "contribute.html",
    "style.css",
    "wjosglogo.svg",
]

TEMPLATE_DIR = 'templates'
RENDER_DIR = 'docs'

class HyperLink:
    def __init__(self, text, link):
        self.text = text
        self.url = link

'''
Basic script to render out templates into their respective files.
'''
def main():
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))
    for template_name in TEMPLATES_TO_RENDER:
        template = env.get_template(template_name)
        with open(f"{RENDER_DIR}/{template_name}", "w") as fp:
            fp.write(template.render(hyperlinks=[
                HyperLink("Home", "/"),
                HyperLink("Projects", "/"),
                HyperLink("Contribute", "/contribute.html"),
            ]))

    return

if __name__ == '__main__':
    main()
