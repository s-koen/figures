function loadPage() {

    let hash = window.location.hash;

    if (!hash) {
        return;
    }

    let path = hash.slice(2);

    let iframe = document.getElementById("viewer");

    iframe.src = path + ".html";
}

window.addEventListener("hashchange", loadPage);

loadPage();
