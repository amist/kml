from bs4 import BeautifulSoup       # pip install BeautifulSoup4

def _print(str):
    try:
        print(str)
    except UnicodeEncodeError as e:
        print('error')

        
def get_coordinates(soup):
    path = []
    for p in soup.findAll('Placemark'):
        for c in p.findAll('coordinates'):
            path.append(c.get_text())
    return '\n'.join(path)
    
    
def add_path(soup):
    path = get_coordinates(soup)
    
    tag = soup.new_tag('Placemark')
    tag.append(soup.new_tag('styleUrl'))
    tag.styleUrl.append('#my_path_line')
    tag.append(soup.new_tag('LineString'))
    tag.LineString.append(soup.new_tag('coordinates'))
    tag.LineString.coordinates.append(path)
    
    soup.Document.append(tag)
    with open('output.kml', 'wb') as f:
        f.write(soup.encode('utf-8'))
        
def add_path_style(soup):
    tag = soup.new_tag('Style')
    tag['id'] = 'my_path_line'
    tag.append(soup.new_tag('LineStyle'))
    tag.LineStyle.append(soup.new_tag('color'))
    tag.LineStyle.color.append('ffffff00')
    tag.LineStyle.append(soup.new_tag('width'))
    tag.LineStyle.width.append('3')
    soup.Document.append(tag)
    
            
if __name__ == '__main__':
    f = open("t1.kml", "r", encoding='utf-8')
    data = f.read()

    # 'xml' parameters for case sensitivity. Needs lxml to be installed
    soup = BeautifulSoup(data, 'xml')
    
    add_path_style(soup)
    add_path(soup)
    
    
    
    
    