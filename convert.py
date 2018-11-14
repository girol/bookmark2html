#!/usr/bin/python3

def remove_quebra_de_linha(linha):
    return linha.replace('\n', '')

# Cria um link HTML com a tag <a> e target blank

def cria_link_html(url):
    clean_url = remove_quebra_de_linha(url)
    return '<a href="{u}">{u}</a>'.format(u = clean_url)


# Lista exportada diretamente do firefox
link_list = open('my_linkx.txt')
the_html = open('my_page.html', 'w+')

for line in link_list:
    # Se começa com http, é um link
    if line.startswith('http'):
        line = cria_link_html(line)
        the_html.write("<ul>\n")
        the_html.write("\t <li>" + line + "</li>\n")
        the_html.write("</ul>\n")

    # Senão, é um título
    else:
        line = remove_quebra_de_linha(line)
        the_html.write("<h2>" + line + "</h2>\n")

