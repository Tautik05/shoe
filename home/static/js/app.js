"use strict";

const wrapper = document.querySelector(".sliderWrapper");
const menuItems = document.querySelectorAll(".menuitem");

menuItems.forEach((item, index) => {
  item.addEventListener("click", () => {
    wrapper.style.transform = `translateX(${-100 * index}vw)`;
    wrapper.style.transition = "transform 1s ease-in-out";
  });
});
