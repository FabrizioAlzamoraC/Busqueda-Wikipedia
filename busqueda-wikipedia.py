#pip install wikipedia-api
import wikipediaapi
import msvcrt

wiki = wikipediaapi.Wikipedia(
    language='es',
    extract_format=wikipediaapi.ExtractFormat.WIKI,
    user_agent='YourUserAgent/1.0'
)

pagina = input('Ingrese búsqueda:\n ')
page_py = wiki.page(pagina)

if page_py.exists():
    print("Resultado de búsqueda: %s" % page_py.summary)
else:
    print("La página no existe")

msvcrt.getch()