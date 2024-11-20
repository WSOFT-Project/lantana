# Lantana Link OpenNewTab拡張機能
# この拡張機能は外部サイトへのリンクを新しいタブで開きます
from markdown import Extension
from markdown.postprocessors import Postprocessor
from bs4 import BeautifulSoup
from urllib.parse import urlparse

openNewTabRules = []
openNewTabIgnoreRules = []

class OpenNewTabRule:
    def __init__(self, rule_dict):
        self.base_url = urlparse(rule_dict['base_url'])
        if 'subdomain_depth' in rule_dict:
            self.subdomain_depth = rule_dict['subdomain_depth']
        if 'path_depth' in rule_dict:
            self.path_depth = rule_dict['path_depth']
        if 'class_name' in rule_dict:
            self.className = rule_dict['class_name']
        if 'id' in rule_dict:
            self.id = rule_dict['id']
    base_url = None
    subdomain_depth = 0
    path_depth = -1
    className = None
    id = None

def GetRules(rules):
    rule_list = []
    for rule in rules:
        if 'base_url':
            rule_list.append(OpenNewTabRule(rule))
    return rule_list

class OpenNewTabExtension(Extension):
    def __init__(self, *args, **kwargs):
        self.config = {
            'rules': [[], 'Rules for OpenNewTab'],
            'ignore_rules': [[], 'IgnoreRules for OpenNewTab']
        }
        super().__init__(*args, **kwargs)
    def extendMarkdown(self, md, md_globals):
        global openNewTabRules
        global openNewTabIgnoreRules
        openNewTabRules = GetRules(self.getConfig('rules'))
        openNewTabIgnoreRules = GetRules(self.getConfig('ignore_rules'))
        md.postprocessors.add('link_opennewtab', OpenNewTabPostprocesser(self), '>raw_html')


class OpenNewTabPostprocesser(Postprocessor):
    def run(self, html):
        return editRawHtml(html)

def editRawHtml(html):
    soup = BeautifulSoup(html, 'html.parser')
    global openNewTabRules
    global openNewTabIgnoreRules
    for tag in soup.select('a[href*="://"]:not(.unnewtab)'):
        linked_url = urlparse(tag.attrs["href"])
        cond = True
        for rule in openNewTabIgnoreRules:
            if not checkMatch(linked_url, rule, tag):
                cond = False
                break
        for rule in openNewTabRules:
            if not checkMatch(linked_url, rule, tag):
                cond = True
                break
        if cond:
            tag.attrs["target"] = ['_blank']
            tag.attrs["rel"] = ['noopener" ,"noreferrer']
    return str(soup)

def makeExtension(*args, **kwargs):
    return OpenNewTabExtension(*args, **kwargs)

def checkMatch(target, rule: OpenNewTabRule, tag: BeautifulSoup):
    # クラス名、idの判定
    if rule.className and rule.className not in tag['class']:
        return True
    if rule.id and rule.id != tag['id']:
        return True
    # ホスト名の判定
    if rule.base_url.hostname != target.hostname and rule.subdomain_depth != -1:
        if rule.subdomain_depth == 0:
            return True
        # IPアドレスの場合は判定から弾く
        if rule.base_url.hostname.replace('.', '').isdigit() and target.hostname.replace('.', '').isdigit():
            return True
        else:
            base_domains = rule.base_url.hostname.split('.')
            target_domains = target.hostname.split('.')
            if len(base_domains) < rule.subdomain_depth + 1 or len(target_domains) < rule.subdomain_depth + 1:
                return True
            for i in range(rule.subdomain_depth + 1):
                if base_domains[-i-1] != target_domains[-i-1]:
                    return True
    # パスの判定
    if rule.base_url.path != target.path and rule.path_depth != -1:
        if rule.path_depth == 0:
            return True
        base_dirs = rule.base_url.path.split('/')
        target_dirs = target.path.split('/')
        if len(base_dirs) < rule.path_depth or len(target_dirs) < rule.path_depth:
            return True
        for i in range(rule.path_depth):
            if base_dirs[i] != target_dirs[i]:
                return True
    return False
