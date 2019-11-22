

---
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> <p class="ssw15-rteElement-P">The SQL 2005 generated scripts are not compatible to SQL 2000, so use SQL 2000 to generate your scripts if you want to make your scripts work well on both versions.​​<br></p> </span>

<p class="ssw15-rteElement-CodeArea" style="width&#58;770.031px;">IF EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[ProcessTarget]') AND type in (N'P', N'PC'))<br>drop procedure [dbo].[ProcessTarget]</p><dd class="ssw15-rteElement-FigureNormal">Figure&#58; script only works on SQL 2005, because 'sys.objects' is only available in this version<br></dd><p class="ssw15-rteElement-CodeArea" style="width&#58;770.031px;">IF EXISTS (SELECT * FROM dbo.sysobjects WHERE id = OBJECT_ID(N'[dbo].[ProcessTarget]') AND OBJECTPROPERTY(id, N'IsProcedure') = 1)<br>drop procedure [dbo].[ProcessTarget]</p><dd class="ssw15-rteElement-FigureNormal">Figure&#58; script works on both SQL 2000 and SQL 2005​<br></dd>


