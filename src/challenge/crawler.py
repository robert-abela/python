import re, os
from urllib.request import urlopen

MAX_DEPTH = 10
BASE_URL = 'http://www.mcast.edu.mt'

TRC_LVL_ERR = 1
TRC_LVL_INF = 2
TRC_LVL_DBG = 3
TRC_LVL = TRC_LVL_DBG

def record_entry(depth, msg, file, trace=TRC_LVL_INF):
    if trace <= TRC_LVL:
        msg = '{} [{!s}] {}'.format(' ' * (depth*4), depth, msg)
        print(msg)
        file.write(msg+os.linesep)

def add_base(depth, link, file):
    fixed_link = BASE_URL+link
    record_entry(depth, '> Expanded: ' + link + ' > '+fixed_link, file, TRC_LVL_DBG)
    return fixed_link

def start_crawl():
    file = open('links.txt','wt')
    ALL_LINKS.add(BASE_URL)
    record_entry(0, '+ '+BASE_URL, file)
    crawl(1, BASE_URL, file)
    file.close()
    
def crawl(depth, url, file):
    try:
        html = urlopen(url).read().decode('utf-8')
        all_links = re.findall('''href=["'](.[^"']+)["']''', html, re.I)
        for link in all_links:
            if link.startswith('javascript:') or link.startswith('mailto:'):
                record_entry(depth, '> Skipping: ' + link, file, TRC_LVL_DBG)
            else:
                if link.startswith('/'):    #Fix relative paths
                    link = add_base(depth, link, file)
                if link not in ALL_LINKS:
                    record_entry(depth, '+ '+link, file)
                    ALL_LINKS.add(link)
                    if (depth < MAX_DEPTH) and link.startswith(BASE_URL):
                        crawl(depth+1, link, file)
                else:
                    record_entry(depth, '> Duplicate: ' + link, file, TRC_LVL_DBG)
    except UnicodeDecodeError:
        record_entry(depth-1, '> Cannot parse: ' + url, file, TRC_LVL_ERR)
    except:
        record_entry(depth-1, '> Failed URL: ' + url, file, TRC_LVL_ERR)
        ALL_ERRORS.add(url)
  
ALL_LINKS = set()
ALL_ERRORS = set()
start_crawl()
print(len(ALL_LINKS), 'unique links found')
print(len(ALL_ERRORS), 'errors encountered')

# def fix_link(depth, url, link, file):
#     if url.rfind('/') > 6:
#         url = url[0:url.rfind('/')] 
#     fixed_link = url+link
#     record_entry(depth, '> Fixed: ' + link + ' > '+fixed_link, file, TRACE_LEVEL_WRN)
#     return fixed_link