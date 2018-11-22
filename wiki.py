import wikipediaapi as wk

lang = wk.Wikipedia('en')

def wksum(content):
    content = content.replace('wiki ', '')
    article = lang.page(content)
    if article.exists() == False:
        return ('Page not found. Is there some typo?')
    return article.canonicalurl
