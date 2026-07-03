import jinja2
import projects

TEMPLATES_TO_RENDER = [
    "index.html",
    "contribute.html",
    "projects.html",
    "wiki.html",
    "style.css",
    "wjosglogo.svg",
]

TEMPLATE_DIR = 'templates'
RENDER_DIR = 'docs'


class HyperLink:
    def __init__(self, text, link):
        self.text = text
        self.url = link

HYPERLINKS = [
                HyperLink("Home", "/"),
                HyperLink("Projects", "/projects.html"),
                HyperLink("Contribute", "/contribute.html"),
                HyperLink("Wiki", "/wiki.html"),
            ]

'''
Basic script to render out templates into their respective files.
'''
def main():
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))
    for template_name in TEMPLATES_TO_RENDER:
        template = env.get_template(template_name)
        with open(f"{RENDER_DIR}/{template_name}", "w") as fp:
            fp.write(template.render(hyperlinks=HYPERLINKS, projects=projects.PROJECTS))

    return

if __name__ == '__main__':
    main()
