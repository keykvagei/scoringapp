function setRate(rate, event) {
  let element = event.target.parentNode.parentNode.parentNode;
  let rateParam = element.children[1].children[0];
  if (element.children.length == 4) rateParam = element.children[3].children[0];
  if (document.getElementById('rateParam'))rateParam = document.getElementById('rateParam');
  if (rateParam.getAttribute("isSet") == 1) return;
  rateParam.innerHTML = rate + " /5";
}
let rateCards = document.getElementsByClassName("rateCard");
let postCards = document.getElementsByClassName("postCard");
let postExtends = document.getElementsByClassName("post-extend");
let leftSide = document.getElementById("leftSide");
let rightSide = document.getElementById("rightSide");
let isLeftExtend = false;
let isRightExtend = true;

function extendLeft() {
  if (isLeftExtend) return;

  for (let index = 0; index < rateCards.length; index++) {
    let element = rateCards[index];
    element.style.width = "95%";
    element.children[0].children[0].classList.add("col-3");
    element.children[0].children[1].classList.add("col-9");
    let name = element.children[0].children[1].children[0].children[0];
    name.innerHTML = name.innerHTML.replace("Rate", "");
    let rateDiv = document.createElement("div");
    rateDiv.classList = "col-4 d-flex align-items-center";
    let rate = document.createElement("p");
    rate.style =
      "font-size: 25px;font-family: Poppins Light;font-weight: bold;";
    rate.classList = "mb-4";
    rate.setAttribute("isSet", 0);
    rate.innerHTML = "0 / 5";
    rateDiv.append(rate);
    element.children[0].children[1].children[1].append(rateDiv);
    element.children[0].children[1].children[1].children[0].classList = "col-8";
    let description = document.createElement("p");
    description.style =
      "font-size: 17px;font-family: Poppins Light;margin-bottom: 0 !important;text-align: center !important;font-weight: bold; margin-top : 10px";
    description.innerHTML =
      "Lorem ipsum dolor sit amet consectetur adipisicing elit.Cupiditate, eum.";
    element.children[0].children[1].children[0].append(description);
    element.children[0].children[0].children[0].style.marginTop = "0px";
    element.children[0].children[0].children[0].style.marginLeft = "10px";
    isRightExtend = false;
    isLeftExtend = true;
  }
  for (let index = 0; index < postCards.length; index++) {
    let element = postCards[index];
    element.style.width = "100%";
    element.style.maxWidth = "400px";
    element.children[0].children[1].style.display = "none";
    //  postCards[index].style.transition = "all 1s ease-out";
  }

  leftSide.classList.replace("col-4", "col-7");
  rightSide.classList.replace("col-8", "col-5");
}

function extendRight() {
  if (isRightExtend) return;
  for (let index = 0; index < rateCards.length; index++) {
    let element = rateCards[index];
    element.style.width = "90%";
    element.children[0].children[0].classList.remove("col-3");
    element.children[0].children[1].classList.remove("col-9");
    let name = element.children[0].children[1].children[0].children[0];
    name.innerHTML = "Rate" + name.innerHTML;
    element.children[0].children[1].children[1].children[1].remove();
    element.children[0].children[1].children[1].children[0].classList.remove(
      "col-8"
    );
    element.children[0].children[1].children[0].children[1].remove();
    element.children[0].children[0].children[0].style.marginTop = "20px";
    element.children[0].children[0].children[0].style.marginLeft = "0px";
  }
  for (let index = 0; index < postCards.length; index++) {
    let element = postCards[index];

    element.style.width = "90%";
    element.style.maxWidth = "100%";
    element.children[0].children[1].style.display = "";
    //  postCards[index].style.transition = "all 1s ease-out";
    //  postCards[index].style.transition = "all 4s ease-in";
  }
  leftSide.classList.replace("col-7", "col-4");
  rightSide.classList.replace("col-5", "col-8");
  isRightExtend = true;
  isLeftExtend = false;
}
function sendRate(rate, post, targetID, event) {
  let element = event.target.parentNode.parentNode.parentNode;
  let rateParam = element.children[1].children[0];
  if (element.children.length == 4) rateParam = element.children[3].children[0];
  if (document.getElementById('rateParam'))rateParam = document.getElementById('rateParam');

  let s1 = event.target.parentNode.children[4];
  let s2 = event.target.parentNode.children[3];
  let s3 = event.target.parentNode.children[2];
  let s4 = event.target.parentNode.children[1];
  let s5 = event.target.parentNode.children[0];

  switch (rate) {
    case 1:
      s1.style.color = "rgb(241, 117, 255)";
      s2.style.color = "rgb(255, 210, 251)";
      s3.style.color = "rgb(255, 210, 251)";
      s4.style.color = "rgb(255, 210, 251)";
      s5.style.color = "rgb(255, 210, 251)";
      rateParam.innerHTML = "1 /5";
      break;
    case 2:
      s1.style.color = "rgb(241, 117, 255)";
      s2.style.color = "rgb(241, 117, 255)";
      s3.style.color = "rgb(255, 210, 251)";
      s4.style.color = "rgb(255, 210, 251)";
      s5.style.color = "rgb(255, 210, 251)";
      rateParam.innerHTML = "2 /5";

      break;
    case 3:
      s1.style.color = "rgb(241, 117, 255)";
      s2.style.color = "rgb(241, 117, 255)";
      s3.style.color = "rgb(241, 117, 255)";
      s4.style.color = "rgb(255, 210, 251)";
      s5.style.color = "rgb(255, 210, 251)";
      rateParam.innerHTML = "3 /5";

      break;
    case 4:
      s1.style.color = "rgb(241, 117, 255)";
      s2.style.color = "rgb(241, 117, 255)";
      s3.style.color = "rgb(241, 117, 255)";
      s4.style.color = "rgb(241, 117, 255)";
      s5.style.color = "rgb(255, 210, 251)";
      rateParam.innerHTML = "4 /5";

      break;
    default:
      s1.style.color = "rgb(241, 117, 255)";
      s2.style.color = "rgb(241, 117, 255)";
      s3.style.color = "rgb(241, 117, 255)";
      s4.style.color = "rgb(241, 117, 255)";
      s5.style.color = "rgb(241, 117, 255)";
      rateParam.innerHTML = "5 /5";

      break;
  }
  rateParam.setAttribute("isSet", 1);
  event.preventDefault(); // Prevent the default link behavior


  // Extract the rating value from the data-rating attribute

  // Create a data object to send in the POST request
  const data = new URLSearchParams();
  data.append('target_id', targetID);
  if(post){
    data.append('post', post);
  }
    data.append('rate', rate);

  // Make an AJAX POST request to your Django view
  fetch('/rate/', {
      method: 'POST',
      body: data,
      headers: {
          'X-CSRFToken': getCookie('csrftoken') // Add CSRF token if needed
      }
  })
  .then(response => {
      if (response.ok) {
          // Rating was updated successfully, you can handle success here
      } else {
      }
  })
  .catch(error => {
      console.error('Error:', error);
  });
}

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}
function readURL() {
  let input = document.getElementById("imageUpload");
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    reader.onload = function (e) {
      let image = document.getElementById("imagePreview");
      image.style.backgroundImage = "url(" + e.target.result + ")";
      // $("#imagePreview").hide();
      // $("#imagePreview").fadeIn(650);
    };
    reader.readAsDataURL(input.files[0]);
  }
}
function pressEnter(event) {
  if (event.key == "Enter")
    event.target.setAttribute("contenteditable", "false");
  event.target.setAttribute("contenteditable", "true");
}




    //////////////// Arranque //
  
  //////////////// Variáveis // Valores aqui!
  
  var valores = [150,50,62,34,45,190,230,220,170,150,73,54,240,214,210,240,214,210,92];
  var pontos = [];
  var diferenca =[];


  function drawGrid(width,height,colun,line) {
  var ctx = document.getElementById('canvas').getContext('2d');
      ctx.fillRect(0,0,width,height);
      ctx.save();
      for (var c=1; c<(width/colun); c++) {
          ctx.beginPath();
          ctx.moveTo(c*colun,0);
          ctx.lineTo(c*colun,height);
          ctx.stroke();
      }
      for (var l=1; l<(height/line); l++) {
          ctx.beginPath();
          ctx.moveTo(0,l*line);
          ctx.lineTo(width, l*line);
          ctx.stroke();
      }
  }
  
  function drawingLines (width,points,c) {
  var ctx = document.getElementById('canvas').getContext('2d');
  ctx.beginPath();
  ctx.globalAlpha = c*0.04;
  ctx.moveTo(((c-1)*width+10),points[c-1]);
  ctx.lineTo(c*width+10,points[c]);
  ctx.lineTo(c*width+10,300);
  ctx.lineTo(((c-1)*width+10),300);
  ctx.lineTo(((c-1)*width+10),points[c-1]);
  ctx.fill();
  ctx.beginPath();
   ctx.globalAlpha = 1;
  ctx.moveTo(((c-1)*width+10),points[c-1]);
  ctx.lineTo(c*width+10,points[c]);
  ctx.stroke();
  ctx.beginPath();
  ctx.save();
  ctx.fillStyle=ctx.strokeStyle;
  ctx.arc(c*width+10,points[c],3,0,Math.PI*2)
  ctx.fill();
  ctx.restore();
  }
  

  function draw() {
  var ctx = document.getElementById('canvas').getContext('2d');

  //////////////// setupBackground
  ctx.fillStyle ="#000000";
  ctx.strokeStyle ="#000000";
  ctx.save();
  drawGrid(500,300,10,10);

  
  for (var c=0; c<valores.length; c++) { 
      if(isNaN(pontos[c])){
      pontos[c]=300;
  }
  ctx.lineWidth=1.4;
  larg=480/(valores.length -1);
  diferenca[c]=(300-valores[c])-pontos[c];
  pontos[c]+=diferenca[c]/(c+1);
  
  //////////////// setupGraphic
  ctx.strokeStyle ="#F175FF";
  ctx.fillStyle="#F175FF";    
  drawingLines (larg,pontos,c);
  }
}