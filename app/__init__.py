#Al colocar init en la carpeta, el directorio se transforma en un modulo. Si ponemos luego import app, nos importara todo el código que haya en este directorio.

from flask import Flask

app =Flask(__name__)

from app import routes