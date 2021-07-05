window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
    document.getElementById("head").style.fontSize = "35px";
    document.getElementById("imag").style.width = "8%";
    document.getElementById("imag").style.height = "60px";



  } else {
    document.getElementById("head").style.fontSize = "50px";
    document.getElementById("imag").style.width = "15%";
    document.getElementById("imag").style.height = "100px";


  }
};

function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
}

/* Set the width of the side navigation to 0 and the left margin of the page content to 0 */
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
} 
