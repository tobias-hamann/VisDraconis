
<%* 
let title = tp.file.title 
if (title.startsWith("Untitled")) {
title = await tp.system.prompt("Title"); 
await tp.file.rename(`${title}`); 
} tR += "---" 
%>

--- 
creation date: <% tp.file.creation_date() %> 
modification date: <% tp.file.last_modified_date("dddd Do MMMM YYYY HH:mm:ss") %> 
name: <%* tR += `${title}` %>
faction:

--- 

#[[<% tp.config.target_file.basename %>]]

<% await tp.file.move("/docs/NPCs/" + tp.config.target_file.basename) %>

Name:

Appearance:
![<% tp.file.tags%>](../assets/images/<% tp.config.target_file.basename %>.png)