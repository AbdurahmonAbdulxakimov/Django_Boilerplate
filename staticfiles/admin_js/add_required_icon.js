$(document).ready(function () {
    if (window.location.pathname.includes("admin/news/article") && document.getElementById("article_form")) {
        document.querySelector('label[for="id_author"]').innerHTML += "<span class='text-red'>*</span>";
    } else if (window.location.pathname.includes("admin/news/specialreports") && document.getElementById("specialreports_form")) {
        document.querySelector('label[for="id_author"]').innerHTML += "<span class='text-red'>*</span>";
    }
});
