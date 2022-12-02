const codeArea = document.getElementById("code");
codeArea.addEventListener(
  "input",
  function () {
    sessionStorage.setItem("code", codeArea.value);
  },
  false
);

document.addEventListener("DOMContentLoaded", function () {
  codeArea.value = sessionStorage.getItem("code");
});
