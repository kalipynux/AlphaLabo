document.querySelector(".jsFilter").addEventListener("click", function () {
  document.querySelector(".filter-menu").classList.toggle("active");
});

document.querySelector(".grid").addEventListener("click", function () {
  document.querySelector(".list").classList.remove("active");
  document.querySelector(".grid").classList.add("active");
  document.querySelector(".products-area-wrapper").classList.add("gridView");
  document
    .querySelector(".products-area-wrapper")
    .classList.remove("tableView");
});

document.querySelector(".list").addEventListener("click", function () {
  document.querySelector(".list").classList.add("active");
  document.querySelector(".grid").classList.remove("active");
  document.querySelector(".products-area-wrapper").classList.remove("gridView");
  document.querySelector(".products-area-wrapper").classList.add("tableView");
});

var modeSwitch = document.querySelector('.mode-switch');
modeSwitch.addEventListener('click', function () {                      document.documentElement.classList.toggle('light');
 modeSwitch.classList.toggle('active');
});

    // Toggle Dark/Light Theme
    const toggleThemeButton = document.getElementById('toggleTheme');
    const body = document.body;

    toggleThemeButton.addEventListener('click', () => {
        body.classList.toggle('dark-mode');
        toggleThemeButton.innerHTML = body.classList.contains('dark-mode') ?
            '<i class="fas fa-sun"></i> Thème Clair' : '<i class="fas fa-moon"></i> Thème Sombre';
    });

    // Toggle Grid/Table Mode
    const toggleGridButton = document.getElementById('toggleGrid');
    const productsArea = document.getElementById('productsArea');

    toggleGridButton.addEventListener('click', () => {
        productsArea.classList.toggle('grid-mode');
    });

    // Search Functionality
    const searchInput = document.getElementById('searchInput');
    const analyseRows = document.querySelectorAll('.products-row');
    const errorMessage = document.getElementById('errorMessage');

    searchInput.addEventListener('input', function () {
        const searchTerm = this.value.toLowerCase();
        let found = false;

        analyseRows.forEach(row => {
            const text = row.textContent.toLowerCase();
            if (text.includes(searchTerm)) {
                row.style.display = 'flex';
                found = true;
            } else {
                row.style.display = 'none';
            }
        });

        if (found) {
            errorMessage.style.display = 'none';
        } else {
            errorMessage.style.display = 'block';
        }
    });