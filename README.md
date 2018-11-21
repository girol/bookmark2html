# bookmark2html

Não conseguia exportar uma pasta de links salva no navegador em uma lista de links para compartilhar com os amigos.

Acho uma tarefa muito simples para se instalar um plugin no navegador, aumentando seu tempo de carga para uma tarefa trivial e nem sempre utilizada.

Esse script resolve esse problema de forma muito simples.

## Como utilizar

Abra o gerenciador de Bookmarks do Firefox, selecione os links que deseja exportar, copie e cole num arquivo texto. Por exemplo, `my_links.txt`.

Rodar:

```bash
./convert.py my_links.txt my_page.html
```

Há um exemplo de um arquivo de exportação neste diretório com o nome `my_links.txt`