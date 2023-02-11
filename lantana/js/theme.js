//Materialテーマ相互運用機能

//印刷用ページの設定
function isPrintMode(){
    var i = new URL(window.location.href);
    var pms = i.searchParams;
    return pms.has('embed');
}

function togglePrintMode(){
if(isPrintMode()) {
    document.querySelectorAll('.print-hide').forEach(element =>element.parentNode.removeChild(element));
    document.querySelectorAll('.print-visible').forEach(element =>element.classList.remove('d-none'));
    document.querySelector('.print-main').classList.remove('col-md-8');
}}

function linkToNewTab(url){
document.querySelectorAll('a[href*="://"]:not([href*="'+url+'"]):not(.unnewtab)').forEach(element =>element.setAttribute('target','_blank'));
}

function afterload(){
document.querySelectorAll('a[target="_blank"]').forEach(element =>element.setAttribute('rel','noopener noreferrer'));
}

togglePrintMode();

function print_view(){
    var url = new URL(window.location.href);
	url.searchParams.append('embed','');
	window.open(url);
}

function print_normal(){
    var url = new URL(window.location.href);
	url.searchParams.delete('embed');
	window.open(url);
}

function share_to_facebook(){
    location.href='http://www.facebook.com/share.php?u='+encodeURI(location.href);
}
function share_to_twitter(text){
    location.href='https://twiter.com/share?url='+encodeURI(location.href)+"&text="+encodeURI(text);
}

//該当するクラスを置換するメソッド
function replace_class(base,to){
    document.querySelectorAll('.'+base).forEach(element => element.classList.replace(base,to));
}
function add_class(base,to){
    document.querySelectorAll('.'+base).forEach(element => element.classList.add(to));
}

//MaterialのAdmonitionをAlertに置換
replace_class('admonition','alert');
replace_class('admonition-title','alert-heading');
$(".alert a").addClass("alert-link");

//MaterialのAdmonition色をAlert色に置換
add_class('note','alert-primary');
add_class('abstract','alert-secondary');
add_class('info','alert-info');
add_class('tip','alert-warning');
add_class('success','alert-success');
add_class('question','alert-secondary');
add_class('warning','alert-warning');
add_class('failure','alert-danger');
add_class('danger','alert-danger');
add_class('bug','alert-warning');
add_class('example','alert-dark');
add_class('quote','alert-light');

//コードブロックのコピーアイコンの定義
const ICON_COPY = 'bi-clipboard';
const ICON_COPY_CHECK = 'bi-clipboard-check';

//コードブロックにコピーボタンを追加
$(".highlight").addClass("position-relative");
$(".highlight").prepend('<button onclick="copy_btn_clicked(this)" class="btn copybtn position-absolute top-0 end-0"><i class="bi '+ICON_COPY+'"></i></button>');

//コードブロックのコピーボタンが押されたときの処理
function copy_btn_clicked(btn){
    const selection = window.getSelection();
    const code = btn.parentNode;
    selection.selectAllChildren(code.children[code.children.length-1]);
    document.execCommand('copy');
    btn.querySelector('.'+ICON_COPY).classList.add('text-success');
    btn.querySelector('.'+ICON_COPY).classList.replace(ICON_COPY,ICON_COPY_CHECK);
}

//ページのコピーボタンが押されたときの処理
function page_copy_btn_clicked(btn){
    $(document.body).append("<textarea id=\"copyTarget\" style=\"position:absolute; left:-9999px; top:0px;\" readonly=\"readonly\">" +location.href+ "</textarea>");
  let obj = document.getElementById("copyTarget");
  let range = document.createRange();
  range.selectNode(obj);
  window.getSelection().addRange(range);
  document.execCommand('copy');
    btn.querySelector('.'+ICON_COPY).classList.add('text-success');
    btn.querySelector('.'+ICON_COPY).classList.replace(ICON_COPY,ICON_COPY_CHECK);
}

//表をBootstrap仕様に
$("table").addClass("table");

//引用をBootstrap仕様に
$("blockquote").addClass("blockquote");

//画像をBootstrap仕様に
$("img").addClass("img-fluid");


//
$('.btn-outline-secondary .switch').on('click', function() {
    this.replace_class('btn-outline-secondary','btn-secondary');
  });

$('.btn-secondary .switch').on('click', function() {
    this.replace_class('btn-secondary','btn-outline-secondary');
  });


let toggle_state_nav =   false;
let toggle_state_toc =   false;

function toggle_nav(nav){
    toggle_state_nav = !toggle_state_nav;
    if(toggle_state_nav){
        nav.classList.replace('btn-outline-secondary','btn-secondary');
    }else{
        nav.classList.replace('btn-secondary','btn-outline-secondary');
    }
}
function toggle_toc(toc){
    toggle_state_toc = !toggle_state_toc;
    if(toggle_state_toc){
        toc.classList.replace('btn-outline-secondary','btn-secondary');
    }else{
        toc.classList.replace('btn-secondary','btn-outline-secondary');
    }
}

function search(ismobile){
    let query=document.getElementById('searchbox').value;
    if(ismobile){
        query=document.getElementById('searchbox_mobile').value;
    }
    let target = document.getElementById('mkdocs-search-query');
    target.value=query;
    let e = new Event('keyup');
    target.dispatchEvent(e);
    let searchModal = new bootstrap.Modal(document.getElementById('searchModal'), {
        keyboard: false
      });
    searchModal.show();
}

let url = new URL(window.location.href);
let params = url.searchParams;

var get_query = params.get('q');

document.getElementById('searchbox').value=get_query;
document.getElementById('searchbox_mobile').value=get_query;

$('.nav_cop').click(function() {
    $(this).next().collapse('toggle');
});

/*!
 * Color mode toggler for Bootstrap's docs (https://getbootstrap.com/)
 * Copyright 2011-2023 The Bootstrap Authors
 * Licensed under the Creative Commons Attribution 3.0 Unported License.
 */

(() => {
    'use strict'
  
    const storedTheme = localStorage.getItem('theme')
  
    const getPreferredTheme = () => {
      if (storedTheme) {
        return storedTheme
      }
  
      return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
    }
  
    const setTheme = function (theme) {
      if (theme === 'auto' && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.documentElement.setAttribute('data-bs-theme', 'dark')
      } else {
        document.documentElement.setAttribute('data-bs-theme', theme)
      }
    }
  
    setTheme(getPreferredTheme())
  
    const showActiveTheme = theme => {
      const themeSwitcher = document.querySelector('#bd-theme')
      const themeSwitcherText = document.querySelector('#bd-theme-text')
      const activeThemeIcon = document.querySelector('.theme-icon-active use')
      const btnToActive = document.querySelector(`[data-bs-theme-value="${theme}"]`)
      const svgOfActiveBtn = btnToActive.querySelector('svg use').getAttribute('href')
  
      document.querySelectorAll('[data-bs-theme-value]').forEach(element => {
        element.classList.remove('active')
        element.setAttribute('aria-pressed', 'false')
      })
  
      btnToActive.classList.add('active')
      btnToActive.setAttribute('aria-pressed', 'true')
      activeThemeIcon.setAttribute('href', svgOfActiveBtn)
      const themeSwitcherLabel = `${themeSwitcherText.textContent} (${btnToActive.dataset.bsThemeValue})`
      themeSwitcher.setAttribute('aria-label', themeSwitcherLabel)
      themeSwitcher.focus()
    }
  
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
      if (storedTheme !== 'light' || storedTheme !== 'dark') {
        setTheme(getPreferredTheme())
      }
    })
  
    window.addEventListener('DOMContentLoaded', () => {
      showActiveTheme(getPreferredTheme())
  
      document.querySelectorAll('[data-bs-theme-value]')
        .forEach(toggle => {
          toggle.addEventListener('click', () => {
            const theme = toggle.getAttribute('data-bs-theme-value')
            localStorage.setItem('theme', theme)
            setTheme(theme)
            showActiveTheme(theme)
          })
        })
    })
  })()