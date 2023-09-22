const cardBtn1 = document.querySelector("#card-btn1");
const cardBtn2 = document.querySelector("#card-btn2");
const cardBtn3 = document.querySelector("#card-btn3");
const cardBtn4 = document.querySelector("#card-btn4");
const modal1 = document.querySelector(".di1");
const modal2 = document.querySelector(".di2");
const modal3 = document.querySelector(".di3");
const modal4 = document.querySelector(".di4");
const overlay = document.querySelector(".overlay");


cardBtn1.addEventListener('click', () => {
    openModal(modal1, overlay);
});

cardBtn2.addEventListener('click', () => {
    openModal(modal2, overlay);
});

cardBtn3.addEventListener('click', () => {
    openModal(modal3, overlay);
});

cardBtn4.addEventListener('click', () => {
    openModal(modal4, overlay);
});

overlay.addEventListener('click', () => {
    closeModal(modal1, overlay);
    closeModal(modal2, overlay);
    closeModal(modal3, overlay);
    closeModal(modal4, overlay);
});

function openModal(modal, overlay) {
    modal.classList.remove("hidden");
    overlay.classList.remove("hidden");
}

function closeModal(modal, overlay) {
    modal.classList.add("hidden");
    overlay.classList.add("hidden");
}
