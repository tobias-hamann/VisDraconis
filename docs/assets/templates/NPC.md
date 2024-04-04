
--- 
creation date: <% tp.file.creation_date() %> 
modification date: <% tp.file.last_modified_date("dddd Do MMMM YYYY HH:mm:ss") %> 
name: <% tp.file.title %>


--- 
<< [[<% tp.date.now("YYYY-MM-DD", -1) %>]] | [[<% tp.date.now("YYYY-MM-DD", 1) %>]] >> # <% tp.file.title %> <% tp.web.daily_quote() %>