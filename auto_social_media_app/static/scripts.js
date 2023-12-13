let array = ['Lying client', 'scam alert', 'fake reviews', 'bad customers', 'fraudulent customer', 'report','share experience with clients', 'report bad employee', 'bad employee', 'avoid chargebacks', 'avoid scams', 'fake refund', 'business protection', 'web directory']
        
function printKeyWords(array){
    let keyWords = document.getElementById("KeyWords");
    for(let i of array)
        keyWords.innerHTML += "<h6 class='wordKey' onclick='filtrarPalavra(this)'>" + i + "</h6>";
        
}
printKeyWords(array);

function filtrarPalavra(e){
    let word = e.innerText;
    console.log("palavra passe (" +word+") foi clicado");
    return word;
}

function obterTextoDigitado() {
    var meuInput = document.querySelector('.input1');
    var textoDigitado = meuInput.value;

    let keyWords = document.getElementById("KeyWords");
    if (!array.includes(textoDigitado))
        keyWords.innerHTML += "<h6 class='wordKey' onclick='filtrarPalavra(this)'>" + textoDigitado + "</h6>";
    
    if (!array.includes(textoDigitado))
        array.push(textoDigitado);
    return textoDigitado;
}


document.addEventListener('keydown', function(event) {
 
    if (event.key === 'Enter') {
        var textoDigitado = obterTextoDigitado();
        console.log(textoDigitado);
    }
});


function adicionarComentarios(){
    let comments = document.getElementsByClassName("comment");

    for(let eai of comments){
        eai.innerHTML += "<h6 class='nomeUsuario'>Usuario</h6>";
        eai.innerHTML += '<h3 class="TextComment">This is the comment, just testing, thank you</h3>'
        console.log(eai);
    }
        
    
}

function slideDown() {

    var elemento = document.getElementById("Comments");
    var alturaAtual = 0;
    var alturaFinal = 400; // Altura final desejada

    // Exibe o elemento (se estiver oculto)
    elemento.style.display = 'block';

    function animar() {
      alturaAtual += 5; // Ajuste a velocidade do slide ajustando esse valor

      // Se atingir a altura final, interrompe a animação
      if (alturaAtual >= alturaFinal) {
        elemento.style.height = alturaFinal + 'px';
        cancelAnimationFrame(animar);
      } else {
        // Atualiza a altura do elemento e continua a animação
        elemento.style.height = alturaAtual + 'px';
        requestAnimationFrame(animar);
      }
    }

    // Inicia a animação
    requestAnimationFrame(animar);
  }

function facebook() {
    console.log("Função Facebook chamada!");
    let startPage = document.getElementById("startPage");
    let nextPage = document.getElementById("NextPage");

    startPage.style.display = "none";
    nextPage.style.display = "block";

    let comments = document.getElementById("Comments");

    let htmlnovo = '';

    for (let i = 0; i < 10; i++)
        htmlnovo += `<div class='comment faceComment commentIndex${i}'> </div>`;

    comments.innerHTML = htmlnovo;

    adicionarComentarios();

    fadeIn(comments, 1000);
    slideDown(comments, 1500);
    window.location.href = '/facebook/';

}

function instagram(){
    let startPage = document.getElementById("startPage");
    let nextPage = document.getElementById("NextPage");

    startPage.style.display = "none";
    nextPage.style.display = "block"
    

    let comments = document.getElementById("Comments");

    let htmlnovo = ''

    for(let i = 0; i < 10; i++)
        htmlnovo += "<div class='comment faceComment commentIndex${"+i+"}'> </div>"
    
    comments.innerHTML = htmlnovo;
    
    adicionarComentarios();

    fadeIn(comments, 1000);
    slideDown(comments, 1500);
    
}

function twitter(){
    let startPage = document.getElementById("startPage");
    let nextPage = document.getElementById("NextPage");

    startPage.style.display = "none";
    nextPage.style.display = "block"
    

    let comments = document.getElementById("Comments");

    let htmlnovo = ''

    for(let i = 0; i < 10; i++)
        htmlnovo += "<div class='comment faceComment commentIndex${"+i+"}'> </div>"
    
    comments.innerHTML = htmlnovo;
    
    adicionarComentarios();

    fadeIn(comments, 1000);
    slideDown(comments, 1500);
    
}

function youtube(){
    let startPage = document.getElementById("startPage");
    let nextPage = document.getElementById("NextPage");

    startPage.style.display = "none";
    nextPage.style.display = "block"
    

    let comments = document.getElementById("Comments");

    let htmlnovo = ''

    for(let i = 0; i < 10; i++)
        htmlnovo += "<div class='comment faceComment commentIndex${"+i+"}'> </div>"
    
    comments.innerHTML = htmlnovo;
    
    adicionarComentarios();

    fadeIn(comments, 1000);
    slideDown(comments, 1500);
    
}

function back(){
    let startPage = document.getElementById("startPage");
    let nextPage = document.getElementById("NextPage");

    startPage.style.display = "block";
    nextPage.style.display = "none"
}

document.addEventListener('DOMContentLoaded', function() {
    // Espera o DOM estar completamente carregado

    // Obtém o elemento pelo ID
    var comments = document.getElementById('Comments');

    // Inicia a animação fadeIn
    fadeIn(comments, 1000); // 1000 ms (1 segundo) de duração
});

function fadeIn(elemento, duration) {
    var startTime = performance.now();

    function updateOpacity() {
        var currentTime = performance.now();
        var progress = (currentTime - startTime) / duration;

        if (progress < 1) {
            var opacityValue = Math.min(progress, 1);
            elemento.style.opacity = opacityValue;
        } else {
            clearInterval(animationInterval);
            elemento.style.opacity = 1; // Garante que a opacidade seja 1 no final
        }
    }

    var animationInterval = setInterval(updateOpacity, 16); // Atualiza a cada 16 ms (aproximadamente 60 FPS)
}


//relógio
const horas = document.getElementById('horas');
const minutos = document.getElementById('minutos');
const segundos = document.getElementById('segundos');

const relogio = setInterval(function() {
    let dateToday = new Date();

    let hr = dateToday.getHours();
    let min = dateToday.getMinutes();
    let s = dateToday.getSeconds();

    if(hr < 10) hr = '0' + hr;
    if(min < 10) min = '0' + min;
    if(s < 10) s = '0' + s;

    horas.textContent = hr;
    minutos.textContent = min;
    segundos.textContent = s;

})

//para aparecer o reply
let comment = document.getElementsByClassName('comment');

function adicionarEvento(comment) {
    for(let objeto of comment){
        objeto.addEventListener('mouseover', function() {
        // Configurar um temporizador para esperar 0.5 segundos
        setTimeout(function() {
            // Exibir mensagem no console após 0.5 segundos
            console.log("0.5");
        }, 500);
        }); 
    }
}

adicionarEvento(comment);