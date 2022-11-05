var cardNumber;
var betCard = null;
var allJetons = 100;
var betVal;

//TODO:Fonction qui check dans la bdd le nombre de jetons

function game()
{
    var multiple = 2;
    if(betCard != null)
    {
        var winnerCard = Math.floor(Math.random() * 4)+1;
        showWait();
        if(winnerCard == betCard)
        {
            allJetons += betVal*multiple - betVal;
        }
        else
        {
            allJetons -= betVal;
        }
        reset();
        refreshScore();
    }
    else
    {
        alert("Vous n'avez pas encore parié sur une carte")
    }
    return;
}

function refreshScore() {
    creerCookie("name","axel",1);
    if(recupererCookie("name") != null)
    {
        var number = allJetons.toString();
        document.getElementById("nbJetons").innerHTML = number + " Jetons";
    }
    else
    {
        document.getElementById("nbJetons").innerHTML = "S'inscrire";
    }
    return;
}

function getLoc()
{
    var tmp = window.location.toString().split("/");
    tmp.splice(tmp.length-1,1);
    var tmp2 = tmp.join("/");
    return tmp2;
}

function jetonsRedirection()
{
    var loc = getLoc();
    if(recupererCookie("name") != null)
    {
        window.location.href = loc+"/add";
    }
    else
    {
        window.location.href = loc+"/main";
    }
    return;
}

// var bttn = document.getElementById('main-redirect');
// bttn.addEventListener('click', redirect, true);

// function redirect(){
//     var page = getLoc() + "/" + this.id.split("-")[0].toString();
//     window.location.href = page;
// }

var elements = document.getElementsByClassName("modal-reset");
for (var i = 0; i < elements.length; i++) {
    elements[i].addEventListener('click', reset, false);
}

var elements = document.getElementsByClassName("modal-show");

for (var i = 0; i < elements.length; i++) {
    elements[i].addEventListener('click', showModal, false);
}

function showModal()
{
    if(betCard == null)
    {
        cardNumber = this.id.split("-")[2];
        var modals = document.getElementsByClassName("modal");
        for(m in modals)
        {
            if(modals[m].className == "modal" && modals[m].id == "modal-input")
            {
                modals[m].className = "modal is-active";
            }
        }    
    }
    return;
}

function showWait()
{
    var modals = document.getElementsByClassName("modal");
    for(m in modals)
    {
        if(modals[m].className == "modal" && modals[m].id == "modal-wait")
        {
            modals[m].className = "modal is-active";
        }
    }   
    return;
}
function closeWait()
{
    var modals = document.getElementsByClassName("modal");
    for(m in modals)
    {
        if(modals[m].className == "modal is-active" && modals[m].id == "modal-wait")
        {
            modals[m].className = "modal";
        }
    }
    return;
}

function closeAllModal()
{
    closeWait();
    closeModal();
}

document.addEventListener('keydown', (event) => {
    const e = event || window.event;

    if (e.keyCode === 27) { // Escape key
        closeAllModal();
    }
});
var elements = document.querySelectorAll('.modal-close, .modal-background');

for (var i = 0; i < elements.length; i++) {
    elements[i].addEventListener('click', closeAllModal, false);
}

document.addEventListener('keydown', (event) => {
    const e = event || window.event;

    if (e.keyCode === 27) { // Escape key
        closeModal();
    }
});
var elements = document.querySelectorAll('.modal-close, .modal-background');

for (var i = 0; i < elements.length; i++) {
    elements[i].addEventListener('click', closeModal, false);
}

function closeModal()
{
    var modals = document.getElementsByClassName("modal");
    for(m in modals)
    {
        if(modals[m].className == "modal is-active" && modals[m].id == "modal-input")
        {
            var number = document.getElementById("bet").value;
            number = parseInt(number)
            if(Number.isInteger(number) && number > 0)
            {
                if(number <= allJetons)
                {
                    refreshBet(number);
                    betCard = cardNumber;
                }
                else
                {
                    //TODO:faire un modal pour remplacer l'alert
                    alert("Vous n'avez pas assez de jetons");
                }
            }
            else
            {
                //TODO:faire un modal pour remplacer l'alert
                alert("Vous n'avez pas renseignés un nombre entier positif");
            }
            modals[m].className = "modal";
        }
    }
    return;
}

function reset()
{
    cardNumber = this.id != null ?this.id.split("-")[2] : cardNumber;
    refreshBet(0);
    return;
}

function refreshBet(number)
{
    var betJetons = "betJetons"+cardNumber.toString();
    if(number != 0)
    {
        document.getElementById(betJetons).innerHTML = number.toString() + " jeton(s)";
        betCard = cardNumber;
        betVal = document.getElementById("bet").value;
    }
    else
    {
        document.getElementById(betJetons).innerHTML = "";
        betCard = null;
    }
    document.getElementById("bet").value = "";
    return;
}