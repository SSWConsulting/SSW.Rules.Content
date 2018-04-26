---
type: rule
title: Do you use "using" declaration instead of use explicitly "dispose"?
uri: do-you-use-using-declaration-instead-of-use-explicitly-dispose
created: 2018-04-26T20:56:47.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> Don't explicitly use &quot;dispose&quot; to close objects and dispose of them, the &quot;using&quot; statement will do all of them for you. It is another awesome tool that helps reduce coding effort and possible issues. <br>​<br> </span>

<p class="ssw15-rteElement-CodeArea">SqlConnection conn = null; <br>SqlCommand cmd = null; <br>try <br>&#123; <br>conn = new SqlConnection(ConnectionString); <br>cmd = new SqlCommand(sql, conn); <br>conn.Open(); <br>cmd.ExecuteNonQuery(); <br>&#125; <br>catch(SqlException ex) <br>&#123; <br>... <br>&#125; <br>finally <br>&#123; <br>if(cmd!=null) <br>&#123;cmd.Dispose();&#125; <br>if(conn!=null) <br>&#123;conn.Dispose();&#125; <br>&#125; <br></p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad example of dispose of resources<br></dd><p><br></p><p class="ssw15-rteElement-CodeArea">FileStream fs = new FileStream(filePath, FileMode.Open, FileAccess.Read); <br>StreamReader sr = new StreamReader(fs);&#160;</p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad example of dispose of resources <br></dd><p>​<br></p><p class="ssw15-rteElement-CodeArea">try <br>&#123; <br>using (SqlConnection conn = new SqlConnection(ConnectionString)) <br>&#123; <br>using (cmd = new SqlCommand(sql, conn)) <br>&#123; <br>conn.Open(); <br>cmd.ExecuteNonQuery(); <br>conn.Close(); <br>&#125; <br>&#125; <br>&#125; <br>catch(SqlException ex) <br>&#123; <br>... <br>&#125; <br></p><p></p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good example of dispose of resources <br></dd><p class="ssw15-rteElement-CodeArea">using(FileStream fs = new FileStream(filePath, FileMode.Open, FileAccess.Read)) <br>&#123; <br>using(StreamReader sr = new StreamReader(fs)) <br>&#123; <br>... <br>&#125; <br>&#125;</p><dd class="ssw15-rteElement-FigureGood"> Figure&#58; Good example of&#160;dispose&#160;of resources&#160; ​</dd><p>​<br></p>


