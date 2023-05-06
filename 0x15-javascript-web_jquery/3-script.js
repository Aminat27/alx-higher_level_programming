const header = document.querySelector('header');
const redHeader = document.querySelector('#red_header');
redHeader.onclick = () => {
  header.classList.add('red');
};
