using YamlDotNet.RepresentationModel;


var rulesDir = Environment.GetFolderPath(Environment.SpecialFolder.Desktop) + "/SSW.Rules.Content/rules";

if (!Directory.Exists(rulesDir))
{
    Console.WriteLine($"The '{rulesDir}' directory does not exist.");
    return;
}

foreach (var ruleFolder in Directory.GetDirectories(rulesDir))
{
    var rulePath = Path.Combine(rulesDir, ruleFolder);
    var ruleMdPath = Path.Combine(rulePath, "rule.md");

    if (File.Exists(ruleMdPath))
    {
        try
        {
            var readAllText = File.ReadAllText(ruleMdPath);
            var parts = readAllText.Split("---");
            var ruleYaml = parts[1];
            var yamlStream = new YamlStream();
            yamlStream.Load(new StringReader(ruleYaml));
            var ruleData = (YamlMappingNode)yamlStream.Documents[0].RootNode;
            var redirectsNode = ruleData.Children.Keys.FirstOrDefault(key => key.ToString() == "redirects");

            if (redirectsNode != null)
            {
                var redirects = (YamlSequenceNode)ruleData.Children[redirectsNode];
                foreach (var redirect in redirects)
                {
                    var redirectFolder = Path.Combine(rulesDir, redirect.ToString());
                    if (Directory.Exists(redirectFolder))
                    {
                        // Console.WriteLine($"Moving files from left-behind folder '{redirect}' to '{ruleFolder}'");

                        
                        // Check if the redirectFolder has a rule.md file
                        var redirectRuleMdPath = Path.Combine(redirectFolder, "rule.md");
                        if (File.Exists(redirectRuleMdPath))   
                        {
                            Console.WriteLine("⚠️ Still a rule in here! Skipping...");
                            Console.WriteLine(redirectRuleMdPath);
                            continue;
                        }

                        // Move files from old folder to the new folder
                        foreach (var fullFileName in Directory.GetFiles(redirectFolder))
                        {
                            var filename = fullFileName.Split("/").Last();
                            
                            var oldFilePath = Path.Combine(redirectFolder, filename);
                            var newFilePath = Path.Combine(rulePath, filename);
                            
                            File.Move(oldFilePath, newFilePath, false);
                            Console.WriteLine("✅ Migrated " + filename);
                        }

                        // Remove the old folder
                        // Directory.Delete(redirectFolder);
                    }
                }
            }
        }
        catch (Exception e)
        {
            Console.WriteLine($"Error processing rule '{ruleFolder}': {e}");
        }
    }
}
