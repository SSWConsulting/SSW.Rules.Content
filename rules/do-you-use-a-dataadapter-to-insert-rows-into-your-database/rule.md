---
type: rule
archivedreason: 
title: Do you use a DataAdapter to insert rows into your database?
guid: 75a90696-0dce-4dae-a37c-6dedcd62d08a
uri: do-you-use-a-dataadapter-to-insert-rows-into-your-database
created: 2009-05-05T05:30:52.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
  noimage: true
related: []
redirects: []

---

There are 5 common methods of inserting rows into your database:  
<!--endintro-->

1. Use SqlCommand with an SQL INSERT statement and parameters:
        
        <pre>public void SQLInsert(string customerID, string companyName, string contactName)
&#123;
    SqlConnection sqlcon = new SqlConnection();
    sqlcon.ConnectionString = &quot;Persist Security Info=False; 
               Integrated Security=SSPI;database=northwindJV;
               server=(local);Connect Timeout=5&quot;;
    SqlCommand sqlcmd = new SqlCommand();
    sqlcmd.CommandText = &quot;INSERT Customers(CustomerID, CompanyName, 
                ContactName) VALUES(@CustomerID, @CompanyName, @ContactName)&quot;;
    sqlcmd.Connection = sqlcon;
    sqlcmd.Parameters.Add(&quot;@CustomerID&quot;, customerID);
    sqlcmd.Parameters.Add(&quot;@CompanyName&quot;, companyName);
    sqlcmd.Parameters.Add(&quot;@ContactName&quot;, contactName);
    
    ... // for all columns
    
    &#160;try
    &#123;
        sqlcon.Open();
        MessageBox.Show(&quot;The number of records updated was&#58; &quot; 
        + sqlcmd.ExecuteNonQuery().ToString());
    &#125;
    finally
   &#123;
        sqlcon.Close();
   &#125;
&#125;</pre>
        
        <dd>&#160;&#160;&#160;&#160; Figure&#58; Inserting rows using INSERT </dd>
        This approach has two problems - the SQL is inline in the code, and if the database schema is changed, INSERT statement will have to be manually updated.
2. Use SqlCommand and a stored procedure on the SQL Server:
        
        <pre>public void SPInsert(string firstName, string surname)
&#123;
    &#160;&#160;&#160;&#160;SqlConnection sqlcon = new SqlConnection();
    &#160;&#160;&#160;&#160;sqlcon.ConnectionString = &quot;Persist Security Info=False;Integrated Security=SSPI; database=northwind;server=mySQLServer;Connect Timeout=30&quot;;
    &#160;&#160;&#160;&#160;SqlCommand sqlcmd = new SqlCommand();
    &#160;&#160;&#160;&#160;sqlcmd.CommandText = &quot;proc_InsertCustomer&quot;;
    &#160;&#160;&#160;&#160;sqlcmd.CommandType = CommandType.StoredProcedure;
    &#160;&#160;&#160;&#160;sqlcmd.Connection = sqlcon;
    &#160;&#160;&#160;&#160;sqlcmd.Parameters.Add(&quot;@firstName&quot;, firstName);
    &#160;&#160;&#160;&#160;sqlcmd.Parameters.Add(&quot;@surname&quot;, surname);
    &#160;&#160;&#160;&#160;... // for all columns
    &#160;&#160;&#160;&#160;try
    &#160;&#160;&#160;&#160;&#123;
        &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;sqlcon.Open();
        &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;sqlcmd.ExecuteNonQuery();
    &#160;&#160;&#160;&#160;&#125;
    &#160;&#160;&#160;&#160;finally
    &#160;&#160;&#160;&#160;&#123;
        &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;sqlcon.Close();
    &#160;&#160;&#160;&#160;&#125;
&#125;</pre>
        
        <dd>&#160;&#160;&#160;&#160; Figure&#58; Inserting rows using SqlCommand and a stored procedure on the SQL Server </dd>
        This method is better because the SQL is not mixed up with the code (it is in a stored procedure), but it will still break if the database schema is changed, and the all of the parameters to the stored procedure have to be added manually.
3. Use DataAdapter with SQL INSERT statement, then use DataApdater.Update (strongly-typed-dataset)
        
        <pre style="padding-left&#58;15px;">public void DASQLInsert(string firstName, string surname)
&#123;
    &#160;&#160;&#160;&#160;SqlConnection sqlcon = new SqlConnection();
    &#160;&#160;&#160;&#160;sqlcon.ConnectionString = &quot;Persist Security Info=False; Integrated Security=SSPI; database=northwind; server=mySQLServer;Connect Timeout=30&quot;;
    &#160;&#160;&#160;&#160;SqlCommand sqlcmd = new SqlCommand();
    &#160;&#160;&#160;&#160;sqlcmd.CommandText = &quot;INSERT Customers(firstName, surname) 
                  VALUES(@firstName, @surname)&quot;;
    &#160;&#160;&#160;&#160;sqlcmd.Connection = sqlcon;
    &#160;&#160;&#160;&#160;SqlDataAdapter sqladp = new SqlDataAdapter();
    &#160;&#160;&#160;&#160;sqladp.InsertCommand = sqlcmd;
    
    &#160;&#160;&#160;&#160;NorthWindCustomer dst = new NorthWindCustomer();
    &#160;&#160;&#160;&#160;NorthWindCustomer.CustomerRow row = dst.Customer.NewCustomerRow();
    &#160;&#160;&#160;&#160;row.FirstName = firstName;
    &#160;&#160;&#160;&#160;row.Surname = surname;
    &#160;&#160;&#160;&#160;dst.Customer.AddCustomerRow(row);
    &#160;&#160;&#160;&#160;try
    &#160;&#160;&#160;&#160;&#123;
        &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;slqcon.Open();
        &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;sqladp.Update(dst);
    &#160;&#160;&#160;&#160;&#125;
    &#160;&#160;&#160;&#160;finally
    &#160;&#160;&#160;&#160;&#123;  
        &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;sqlcon.Close();
    &#160;&#160;&#160;&#160;&#125;
&#125;</pre>
        
        <dd>&#160;&#160;&#160;&#160;&#160; Figure&#58; Inserting rows using DataAdapter with SQL INSERT statement, then use DataApdater.Update </dd>
        In this example, the SQL is mixed up with the .NET code, and has to be manually updated if the database schema is changed. However, the strongly typed DataSet automatically updates when the database schema changes.
4. Use DataAdapter with a stored procedure for INSERT, then use DataAdapter.Update (strongly-typed-dataset)
        
        <pre>public void DASPInsert(string firstName, string surname)
&#123;
    &#160;&#160;&#160;&#160;SqlConnection sqlcon = new SqlConnection();
    &#160;&#160;&#160;&#160;sqlcon.ConnectionString = &quot;Persist Security Info=False;
                  Integrated Security=SSPI; database=northwind;
                  server=mySQLServer;Connect Timeout=30&quot;;
    &#160;&#160;&#160;&#160;SqlCommand sqlcmd = new SqlCommand();
    &#160;&#160;&#160;&#160;sqlcmd.CommandText = &quot;proc_InsertCustomer&quot;;
    &#160;&#160;&#160;&#160;sqlcmd.CommandType = CommandType.StoredProcedure;
    &#160;&#160;&#160;&#160;sqlcmd.Connection = sqlcon;
    &#160;&#160;&#160;&#160;SqlDataAdapter sqladp = new SqlDataAdapter();
    &#160;&#160;&#160;&#160;sqladp.InsertCommand = sqlcmd;
    &#160;&#160;&#160;&#160;NorthWindCustomer dst = new NorthWindCustomer();
    &#160;&#160;&#160;&#160;NorthWindCustomer.CustomerRow row = dst.Customer.NewCustomerRow();
    &#160;&#160;&#160;&#160;row.FirstName = firstName;
    &#160;&#160;&#160;&#160;row.Surname = surname;
    &#160;&#160;&#160;&#160;dst.Customer.AddCustomerRow(row);
    
    &#160;&#160;&#160;&#160;try
    &#160;&#160;&#160;&#160;&#123;
        &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;sqlcon.Open();
        &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;sqladp.Update(dst);
    &#160;&#160;&#160;&#160;&#125;
    &#160;&#160;&#160;&#160;catch
    &#160;&#160;&#160;&#160;&#123;
        &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;MessageBox.Show(
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;Unable to open connection.&quot;,
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;Error&quot;, MessageBoxButtons.OK, MessageBoxIcon.Error);
    &#160;&#160;&#160;&#160;&#125;
    &#160;&#160;&#160;&#160;finally
    &#160;&#160;&#160;&#160;&#123;
        &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;sqlcon.Close();
    &#160;&#160;&#160;&#160;&#125;
&#125;</pre>
        
        <dd>&#160;&#160;&#160;&#160;&#160;Figure&#58; Inserting rows using DataAdapter with a stored procedure for INSERT, then use DataAdapter.Update (strongly-typed-dataset) - best for SQL Server </dd>
        This is the best approach for Microsoft SQL Server. The parameters for the stored procedure are automatically generated and the strongly typed dataset updates when the database schema changes.
5. Use DataAdapter with SQL SELECT statement, then use command builder to automatically create INSERT, UPDATE and DELETE statements as required. Then use DataAdapter.Update (strongly-typed-dataset).
        
        <pre>public void DACmdb(string firstName, string surname)
&#123;
    &#160;&#160;&#160;&#160;SqlConnection sqlcon = new SqlConnection();
    &#160;&#160;&#160;&#160;sqlcon.ConnectionString = &quot;Persist Security Info=False;
                  Integrated Security=SSPI; database=northwind;
                  server=mySQLServer;Connect Timeout=30&quot;;
    &#160;&#160;&#160;&#160;SqlCommand sqlcmd = new SqlCommand();
    &#160;&#160;&#160;&#160;sqlcmd.CommandText = &quot;SELECT firstName, surname FROM Customers&quot;;
    &#160;&#160;&#160;&#160;sqlcmd.Connection = sqlcon;
    &#160;&#160;&#160;&#160;SqlDataAdapter sqladp = new SqlDataAdapter();
    &#160;&#160;&#160;&#160;sqladp.SelectCommand = sqlcmd;
    &#160;&#160;&#160;&#160;SqlCommandBuilder cmdb = new SqlCommandBuilder(adp);
    
    &#160;&#160;&#160;&#160;NorthWindCustomer dst = new NorthWindCustomer();
    &#160;&#160;&#160;&#160;NorthWindCustomer.CustomerRow row = dst.Customer.NewCustomerRow();
    &#160;&#160;&#160;&#160;row.FirstName = firstName;
    &#160;&#160;&#160;&#160;row.Surname = surname;
    &#160;&#160;&#160;&#160;dst.Customer.AddCustomerRow(row);
    
    &#160;&#160;&#160;&#160;try
    &#160;&#160;&#160;&#160;&#123;
        &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;sqlcon.Open();
        &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;sqladp.Update(dst);
    &#160;&#160;&#160;&#160;&#125;
    &#160;&#160;&#160;&#160;catch
    &#160;&#160;&#160;&#160;&#123;
        &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;MessageBox.Show(
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;Unable to open connection.&quot;,
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;Error&quot;, MessageBoxButtons.OK, MessageBoxIcon.Error);
    &#160;&#160;&#160;&#160;&#125;
    &#160;&#160;&#160;&#160;finally
    &#160;&#160;&#160;&#160;&#123;
        &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;sqlcon.Close();
    &#160;&#160;&#160;&#160;&#125;
&#125;</pre>
        
        <dd>&#160;&#160;&#160;&#160; Figure&#58; Inserting rows using DataAdapter with SQL SELECT statement, then use command builder to automatically create INSERT, UPDATE and DELETE - best for SQL Server</dd>
        This approach is the best approach for Jet (Access) databases, as stored procedures in Access are difficult to implement and unreliable. The INSERT statement is automatically generated by .NET and the strongly typed databases update when the database schema is changed.
