---
type: rule
title: Do you always use the Visual Studio designer for data binding where possible?
uri: do-you-always-use-the-visual-studio-designer-for-data-binding-where-possible
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T05:36:00.000Z
guid: d399f81c-1fd7-4112-9b44-25dcaa2dd85b
related:
- do-you-always-use-the-visual-studio-designer-for-data-binding-where-possible

---
Basic data binding should always be done in the designer because the syntax for data binding is complex, and confusing for other developers reading the code.

<!--endintro-->

![Figure: Simple data binding (binding to a single property) in the designer](simpledatabindingdesigner.gif)

![Figure: Complex data binding (binding to a list) in the designer](complexdatabindingdesigner.gif)

When you need to handle the Format or binding events, you can still use designer data binding, as long as you hook in your events prior to filling data.

```cs
private void Form1_Load(object sender, System.EventArgs e)
{
   Binding currencyBinding = this.textBox1.DataBindings("Text");
   currencyBinding.Format += new 
      ConvertEventHandler(currencyBinding_Format);
   currencyBinding.Parse +=
      new ConvertEventHandler(currencyBinding_Parse);

   OrderDetailsService.Instance.GetAll(Me.OrderDetailsDataSet1);	
}

private void currencyBinding_Format(object sender, ConvertEventArgs e)
{
   if(e.DesiredType == typeof(string))
   {
      e.Value = ((decimal)e.Value).ToString("c");
   }
}

private void currencyBinding_Parse(object sender, ConvertEventArgs e)
{
   if(e.DesiredType == typeof(decimal))
   {
      e.Value = Decimal.Parse(e.Value.ToString(),
         System.Globalization.NumberStyles.Currency);
   }
}
```

```cs
//
// Designer auto generated code.
//
private void InitializeComponent()
{
    this.cmbTumorQuad = new System.Windows.Forms.ComboBox();
		
    //
    // cmbTumorQuad
    //
    this.requiredValidator1.SetCustomValidationEnabled(this.cmbTumorQuad, true);
    this.cmbTumorQuad.DataBindings.Add(new System.Windows.Forms.Binding("SelectedValue", this.dvOccMain, "TumorQuadrant"));
    this.cmbTumorQuad.DataSource = this.dvTumorQuad;
    this.cmbTumorQuad.DisplayMember = "Description";
    this.requiredValidator1.SetDisplayName(this.cmbTumorQuad, "");
}
```
::: good
Figure: Good example - DataBinding in Designer
:::

```cs
private void DataBind()
{
    ChangeBinding(txtRuleName.DataBindings,	"Text", jobRules, "RuleData.RuleName");
    ChangeBinding(cmbFileFilter.DataBindings, "Text", jobRules, "RuleData.FileFilter");
    ChangeBinding(txtSearchString.DataBindings, "Text", jobRules, "RuleData.SearchString");
    ChangeBinding(txtCreatedBy.DataBindings, "Text" , jobRules, "RuleData.EmpCreated");
}
	
protected Binding ChangeBinding(ControlBindingsCollection bindings, string propertyName, 
object dataSource, string dataMember, ConvertEventHandler eFormat, ConvertEventHandler eParse) 
{
    Binding b = bindings[propertyName];
    if ( b != null )
        bindings.Remove(b);
    b = new Binding(propertyName, dataSource, dataMember);
    bindings.Add(b);
    return b;
}
```
::: bad
Figure: Bad example - DataBinding in Code
:::

```cs
private void DataBind()
{
    //Header
    picRuleType.Image = Core.GetRuleTypeImage((RuleType)rule.RuleType, 48);
    ruleNameTextBox.Text = rule.RuleName;

    //General Tab
    notesTextBox.Text = rule.RuleDescription;
    ruleUrlTextBox.Text = rule.RuleURL;

    //Search Tab
    cboRuleType.SelectedValue = (RuleType)rule.RuleType;
    searchForTextBox.Text = rule.SearchString;
    shouldExistComboBox.SelectedIndex = (rule.ShouldExist == true ? 0 : 1);

    //Change History Tab
    createdByTextBox.Text = rule.EmpCreated;
    dateCreatedTextBox.Text = rule.DateCreated.ToString();
    lastUpdatedByTextBox.Text = rule.EmpUpdated;
    dateLastUpdatedTextBox.Text = rule.DateUpdated.ToString();
}
```
::: bad
Figure: Bad example - Set controls' values in Code
:::

