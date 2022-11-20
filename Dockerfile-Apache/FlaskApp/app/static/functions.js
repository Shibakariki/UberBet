var cardNumber;
var betCard = null;
var betVal;

function getNbJetons()
{
    if (isNaN(parseInt(recupererCookie("ckitonbjt-v2"))))
    {
        return 0;
    }
    else
    {
        return parseInt(recupererCookie("ckitonbjt-v2"));
    }
}

function setNbJetons(nbJetons)
{
    supprimerCookie("ckitonbjt-v2");
    creerCookie("ckitonbjt-v2",nbJetons,1);
    redirect("resetJetons",recupererCookie("name"));
}

//TODO:Fonction qui check dans la bdd le nombre de jetons

function sleep(milliseconds) {  
    return new Promise(resolve => setTimeout(resolve, milliseconds));  
}  

async function game()
{
    var multiple = 2;
    if(betCard != null)
    {
        var winnerCard = Math.floor(Math.random() * 4)+1;
        showWait();
        await sleep(3000);  
        if(winnerCard == betCard)
        {
            setNbJetons(getNbJetons() + betVal*multiple - betVal);
        }
        else
        {
            setNbJetons(getNbJetons() - betVal);
        }
        reset();
        refreshScore();
        closeWait();
    }
    else
    {
        alert("Vous n'avez pas encore parié sur une carte")
    }
    return;
}

function refreshScore() {
    if(recupererCookie("name") != null)
    {
        var number = getNbJetons().toString();
        document.getElementById("nbJetons").innerHTML = number + " Jetons";
    }
    else
    {
        document.getElementById("nbJetons").innerHTML = "S'inscrire";
    }
    var loc = window.location.toString().split("/");
    if(loc[loc.length-2]=="erreur")
    {
        var lb = document.getElementById(loc[loc.length-1].toString());
        if (lb != null)
        {
            lb.style.color = "#ff0000";
        }
    }
    return;
}

function getLoc()
{
    var tmp = window.location.toString().split("/");
    if (tmp[tmp.length-2] == "erreur")
    {
        tmp.splice(tmp.length-1,2);
    }
    else
    {
        tmp.splice(tmp.length-1,1);
    }
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
        window.location.href = loc+"/inscription";
    }
    return;
}

function deconnexionRedirection()
{
    redirect("deconnexion");
}

function redirect(param=null){
    var page = getLoc() + "/" + this.id.split("-")[0].toString();
    if (param != null)
    {
        page += "/"+param;
    }
    window.location.href = page;
}

function redirect(page_name,param=null){
    var page = getLoc() + "/" + page_name;
    if (param != null)
    {
        page += "/"+param;
    }
    window.location.href = page;
}

function redirectBack(){
    var page = getLoc();
    window.location.href = page;
}

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
        closeModal();
    }
});

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
                if(number <= getNbJetons())
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