---
type: rule
archivedreason: 
title: Do you version your .xml files?
guid: fe869a35-0ca6-4558-89ac-3e79ef775018
uri: do-you-version-your-xml-files
created: 2009-04-29T06:07:29.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
  noimage: true
related: []
redirects: []

---

It is good to store program settings in an .xml file. But developers rarely worry about future schema changes and how they will inform the user it is an old schema.

 What is wrong with this?

<!--endintro-->


```xml
<?xml version="1.0" standalone="yes"?>
<NewDataSet>
  <xs:schema id="NewDataSet" xmlns=""
     xmlns:xs="http://www.w3.org/2001/XMLSchema"
     xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">
    <xs:element name=NewDataSet" msdata:IsDataSet="true" msdata:Locale="en-AU">
    <xs:complexType>
      <xs:choice maxOccurs="unbounded">
       <xs:element name="Table1">
       <xs:complexType>
       <xs:sequence>
       <xs:element name="DateUpdated" type="xs:dateTime" minOccurs="0" />
       <xs:element name="NewDatabase" type="xs:boolean" minOccurs="0" />
       <xs:element name="ConnectionString" type="xs:string" minOccurs="0" />
       <xs:element name="SQLFilePath" type="xs:string" minOccurs="0" />
       <xs:element name="TimeOut" type="xs:int" minOccurs="0" />
       <xs:element name="TurnOnMSDE" type="xs:boolean" minOccurs="0" />
       <xs:element name="KeepXMLRecords" type="xs:boolean" minOccurs="0" />
       <xs:element name="UserMode" type="xs:boolean" minOccurs="0" />
       <xs:element name="ReconcileScriptsMode" type="xs:boolean" minOccurs="0" />
       <xs:element name="FolderPath" type="xs:string" minOccurs="0" /> />
       <xs:element name="SelectedFile" type="xs:string" minOccurs="0" />
       <xs:element name="UpdateVersionTable" type="xs:boolean" minOccurs="0" />
       </xs:sequence>
       </xs:complexType>
       </xs:element>
      </xs:choice>
     </xs:complexType>
     </xs:element>
    </xs:schema>
 
    <Table1>
      <DateUpdated>2004-05-17T10:04:06.9438192+10:00</DateUpdated>
      <NewDatabase>true</NewDatabase>
      <ConnectionString>Provider=SQLOLEDB.1;Integrated Security=SSPI;
      Persist Security Info=False;
      Data Source=(local);Initial Catalog=master</ConnectionString>
      <SQLFilePath>ver0001.sql</SQLFilePath>
      <TimeOut>5</TimeOut>
      <TurnOnMSDE>false</TurnOnMSDE>
      <KeepXMLRecords>false</KeepXMLRecords>
      <UserMode>true</UserMode>
      <ReconcileScriptsMode>true</ReconcileScriptsMode>
      <FolderPath>C:\Program Files\SSW SQL Deploy\Samples\DatabaseSQLScripts\
      </FolderPath>
      <SelectedFile />
      <UpdateVersionTable>true</UpdateVersionTable>
    </Table1>
</NewDataSet>
```
::: bad
Bad example - XML file without version control       
:::

```xml
<?xml version="1.0" standalone="yes"?>
<NewDataSet>
  <xs:schema id="NewDataSet" xmlns=""
     xmlns:xs="http://www.w3.org/2001/XMLSchema"
     xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">
    <xs:element name=NewDataSet" msdata:IsDataSet="true" msdata:Locale="en-AU">
    <xs:complexType>
      <xs:choice maxOccurs="unbounded">
       <xs:element name="Table1">
       <xs:complexType>
       <xs:sequence>
       <xs:element name="Version" type="xs:string" minOccurs="0" />
       <xs:element name="DateUpdated" type="xs:dateTime" minOccurs="0" />
       <xs:element name="NewDatabase" type="xs:boolean" minOccurs="0" />
       <xs:element name="ConnectionString" type="xs:string" minOccurs="0" />
       <xs:element name="SQLFilePath" type="xs:string" minOccurs="0" />
       <xs:element name="TimeOut" type="xs:int" minOccurs="0" />
       <xs:element name="TurnOnMSDE" type="xs:boolean" minOccurs="0" />
       <xs:element name="KeepXMLRecords" type="xs:boolean" minOccurs="0" />
       <xs:element name="UserMode" type="xs:boolean" minOccurs="0" />
       <xs:element name="ReconcileScriptsMode" type="xs:boolean" minOccurs="0" />
       <xs:element name="FolderPath" type="xs:string" minOccurs="0" /> />
       <xs:element name="SelectedFile" type="xs:string" minOccurs="0" />
       <xs:element name="UpdateVersionTable" type="xs:boolean" minOccurs="0" />
       </xs:sequence>
       </xs:complexType>
       </xs:element>
      </xs:choice>
     </xs:complexType>
     </xs:element>
    </xs:schema>
 
   <Table1>
      <Version>1.2</Version> 
      <DateUpdated>2004-05-17T10:04:06.9438192+10:00</DateUpdated>
      <NewDatabase>true</NewDatabase>
      <ConnectionString>Provider=SQLOLEDB.1;Integrated Security=SSPI;
      Persist Security Info=False;
      Data Source=(local);Initial Catalog=master</ConnectionString>
      <SQLFilePath>ver0001.sql</SQLFilePath>
      <TimeOut>5</TimeOut>
      <TurnOnMSDE>false</TurnOnMSDE>
      <KeepXMLRecords>false</KeepXMLRecords>
      <UserMode>true</UserMode>
      <ReconcileScriptsMode>true</ReconcileScriptsMode>
      <FolderPath>C:\Program Files\SSW SQL Deploy\Samples\DatabaseSQLScripts\
      </FolderPath>
      <SelectedFile />
      <UpdateVersionTable>true</UpdateVersionTable>
    </Table1>
</NewDataSet>
```
::: good
Good example - XML file with version control   
:::

The version tags identifies what version the file is. This version should be hard coded into the application. Every time you change the format of the file, you would increment this number.

The code below shows how this would be implemented in your project.

```vb
Public Function IsXMLFileValid() As Boolean

  Dim fileVersion As String = "not specified"
  Dim dsSettings As New DataSet
  Dim IsMalformed As Boolean = False 
  ' Is the file malformed all together with possibly version

  Try
    dsSettings.ReadXml(mXMLFileInfo.FullName, XmlReadMode.ReadSchema)
  Catch ex As Exception
    IsMalformed = True
  End Try

  If (Not IsMalformed) Then
    Dim strm As Stream = Asm.GetManifestResourceStream(Asm.GetName().Name _ 
     + "." + "XMLFileSchema.xsd")
    Dim sReader As New StreamReader(strm)
    Dim dsXMLSchema As New DataSet
    dsXMLSchema.ReadXmlSchema(sReader)

    If dsSettings.Tables(0).Columns.Contains("Version") Then _
      fileVersion = dsSettings.Tables(0).Rows(0)("Version").ToString
    End If

    If fileVersion = "" Then
      fileVersion = "not specified"
    End If

    If fileVersion = Global.XMLFileVersion AndAlso 
        Not dsSettings.GetXmlSchema() = dsXMLSchema.GetXmlSchema() Then
      Return False
    End If

  End If

  If IsMalformed OrElse fileVersion <> Global.XMLFileVersion Then

    If mshouldConvertFile Then
      ' Convert the file
      ConvertToCurrentVersion(IsMalformed)
    Else
      Throw New XMLFileVersionException(fileVersion, Global.XMLFileVersion )
    End If

  End If

  Return True

End Function
```
**Figure: Code to illustrate how to check if the xml file is valid** 

::: info
**Note:** to allow backward compatibility, you should give the user an option to convert old xml files into the new version structure.
:::
