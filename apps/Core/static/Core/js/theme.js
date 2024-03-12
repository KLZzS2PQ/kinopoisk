const btnDarkTheme = document.querySelector('.btn-dark-theme')
const btnWhiteTheme = document.querySelector('.btn-white-theme')
const body = document.querySelector('body')
const btnTheme = document.querySelector('.btn-theme')
let currentTheme = true
btnTheme.addEventListener('click', toggleTheme)

function toggleTheme() {
    btnDarkTheme.style.opacity = currentTheme ? '0' : '100%'
    btnWhiteTheme.style.opacity = currentTheme ? '100%' : '0'
    localStorage.setItem('theme', currentTheme ? 'light' : 'dark')
    body.setAttribute('data-bs-theme', currentTheme ? 'light' : 'dark')
    currentTheme = !currentTheme
}

const localTheme = localStorage.getItem('theme')
if (localTheme === 'light') {
    toggleTheme()
}
