#!/usr/bin/python3
import sys
from model.Bookmark import Bookmark
from model.BookmarkGroup import BookmarkGroup


def create_model(input_stream):
    root = BookmarkGroup("Bookmarks")
    active_group = root

    for line in input_stream:
        value = line.strip()
        # Se começa com http, é um link
        if value.startswith('http'):
            bookmark = Bookmark(value)
            active_group.bookmarks.append(bookmark)
        # Senão, é um título
        else:
            print(active_group.name)
            active_group = BookmarkGroup(value)
            root.subgroups.append(active_group)

    return root


def serialize_as_html(model,output_stream):
    
    def inner_serialize_bookmark(bookmark,output_stream):
        output_stream.write("<li><a href={url}>{url}</a></li>\n".format(url=bookmark.url))

    def inner_serialize_bookmark_list(bookmark_list, output_stream):
        if bookmark_list:
            output_stream.write("<ul>\n")
            for bookmark in bookmark_list:
                inner_serialize_bookmark(bookmark,output_stream)
            output_stream.write("</ul>\n")

    def format_header(name,level):
       return "<h{level!s}>{name}</h{level!s}>".format(name=name,level=level)

    def inner_serialize_group(group,output_stream,level):
        header = format_header(group.name,level)
        output_stream.write("{}\n".format(header))
        inner_serialize_bookmark_list(group.bookmarks, output_stream)
        for g in group.subgroups:
            inner_serialize_group(g,output_stream,level+1)
    

    def inner_serialize_as_html(model,output_stream,level=1):
        if isinstance(model,Bookmark):
            inner_serialize_bookmark(model_output_stream)
        elif isinstance(model,BookmarkGroup):
            inner_serialize_group(model,output_stream,level)
        else:
            raise Exception("Unknow class model.")

    inner_serialize_as_html(model,output_stream)


if __name__ == "__main__":
    input_stream = open(sys.argv[1])
    output_stream = open(sys.argv[2],"w")
    model = create_model(input_stream)
    serialize_as_html(model,output_stream)
