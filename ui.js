const btn = document.getElementById("toggle-sidebar");

btn.addEventListener("click", () => {
    document.body.classList.toggle("sidebar-collapsed");
});
