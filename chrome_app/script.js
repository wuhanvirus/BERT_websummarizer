chrome.tabs.executeScript({
    code:'var bodyUrl = document.querySelector("a").innerText;'
},function(result){
    alert(result[0]);
});