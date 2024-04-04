
--- 
creation date: <% tp.file.creation_date() %> 
modification date: <% tp.file.last_modified_date("dddd Do MMMM YYYY HH:mm:ss") %> 
name: <% tp.config.target_file.basename %>


--- 

#[[<% tp.config.target_file.basename %>]]
<% await tp.file.move("/docs/NPCs/" + tp.config.target_file.basename) %>

<% tp.frontmatter.name %>