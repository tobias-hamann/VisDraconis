<%* 
let title = tp.file.title 
if (title.startsWith("Untitled")) {
title = await tp.system.prompt("Session Titel"); 
sessionNum = await tp.user.getThisGameNum(tp);
await tp.file.rename(`${sessionNum}_${title}`); 
} tR += "---" 
%>
creation date: <% tp.file.creation_date() %> 
modification date: <% tp.file.last_modified_date("dddd Do MMMM YYYY HH:mm:ss") %> 
name: <%* tR += `${title}` %>
type: dm_session 
campaign: VisDraconis
sessionNum: <%* tR += `${sessionNum}` %>
Summary: ""
sessionDate: 
tags:
--- 

# [[<% tp.config.target_file.basename %>]]
<% await tp.file.move("/DM/DM_Sessions/" + tp.config.target_file.basename) %>
Tags: 

Vorherige Session: 
```dataview
LIST
WHERE sessionNum = <%* tR += `${sessionNum-1}` %>
```
Nachfolgende Session: 
```dataview
LIST
WHERE sessionNum = <%* tR += `${sessionNum-(-1)}` %>
```

### Informationen:
