function init() {
  const select = document.querySelector("#category");
  const cardContainer = document.querySelector(".cards-container");

  async function filterByCategeory() {
    const url = `http://127.0.0.1:8000/blog/category/?category=${select.value}`;
    const data = await fetch(url);
    let { template } = await data.json();
    cardContainer.innerHTML = template
  }
  select.addEventListener("change", filterByCategeory);
}
init();
