function creerCookie(nom, contenu, jours) {
    var e = null;
    var date = new Date();
    date.setTime(date.getTime() + (jours * 24 * 60 * 60 * 1000));
    e = "; expires=" + date.toGMTString();
    document.cookie = nom + "=" + contenu + e + "; path=/";
}

function recupererCookie(nom) {
    nom = nom + "=";
    var liste = document.cookie.split(';');
    for (var i = 0; i < liste.length; i++) {
        var c = liste[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nom) == 0) return c.substring(nom.length, c.length);
    }
    return null;
}

function supprimerCookie(nom)
{
    var date = new Date();
    date.setTime(date.getTime()-1000);
    document.cookie = nom+"=; expires="+date.toGMTString()+ "; path=/";;
}