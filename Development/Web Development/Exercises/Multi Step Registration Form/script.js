const nextButton = document.querySelector(".btn-next");
const prevButton = document.querySelector(".btn-prev");
const steps = document.querySelectorAll(".step");
const form_steps = document.querySelectorAll(".form-step");
let active = 1;

nextButton.addEventListener("click", () => {
  active++;

  if (active > steps.length) {
    active = steps.length;
  }

  updateProgress();
});

prevButton.addEventListener("click", () => {
  active--;

  if (active < 1) {
    active = 1;
  }

  updateProgress();
});

const updateProgress = () => {
  console.log("Steps = " + steps.length);
  console.log("Active = " + active);

  // Toggle .active class for each list items
  steps.forEach((step, i) => {
    if (i == active - 1) {
      step.classList.add("active");
      form_steps[i].classList.add("active");
    } else {
      step.classList.remove("active");
      form_steps[i].classList.remove("active");
    }
  });

  // enable aor disable prev and next button
  if (active === 1) {
    prevButton.disabled = true;
  } else if (active === steps.length) {
    nextButton.disabled = true;
  } else {
    prevButton.disabled = false;
    nextButton.disabled = false;
  }
};
