
--- 
creation date: <% tp.file.creation_date() %> 
modification date: <% tp.file.last_modified_date("dddd Do MMMM YYYY HH:mm:ss") %> 
name: <% tp.file.title %>


--- 

#[[<% tp.file.title %>]]
<% await tp.file.move("/docs/NPCs/" + tp.file.title) %>