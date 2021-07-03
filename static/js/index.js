
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  let content = document.querySelector(".eff");
  let content2 = document.querySelector(".efe");
  let contentPos = content.getBoundingClientRect().top;
  let contentPos2 = content2.getBoundingClientRect().top;
  let screenPos = window.innerHeight;

  if(contentPos < screenPos){
    content.classList.add('active');
  }
  else{
    content.classList.remove('active');

  }
  if(contentPos2 < screenPos){
    content2.classList.add('active');
  }
  else{
    content2.classList.remove('active');

  }
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
