function getThisGameNum (tp) {
    let thisCampaign = tp.file.folder(false);
    
    let numOfGames = app.plugins.plugins.dataview.api
        .pages(`"docs/Sessions"`)
        .where(page => {
            if (page.type === 'session') {
                return true
            }
        }).length

        numOfGames = JSON.stringify(numOfGames+1);
        while (numOfGames.length<3) {
            numOfGames = "0" + numOfGames
        }
        return numOfGames
}
module.exports = getThisGameNum;