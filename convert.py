#!/usr/bin/python3
import sys

def remove_quebra_de_linha(linha):
    return linha.replace('\n', '')

# Cria um link HTML com a tag <a> e target blank

def cria_link_html(url):
    clean_url = url.strip()
    return '<a href="{u}" target="_blank">{u}</a>'.format(u = clean_url)


def do_it(input_file,output_file):
    for line in input_file:
        # Se começa com http, é um link
        if line.startswith('http'):
            line = cria_link_html(line)
            output_file.write("<ul>\n")
            output_file.write("\t <li>" + line + "</li>\n")
            output_file.write("</ul>\n")

        # Senão, é um título
        else:
            line = line.strip()
            output_file.write("<h2>" + line + "</h2>\n")


if __name__ == '__main__':
    # Lista exportada diretamente do firefox
    input_file = open(sys.argv[1])
    output_file = open(sys.argv[2],"w+")
    do_it(input_file,output_file)
