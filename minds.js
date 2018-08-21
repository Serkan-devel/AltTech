// ==UserScript==
// @name         Minds Show Impressions
// @namespace    http://www.minds.com/
// @version      0.8
// @description  Shows the number of impressions/views on a post.
// @author       You
// @match        https://www.minds.com/*
// @grant        none
// @require      https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js
// ==/UserScript==
function getCookie(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length == 2) {
        return parts.pop().split(";").shift();
    }
}
function http(method, url, payload, callback) {
    $.ajax({
        method: method,
        url: url,
        headers: { 'x-xsrf-token': getCookie('XSRF-TOKEN') }
    }).done(function(ret) { callback(ret); });
}
function getImpressions(id, callback) {
    http('GET', 'https://www.minds.com/api/v1/newsfeed/single/'+ id, '', function(ret) {callback(ret.activity.impressions)});
}
var hash = []
function updateViews() {
    var pl = document.getElementsByClassName('permalink');
    for(var i = 0; i < pl.length; i++) {
        if (hash.indexOf(pl[i]) != -1) {
            continue;
        }
        hash.push(pl[i]);
        var ff = function(el) {
            return function(views) {
                el.childNodes[0].innerHTML += `<br>${views} views<br>`;
            };
        }
        var match = /\/([^\/]*)$/.exec(pl[i].href);
        if (match != null) {
            var id = match[1];
            getImpressions(id, ff(pl[i]));
        }
    }
}
var callback = function(mutationsList) {
    mutationsList.forEach((mutation) => {
        if (mutation.type == 'childList') {
            updateViews();
        }
    });
};
var observer = new MutationObserver(callback);
observer.observe(document.body, { childList: true, subtree: true });
